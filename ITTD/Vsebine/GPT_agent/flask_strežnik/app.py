from flask import Flask, request, render_template

app = Flask(__name__)  # Ustvari aplikacijo

@app.route("/", methods=["GET", "POST"])  # Pot na URL-ju "/"
def index():
    """
    Glavna funkcija:
    - Če uporabnik obišče stran (GET), pokaže HTML obrazec.
    - Če uporabnik pošlje podatke (POST), jih obdelamo in vrnemo odgovor.
    """
    odgovor = ""  # Spremenljivka za odgovor
    if request.method == "POST":  # Če uporabnik pošlje obrazec
        uporabnikov_vnos = request.form["user_input"]  # Prebere vnos iz obrazca
        odgovor = f"Prejeli smo vaše vprašanje: {uporabnikov_vnos}"  # Pripravi odgovor
    return render_template("index.html", odgovor=odgovor)  # Pošlje HTML stran z odgovorom

if __name__ == "__main__":
    app.run(debug=True)  # Zaženi strežnik v načinu za razvoj
