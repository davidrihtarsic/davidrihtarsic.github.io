#!/usr/bin/env python3
import argparse
import csv
from functools import wraps
import io
import json
import os
import re
import secrets
import socket
import sqlite3
import time
from datetime import datetime
from pathlib import Path

from flask import Flask, Response, abort, jsonify, redirect, render_template, request, send_file, send_from_directory, session, url_for
from markupsafe import Markup, escape
import qrcode
import qrcode.image.svg
from werkzeug.utils import secure_filename

BASE_DIR = Path(__file__).resolve().parent
QUIZ_DIR = BASE_DIR / "quizzes"
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "quiz.db"
TEACHER_PIN_PATH = DATA_DIR / "teacher_pin.txt"

for p in (QUIZ_DIR, DATA_DIR):
    p.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)
SECRET_PATH = DATA_DIR / "secret.key"
if os.environ.get("QUIZ_SECRET"):
    app.secret_key = os.environ["QUIZ_SECRET"]
elif SECRET_PATH.exists():
    app.secret_key = SECRET_PATH.read_text(encoding="utf-8").strip()
else:
    app.secret_key = secrets.token_hex(32)
    SECRET_PATH.write_text(app.secret_key, encoding="utf-8")
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024
app.config["QUIZ_PORT"] = 5000

ALLOWED_IMAGES = {"png", "jpg", "jpeg", "gif", "webp", "svg"}


