# Kviz sistem v0.2.1

Lokalna Flask aplikacija za pripravo in izvajanje kvizov v učilnici. Učitelj zažene strežnik na svojem računalniku, študentje pa se povežejo z brskalnikom prek istega lokalnega omrežja.

## Funkcije

- grafični urejevalnik kvizov;
- JSON kot odprt in ročno urejevalen format;
- uvoz in izvoz JSON;
- tipi vprašanj: en odgovor, več odgovorov, drži/ne drži, kratek odgovor;
- neobvezna slika, tema, zahtevnost, točke in čas;
- vstop študentov prek QR kode ali s 6-mestno kodo;
- samodejno ocenjevanje;
- učiteljski pogled v živo (osveževanje na 2 s);
- statistika za vsako vprašanje;
- skupna statistika;
- matrični prikaz študent × vprašanje;
- trajno shranjevanje sej in odgovorov v SQLite.

## Namestitev na Arch Linuxu

V terminalu odpri mapo projekta in ustvari virtualno okolje:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Nato zaženi:

```bash
./run.sh
```

ali:

```bash
python app.py --host 0.0.0.0 --port 5000
```

Učiteljski računalnik odpre:

```text
http://127.0.0.1:5000
```

Študentje v istem omrežju odprejo naslov, ki ga program izpiše ob zagonu, npr.:

```text
http://192.168.1.25:5000/join
```

## Potek uporabe

1. Ob prvem obisku učiteljskega dela vpiši PIN, ki se izpiše v terminalu ob zagonu.
2. Na domači strani izberi **Urejevalnik**.
3. Ustvari kviz in ga shrani.
4. Na domači strani pri kvizu klikni **Zaženi**.
5. Študentom pokaži QR kodo; po skeniranju se odpre neposreden vstop v sejo. Kot rezervna možnost ostaneta povezava in 6-mestna koda.
6. Učiteljski pogled sproti prikazuje odzive in matriko.
7. **Podrobna statistika** prikaže rezultate po vprašanjih in skupni matrični pregled.

## QR prijava

Ko učitelj zažene sejo, se na učiteljskem zaslonu samodejno prikaže QR koda. Koda vsebuje neposredno povezavo na trenutno sejo (`/join/KODA`), zato študent po skeniranju vpiše le svoje ime ali vzdevek. Gumb **Povečaj QR** odpre čist projekcijski pogled za prikaz na platnu.

Če aplikacijo objaviš prek drugega naslova ali reverznega posrednika, lahko osnovni naslov za QR kode nastaviš z okoljsko spremenljivko, npr.:

```bash
QUIZ_BASE_URL=https://kviz.example.si ./run.sh
```

V običajnem lokalnem omrežju to ni potrebno; aplikacija uporabi lokalni IP računalnika in izbrana vrata.

## JSON format

Primer:

```json
{
  "version": 1,
  "title": "Osnove elektronike",
  "description": "Kratek kviz",
  "questions": [
    {
      "id": "q1",
      "type": "single",
      "question": "Kolikšna je napetost ...?",
      "answers": ["0,2 V", "2 V", "5 V", "20 V"],
      "correct": [1],
      "topic": "Ohmov zakon",
      "difficulty": 1,
      "points": 1,
      "time": 30,
      "image": "",
      "image_width": 100
    }
  ]
}
```

Pri `single`, `multiple` in `true_false` so elementi `correct` indeksi pravilnih odgovorov, pri čemer je prvi odgovor indeks `0`. Pri `text` so v `answers` zapisani vsi sprejemljivi besedilni odgovori.

## Podatki

- kvizi in njihove slike: `quizzes/<ime-kviza>/<ime-kviza>.json` ter `quizzes/<ime-kviza>/*.(png|jpg|...)`
- rezultati: `data/quiz.db`

Za novo prazno bazo je dovolj, da ob ugasnjenem programu izbrišeš `data/quiz.db`; ob naslednjem zagonu se ustvari na novo.

## Učiteljski in študentski dostop

Od te različice naprej sta učiteljski in študentski del ločena:

- učiteljski **Domov**, **Urejevalnik**, upravljanje sej in statistika zahtevajo učiteljski PIN;
- PIN se ob prvem zagonu samodejno ustvari in izpiše v terminalu;
- PIN se shrani v `data/teacher_pin.txt` in ostane enak pri naslednjih zagonih;
- po želji ga lahko določiš z okoljsko spremenljivko `QUIZ_TEACHER_PIN`;
- študent, ki vstopi prek QR kode ali `/join`, vidi samo prijavo, vprašanja in svoj rezultat.