def markdown_text(value):
    """Render the small Markdown/math subset used in quiz text safely."""
    text = escape(str(value or ""))
    text = re.sub(r"_\{([^{}]+)\}", r"<sub>\1</sub>", text)
    text = re.sub(r"\^\{([^{}]+)\}", r"<sup>\1</sup>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return Markup(text)


app.jinja_env.filters["markdown"] = markdown_text
def teacher_pin():
    env_pin = os.environ.get("QUIZ_TEACHER_PIN", "").strip()
    if env_pin:
        return env_pin
    if TEACHER_PIN_PATH.exists():
        pin = TEACHER_PIN_PATH.read_text(encoding="utf-8").strip()
        if pin:
            return pin
    pin = f"{secrets.randbelow(1_000_000):06d}"
    TEACHER_PIN_PATH.write_text(pin, encoding="utf-8")
    try:
        os.chmod(TEACHER_PIN_PATH, 0o600)
    except OSError:
        pass
    return pin


TEACHER_PIN = teacher_pin()


def teacher_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("teacher_authenticated"):
            next_url = request.full_path if request.query_string else request.path
            if request.method == "GET":
                return redirect(url_for("teacher_login", next=next_url))
            abort(403)
        return view(*args, **kwargs)
    return wrapped


def db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    con = db()
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            quiz_file TEXT NOT NULL,
            title TEXT NOT NULL,
            created_at TEXT NOT NULL,
            active INTEGER NOT NULL DEFAULT 1
        );
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            joined_at TEXT NOT NULL,
            finished_at TEXT,
            FOREIGN KEY(session_id) REFERENCES sessions(id)
        );
        CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participant_id INTEGER NOT NULL,
            question_id TEXT NOT NULL,
            answer_json TEXT NOT NULL,
            is_correct INTEGER NOT NULL,
            points_awarded REAL NOT NULL,
            max_points REAL NOT NULL,
            response_ms INTEGER,
            answered_at TEXT NOT NULL,
            UNIQUE(participant_id, question_id),
            FOREIGN KEY(participant_id) REFERENCES participants(id)
        );
        """
    )
    columns = {row[1] for row in con.execute("PRAGMA table_info(sessions)").fetchall()}
    if "notes" not in columns:
        con.execute("ALTER TABLE sessions ADD COLUMN notes TEXT NOT NULL DEFAULT ''")
    con.commit()
    con.close()


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def safe_quiz_name(name):
    raw = str(name or "").replace("\\", "/").strip("/")
    parts = [secure_filename(part) for part in raw.split("/") if part not in {"", ".", ".."}]
    if not parts:
        parts = ["kviz"]
    if len(parts) == 1:
        parts = [Path(parts[0]).stem, parts[0]]
    else:
        parts = [parts[-2], parts[-1]]
    if not parts[1].endswith(".json"):
        parts[1] += ".json"
    return "/".join(parts)


def quiz_asset_dir(filename):
    """Return the private asset directory belonging to one quiz."""
    return QUIZ_DIR / Path(safe_quiz_name(filename)).parent


def quiz_dir_name(filename):
    return Path(safe_quiz_name(filename)).parent.name


def safe_image_name(name):
    name = secure_filename(Path(str(name or "")).name)
    if not name or "." not in name:
        return ""
    if name.rsplit(".", 1)[-1].lower() not in ALLOWED_IMAGES:
        return ""
    return name


def load_quiz(filename):
    filename = safe_quiz_name(filename)
    path = QUIZ_DIR / filename
    if not path.exists():
        # Read old flat quiz files during the one-time migration.
        legacy_path = QUIZ_DIR / Path(filename).name
        if legacy_path.exists():
            path = legacy_path
    if not path.exists():
        abort(404, "Kviz ne obstaja.")
    with path.open("r", encoding="utf-8") as f:
        quiz = json.load(f)
    return quiz, filename


def validate_quiz(quiz):
    if not isinstance(quiz, dict):
        raise ValueError("Kviz mora biti JSON objekt.")
    if not str(quiz.get("title", "")).strip():
        raise ValueError("Manjka naslov kviza.")
    questions = quiz.get("questions")
    if not isinstance(questions, list):
        raise ValueError("Polje questions mora biti seznam.")

    seen = set()
    for i, q in enumerate(questions, 1):
        if not isinstance(q, dict):
            raise ValueError(f"Vprašanje {i} ni veljaven objekt.")
        qid = str(q.get("id") or f"q{i}")
        if qid in seen:
            raise ValueError(f"Podvojen ID vprašanja: {qid}")
        seen.add(qid)
        q["id"] = qid
        qtype = q.get("type")
        if qtype not in {"single", "multiple", "true_false", "text"}:
            raise ValueError(f"Vprašanje {qid}: neznan tip {qtype}.")
        if not str(q.get("question", "")).strip():
            raise ValueError(f"Vprašanje {qid}: besedilo je prazno.")
        answers = q.get("answers", [])
        correct = q.get("correct", [])
        if not isinstance(answers, list) or not isinstance(correct, list):
            raise ValueError(f"Vprašanje {qid}: answers in correct morata biti seznama.")
        if qtype in {"single", "multiple", "true_false"}:
            if qtype == "true_false" and len(answers) != 2:
                raise ValueError(f"Vprašanje {qid}: drži/ne drži mora imeti dva odgovora.")
            if len(answers) < 2:
                raise ValueError(f"Vprašanje {qid}: premalo odgovorov.")
            for idx in correct:
                if not isinstance(idx, int) or idx < 0 or idx >= len(answers):
                    raise ValueError(f"Vprašanje {qid}: neveljaven indeks pravilnega odgovora.")
            if qtype in {"single", "true_false"} and len(correct) != 1:
                raise ValueError(f"Vprašanje {qid}: dovoljen je natanko en pravilen odgovor.")
        elif qtype == "text" and not answers:
            raise ValueError(f"Vprašanje {qid}: dodaj vsaj en sprejemljiv besedilni odgovor.")
        q["points"] = float(q.get("points", 1) or 1)
        q["difficulty"] = int(q.get("difficulty", 1) or 1)
        q["time"] = int(q.get("time", 0) or 0)
        q.setdefault("topic", "")
        q.setdefault("image", "")
        try:
            q["image_width"] = max(1, min(100, int(q.get("image_width", 100) or 100)))
        except (TypeError, ValueError):
            q["image_width"] = 100
    quiz.setdefault("version", 1)
    quiz.setdefault("description", "")
    return quiz


def list_quizzes():
    rows = []
    paths = list(QUIZ_DIR.glob("*/*.json")) + list(QUIZ_DIR.glob("*.json"))
    for path in sorted(paths):
        try:
            with path.open("r", encoding="utf-8") as f:
                q = json.load(f)
            rows.append({
                "file": str(path.relative_to(QUIZ_DIR)).replace("\\", "/") if path.parent != QUIZ_DIR else safe_quiz_name(path.name),
                "title": q.get("title", path.stem),
                "count": len(q.get("questions", [])),
                "description": q.get("description", ""),
            })
        except Exception:
            rows.append({"file": path.name, "title": path.stem, "count": "?", "description": "Napaka v JSON"})
    return rows


def normalize_text(value):
    value = str(value or "").strip().casefold()
    value = re.sub(r"\s+", " ", value)
    return value


def grade_question(q, submitted):
    max_points = float(q.get("points", 1))
    qtype = q["type"]
    if qtype == "text":
        value = normalize_text(submitted)
        accepted = {normalize_text(x) for x in q.get("answers", [])}
        ok = value in accepted
    else:
        if not isinstance(submitted, list):
            submitted = [submitted]
        try:
            selected = {int(x) for x in submitted}
        except (TypeError, ValueError):
            selected = set()
        expected = set(q.get("correct", []))
        ok = selected == expected
    return ok, max_points if ok else 0.0


def get_session_by_code(code):
    con = db()
    row = con.execute("SELECT * FROM sessions WHERE code=?", (code.upper(),)).fetchone()
    con.close()
    return row


def participant_authorized(code, pid):
    return session.get(f"participant_{code.upper()}") == pid


def get_participant(pid, code=None):
    con = db()
    if code:
        row = con.execute(
            "SELECT p.*, s.code, s.quiz_file, s.title AS quiz_title, s.active FROM participants p JOIN sessions s ON s.id=p.session_id WHERE p.id=? AND s.code=?",
            (pid, code.upper()),
        ).fetchone()
    else:
        row = con.execute("SELECT * FROM participants WHERE id=?", (pid,)).fetchone()
    con.close()
    return row


def local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return "127.0.0.1"


def join_url_for(code):
    base_url = os.environ.get("QUIZ_BASE_URL", "").strip().rstrip("/")
    if base_url:
        return f"{base_url}/join/{code.upper()}"
    return f"http://{local_ip()}:{app.config.get('QUIZ_PORT', 5000)}/join/{code.upper()}"


@app.route("/teacher-login", methods=["GET", "POST"])
def teacher_login():
    if session.get("teacher_authenticated"):
        return redirect(url_for("index"))
    error = ""
    if request.method == "POST":
        pin = request.form.get("pin", "").strip()
        if secrets.compare_digest(pin, TEACHER_PIN):
            session["teacher_authenticated"] = True
            target = request.form.get("next", "").strip()
            if target.startswith("/") and not target.startswith("//"):
                return redirect(target)
            return redirect(url_for("index"))
        error = "Napačen učiteljski PIN."
    return render_template("teacher_login.html", error=error, next_url=request.args.get("next", ""))


@app.post("/teacher-logout")
@teacher_required
def teacher_logout():
    session.pop("teacher_authenticated", None)
    return redirect(url_for("teacher_login"))


@app.route("/")
@teacher_required
def index():
    con = db()
    recent = con.execute("SELECT code,title,created_at,active FROM sessions ORDER BY id DESC LIMIT 8").fetchall()
    con.close()
    return render_template("index.html", quizzes=list_quizzes(), sessions=recent, lan_ip=local_ip())


@app.route("/editor")
@teacher_required
def editor():
    return render_template("editor.html", quizzes=list_quizzes(), selected=request.args.get("file", ""))


@app.get("/api/quiz")
@teacher_required
def api_quiz_get():
    filename = request.args.get("file", "")
    if not filename:
        return jsonify({"version": 1, "title": "Nov kviz", "description": "", "questions": []})
    quiz, filename = load_quiz(filename)
    return jsonify({"file": filename, "quiz": quiz})


@app.post("/api/quiz/save")
@teacher_required
def api_quiz_save():
    payload = request.get_json(force=True)
    filename = safe_quiz_name(payload.get("file") or payload.get("quiz", {}).get("title", "kviz"))
    try:
        quiz = validate_quiz(payload.get("quiz", {}))
    except ValueError as e:
        return jsonify({"ok": False, "error": str(e)}), 400
    path = QUIZ_DIR / filename
    quiz_asset_dir(filename).mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(quiz, f, ensure_ascii=False, indent=2)
    return jsonify({"ok": True, "file": filename})


@app.post("/api/quiz/import")
@teacher_required
def api_quiz_import():
    up = request.files.get("file")
    if not up:
        return jsonify({"ok": False, "error": "Datoteka manjka."}), 400
    try:
        quiz = json.load(up.stream)
        quiz = validate_quiz(quiz)
    except Exception as e:
        return jsonify({"ok": False, "error": f"Neveljaven JSON: {e}"}), 400
    filename = safe_quiz_name(up.filename or quiz.get("title", "kviz"))
    quiz_asset_dir(filename).mkdir(parents=True, exist_ok=True)
    with (QUIZ_DIR / filename).open("w", encoding="utf-8") as f:
        json.dump(quiz, f, ensure_ascii=False, indent=2)
    return jsonify({"ok": True, "file": filename})


@app.post("/api/image")
@teacher_required
def api_image():
    up = request.files.get("file")
    if not up or not up.filename:
        return jsonify({"ok": False, "error": "Slika manjka."}), 400
    quiz_file = request.form.get("quiz_file", "")
    if not quiz_file:
        return jsonify({"ok": False, "error": "Ime kviza manjka."}), 400
    ext = up.filename.rsplit(".", 1)[-1].lower() if "." in up.filename else ""
    if ext not in ALLOWED_IMAGES:
        return jsonify({"ok": False, "error": "Nepodprt format slike."}), 400
    name = f"{int(time.time())}_{secrets.token_hex(4)}.{ext}"
    asset_dir = quiz_asset_dir(quiz_file)
    asset_dir.mkdir(parents=True, exist_ok=True)
    up.save(asset_dir / name)
    return jsonify({"ok": True, "path": name})


@app.get("/quiz-image/<quiz_name>/<path:image>")
def quiz_image(quiz_name, image):
    """Serve only an image from the selected quiz's own asset directory."""
    image_name = safe_image_name(image)
    if not image_name:
        abort(404)
    # Keep old quizzes readable while they are being moved to their own folder.
    if str(image).replace("\\", "/").startswith("uploads/"):
        legacy_dir = BASE_DIR / "static" / "uploads"
        if (legacy_dir / image_name).is_file():
            return send_from_directory(legacy_dir, image_name)
    quiz_name = secure_filename(quiz_name)
    asset_dir = QUIZ_DIR / quiz_name
    if not (asset_dir / image_name).is_file():
        abort(404)
    return send_from_directory(asset_dir, image_name)


@app.get("/quiz/export/<path:filename>")
@teacher_required
def export_quiz(filename):
    _, filename = load_quiz(filename)
    return send_file(QUIZ_DIR / filename, as_attachment=True, download_name=Path(filename).name)


@app.post("/session/start")
@teacher_required
def start_session():
    filename = request.form.get("quiz_file", "")
    quiz, filename = load_quiz(filename)
    validate_quiz(quiz)
    con = db()
    while True:
        code = "".join(secrets.choice("ABCDEFGHJKLMNPQRSTUVWXYZ23456789") for _ in range(6))
        exists = con.execute("SELECT 1 FROM sessions WHERE code=?", (code,)).fetchone()
        if not exists:
            break
    con.execute(
        "INSERT INTO sessions(code,quiz_file,title,created_at,active) VALUES(?,?,?,?,1)",
        (code, filename, quiz.get("title", filename), now_iso()),
    )
    con.commit()
    con.close()
    return redirect(url_for("teacher", code=code))


@app.post("/session/<code>/stop")
@teacher_required
def stop_session(code):
    con = db()
    con.execute("UPDATE sessions SET active=0 WHERE code=?", (code.upper(),))
    con.commit()
    con.close()
    return redirect(url_for("teacher", code=code))


@app.post("/session/<code>/resume")
@teacher_required
def resume_session(code):
    con = db()
    con.execute("UPDATE sessions SET active=1 WHERE code=?", (code.upper(),))
    con.commit()
    con.close()
    return redirect(url_for("teacher", code=code))


@app.post("/session/<code>/update")
@teacher_required
def update_session(code):
    con = db()
    con.execute("UPDATE sessions SET notes=? WHERE code=?", (request.form.get("notes", "").strip()[:5000], code.upper()))
    con.commit()
    con.close()
    return redirect(url_for("teacher", code=code))


@app.post("/session/<code>/delete")
@teacher_required
def delete_session(code):
    con = db()
    row = con.execute("SELECT id FROM sessions WHERE code=?", (code.upper(),)).fetchone()
    if not row:
        con.close()
        abort(404)
    participant_ids = [r[0] for r in con.execute("SELECT id FROM participants WHERE session_id=?", (row["id"],)).fetchall()]
    if participant_ids:
        placeholders = ",".join("?" for _ in participant_ids)
        con.execute(f"DELETE FROM answers WHERE participant_id IN ({placeholders})", participant_ids)
    con.execute("DELETE FROM participants WHERE session_id=?", (row["id"],))
    con.execute("DELETE FROM sessions WHERE id=?", (row["id"],))
    con.commit()
    con.close()
    return redirect(url_for("index"))


@app.route("/join", methods=["GET", "POST"])
def join_code():
    if request.method == "POST":
        code = request.form.get("code", "").strip().upper()
        return redirect(url_for("join", code=code))
    return render_template("join_code.html")


@app.route("/join/<code>", methods=["GET", "POST"])
def join(code):
    sess = get_session_by_code(code)
    if not sess:
        return render_template("message.html", title="Kviz ne obstaja", message="Preveri vstopno kodo."), 404
    if not sess["active"]:
        return render_template("message.html", title="Kviz je zaključen", message="Ta seja ne sprejema več odgovorov."), 403
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            return render_template("join.html", s=sess, error="Vpiši ime ali vzdevek.")
        con = db()
        cur = con.execute(
            "INSERT INTO participants(session_id,name,joined_at) VALUES(?,?,?)",
            (sess["id"], name[:80], now_iso()),
        )
        pid = cur.lastrowid
        con.commit()
        con.close()
        session[f"participant_{code.upper()}"] = pid
        return redirect(url_for("take", code=code, pid=pid))
    return render_template("join.html", s=sess, error="")


@app.route("/take/<code>/<int:pid>")
def take(code, pid):
    p = get_participant(pid, code)
    if not p:
        abort(404)
    if not participant_authorized(code, pid):
        abort(403)
    if not p["active"]:
        return redirect(url_for("student_result", code=code, pid=pid))
    quiz, quiz_file = load_quiz(p["quiz_file"])
    questions = quiz.get("questions", [])
    con = db()
    answered_rows = con.execute("SELECT question_id FROM answers WHERE participant_id=?", (pid,)).fetchall()
    con.close()
    answered = {r["question_id"] for r in answered_rows}
    q = next((x for x in questions if str(x["id"]) not in answered), None)
    if q is None:
        con = db()
        con.execute("UPDATE participants SET finished_at=COALESCE(finished_at,?) WHERE id=?", (now_iso(), pid))
        con.commit()
        con.close()
        return redirect(url_for("student_result", code=code, pid=pid))
    idx = questions.index(q)
    return render_template(
        "take.html",
        p=p,
        quiz=quiz,
        quiz_file=quiz_file,
        quiz_dir=quiz_dir_name(quiz_file),
        q=q,
        index=idx + 1,
        total=len(questions),
        started_ms=int(time.time() * 1000),
    )


@app.post("/answer/<code>/<int:pid>/<qid>")
def answer(code, pid, qid):
    p = get_participant(pid, code)
    if not p or not p["active"] or not participant_authorized(code, pid):
        abort(403)
    quiz, _ = load_quiz(p["quiz_file"])
    q = next((x for x in quiz.get("questions", []) if str(x["id"]) == str(qid)), None)
    if not q:
        abort(404)
    qtype = q["type"]
    if qtype == "text":
        submitted = request.form.get("answer", "")
        stored = submitted
    elif qtype == "multiple":
        submitted = request.form.getlist("answer")
        stored = [int(x) for x in submitted if str(x).isdigit()]
    else:
        submitted = request.form.get("answer", "")
        stored = [int(submitted)] if str(submitted).isdigit() else []
    ok, points = grade_question(q, submitted)
    try:
        started_ms = int(request.form.get("started_ms", "0"))
        response_ms = max(0, int(time.time() * 1000) - started_ms) if started_ms else None
    except ValueError:
        response_ms = None
    con = db()
    con.execute(
        """
        INSERT INTO answers(participant_id,question_id,answer_json,is_correct,points_awarded,max_points,response_ms,answered_at)
        VALUES(?,?,?,?,?,?,?,?)
        ON CONFLICT(participant_id,question_id) DO UPDATE SET
          answer_json=excluded.answer_json,is_correct=excluded.is_correct,
          points_awarded=excluded.points_awarded,max_points=excluded.max_points,
          response_ms=excluded.response_ms,answered_at=excluded.answered_at
        """,
        (pid, str(qid), json.dumps(stored, ensure_ascii=False), int(ok), points, float(q.get("points", 1)), response_ms, now_iso()),
    )
    con.commit()
    con.close()
    return redirect(url_for("take", code=code, pid=pid))


@app.route("/result/<code>/<int:pid>")
def student_result(code, pid):
    p = get_participant(pid, code)
    if not p:
        abort(404)
    if not participant_authorized(code, pid):
        abort(403)
    con = db()
    row = con.execute(
        "SELECT COALESCE(SUM(points_awarded),0) AS score, COALESCE(SUM(max_points),0) AS max_score, COUNT(*) AS n FROM answers WHERE participant_id=?",
        (pid,),
    ).fetchone()
    con.close()
    pct = round(100 * row["score"] / row["max_score"], 1) if row["max_score"] else 0
    return render_template("student_result.html", p=p, score=row["score"], max_score=row["max_score"], pct=pct)


@app.route("/teacher/<code>")
@teacher_required
def teacher(code):
    sess = get_session_by_code(code)
    if not sess:
        abort(404)
    quiz, _ = load_quiz(sess["quiz_file"])
    join_url = join_url_for(sess["code"])
    return render_template("teacher.html", s=sess, quiz=quiz, join_url=join_url)


@app.get("/teacher/<code>/qr")
@teacher_required
def teacher_qr(code):
    sess = get_session_by_code(code)
    if not sess:
        abort(404)
    return render_template("qr_display.html", s=sess, join_url=join_url_for(sess["code"]))


@app.get("/session/<code>/qr.svg")
@teacher_required
def session_qr(code):
    sess = get_session_by_code(code)
    if not sess:
        abort(404)
    qr = qrcode.make(
        join_url_for(sess["code"]),
        image_factory=qrcode.image.svg.SvgPathImage,
        box_size=10,
        border=4,
    )
    out = io.BytesIO()
    qr.save(out)
    return Response(
        out.getvalue(),
        mimetype="image/svg+xml",
        headers={"Cache-Control": "no-store, max-age=0"},
    )


@app.route("/stats/<code>")
@teacher_required
def stats(code):
    sess = get_session_by_code(code)
    if not sess:
        abort(404)
    quiz, _ = load_quiz(sess["quiz_file"])
    return render_template("stats.html", s=sess, quiz=quiz)


@app.get("/stats/<code>/csv")
@teacher_required
def stats_csv(code):
    sess = get_session_by_code(code)
    if not sess:
        abort(404)
    quiz, _ = load_quiz(sess["quiz_file"])
    questions = quiz.get("questions", [])
    con = db()
    participants = con.execute("SELECT * FROM participants WHERE session_id=? ORDER BY name COLLATE NOCASE, id", (sess["id"],)).fetchall()
    answers = con.execute("SELECT a.* FROM answers a JOIN participants p ON p.id=a.participant_id WHERE p.session_id=?", (sess["id"],)).fetchall()
    con.close()
    amap = {(r["participant_id"], r["question_id"]): r for r in answers}
    out = io.StringIO()
    out.write("\ufeff")
    w = csv.writer(out, delimiter=";")
    w.writerow(["Študent"] + [f"V{i+1}" for i in range(len(questions))] + ["Točke", "Možne točke", "Rezultat %"])
    max_total = sum(float(q.get("points", 1)) for q in questions)
    for p in participants:
        total = 0.0
        cells = []
        for q in questions:
            a = amap.get((p["id"], str(q["id"])))
            if not a:
                cells.append("")
            else:
                total += float(a["points_awarded"])
                cells.append("1" if a["is_correct"] else "0")
        pct = round(100 * total / max_total, 1) if max_total else 0
        w.writerow([p["name"], *cells, total, max_total, pct])
    filename = f"rezultati_{sess['code']}.csv"
    return Response(out.getvalue(), mimetype="text/csv; charset=utf-8", headers={"Content-Disposition": f"attachment; filename={filename}"})


@app.get("/api/stats/<code>")
@teacher_required
def api_stats(code):
    sess = get_session_by_code(code)
    if not sess:
        return jsonify({"error": "not found"}), 404
    quiz, _ = load_quiz(sess["quiz_file"])
    questions = quiz.get("questions", [])
    con = db()
    participants = con.execute(
        "SELECT * FROM participants WHERE session_id=? ORDER BY name COLLATE NOCASE, id",
        (sess["id"],),
    ).fetchall()
    answers = con.execute(
        """
        SELECT a.* FROM answers a
        JOIN participants p ON p.id=a.participant_id
        WHERE p.session_id=?
        """,
        (sess["id"],),
    ).fetchall()
    con.close()

    answer_map = {(r["participant_id"], r["question_id"]): r for r in answers}
    matrix = []
    for p in participants:
        cells = []
        total = 0.0
        max_total = sum(float(q.get("points", 1)) for q in questions)
        answered_count = 0
        for q in questions:
            a = answer_map.get((p["id"], str(q["id"])))
            if a:
                answered_count += 1
                total += float(a["points_awarded"])
                try:
                    raw = json.loads(a["answer_json"])
                except Exception:
                    raw = a["answer_json"]
                cells.append({
                    "question_id": str(q["id"]),
                    "status": "correct" if a["is_correct"] else "wrong",
                    "points": a["points_awarded"],
                    "max_points": a["max_points"],
                    "response_ms": a["response_ms"],
                    "answer": raw,
                })
            else:
                cells.append({"question_id": str(q["id"]), "status": "empty", "points": 0, "max_points": float(q.get("points", 1)), "response_ms": None, "answer": None})
        matrix.append({
            "participant_id": p["id"],
            "name": p["name"],
            "finished": bool(p["finished_at"]),
            "answered": answered_count,
            "score": total,
            "max_score": max_total,
            "percent": round(100 * total / max_total, 1) if max_total else 0,
            "cells": cells,
        })

    per_question = []
    for i, q in enumerate(questions, 1):
        q_answers = [r for r in answers if r["question_id"] == str(q["id"])]
        correct_n = sum(1 for r in q_answers if r["is_correct"])
        avg_ms_vals = [r["response_ms"] for r in q_answers if r["response_ms"] is not None]
        avg_ms = round(sum(avg_ms_vals) / len(avg_ms_vals)) if avg_ms_vals else None
        distribution = []
        if q["type"] != "text":
            for idx, label in enumerate(q.get("answers", [])):
                n = 0
                for r in q_answers:
                    try:
                        raw = json.loads(r["answer_json"])
                        if idx in raw:
                            n += 1
                    except Exception:
                        pass
                distribution.append({"index": idx, "label": label, "count": n})
        per_question.append({
            "id": str(q["id"]),
            "number": i,
            "question": q["question"],
            "topic": q.get("topic", ""),
            "type": q["type"],
            "answered": len(q_answers),
            "correct": correct_n,
            "wrong": len(q_answers) - correct_n,
            "success": round(100 * correct_n / len(q_answers), 1) if q_answers else 0,
            "avg_ms": avg_ms,
            "distribution": distribution,
            "answers": q.get("answers", []),
        })

    completed = [m for m in matrix if m["finished"]]
    avg_percent = round(sum(m["percent"] for m in matrix) / len(matrix), 1) if matrix else 0
    return jsonify({
        "session": {"code": sess["code"], "title": sess["title"], "active": bool(sess["active"])},
        "summary": {
            "participants": len(participants),
            "completed": len(completed),
            "answers": len(answers),
            "average_percent": avg_percent,
        },
        "questions": per_question,
        "matrix": matrix,
    })


if __name__ == "__main__":
    init_db()
    parser = argparse.ArgumentParser(description="Lokalni sistem za kvize")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    print(f"\nUčiteljski dostop: http://127.0.0.1:{args.port}")
    print(f"Učiteljski PIN: {TEACHER_PIN}")
    print(f"Za študente v lokalnem omrežju: http://{local_ip()}:{args.port}/join\n")
    app.config["QUIZ_PORT"] = args.port
    app.run(host=args.host, port=args.port, debug=args.debug)
