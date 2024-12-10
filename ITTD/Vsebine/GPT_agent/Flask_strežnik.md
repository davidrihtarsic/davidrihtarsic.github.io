FLASK STREŽNIK
================================================================================

Flask je priljubljen Pythonov spletni okvir (framework), ki omogoča hitro ustvarjanje spletnih aplikacij. Povezava med Pythonom in HTML deluje tako, da Flask usmeri podatke med spletno stranjo (HTML) in strežnikom (Python).

### **1. Namestitev Flask**
Najprej namesti Flask, če še ni nameščen:
```bash
pip install flask
```

---

### **2. Osnovni koncept povezave Python in HTML**
Flask omogoča:
- Ustvarjanje strežnika za obdelavo zahtev.
- Povezovanje s HTML stranjo za prikaz rezultatov.
- Pošiljanje podatkov med Pythonom in HTML preko obrazcev (forms) ali dinamičnih vsebin.

---

### **3. Ustvarjanje preproste Flask aplikacije**

Ustvarimo si takole strukturo direktroijev in datotek:
   - Struktura mape:
     ```
     projektna_mapa/
     ├── app.py
     └── templates/
         └── index.html
     ```

#### **Korak 1: Python koda (Flask strežnik)**
```python
"""
Ta koda:
1. Zažene strežnik, ki sprejme zahteve uporabnika.
2. Pošlje HTML stran za prikaz v brskalniku.
3. Obdeluje podatke, ki jih uporabnik vnese na spletni strani.
"""

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
```

#### **Korak 2: HTML koda (index.html)**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask Uvod</title>
</head>
<body>
    <h1>Dobrodošli na Flask strani!</h1>
    <form method="post"> <!-- Obrazec za pošiljanje podatkov -->
        <label for="user_input">Vnesite vprašanje:</label><br>
        <input type="text" id="user_input" name="user_input" required><br><br>
        <input type="submit" value="Pošlji">
    </form>
    {% if odgovor %} <!-- Prikaže odgovor, če obstaja -->
    <h2>Odgovor:</h2>
    <p>{{ odgovor }}</p>
    {% endif %}
</body>
</html>
```

#### **Kaj se zgodi:**
1. Uporabnik obišče URL `http://127.0.0.1:5000/`.
2. Flask strežnik prikaže HTML stran (GET zahteva).
3. Ko uporabnik v obrazec vnese podatke in klikne "Pošlji":
   - Flask prejme podatke (POST zahteva).
   - Python obdela podatke in pošlje rezultat nazaj v HTML.

---

### **4. Kako dodamo dinamičnost z GPT-4**

#### **Spremenjena Python koda z GPT-4:**
```python
import openai
from flask import Flask, request, render_template

# Nastavi API ključ
openai.api_key = "your-api-key"

app = Flask(__name__)

def gpt_response(user_input):
    """
    Funkcija za komunikacijo z GPT-4 API.
    Sprejme uporabnikov vnos in vrne odgovor GPT.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ti si pomočnik za tehniko in tehnologijo."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Prikaže HTML stran in obdeluje uporabnikove vnose.
    """
    odgovor = ""
    if request.method == "POST":
        uporabnikov_vnos = request.form["user_input"]
        odgovor = gpt_response(uporabnikov_vnos)  # Pokliče GPT-4 za odgovor
    return render_template("index.html", odgovor=odgovor)

if __name__ == "__main__":
    app.run(debug=True)
```

#### **HTML koda ostane enaka:**
HTML del obrazca in prikaz odgovora ne potrebujeta sprememb.

---

### **5. Kako poženemo Flask aplikacijo**
1. Shrani Python kodo v datoteko, npr. `app.py`.
2. Shrani HTML kodo v mapo `templates` znotraj iste mape kot `app.py`.
   - Struktura mape:
     ```
     projektna_mapa/
     ├── app.py
     └── templates/
         └── index.html
     ```
3. Zaženi aplikacijo:
   ```bash
   python app.py
   ```
4. Odpri brskalnik in obišči `http://127.0.0.1:5000/`.

---

### **6. Ključni pojmi Flask**
- **`@app.route`**: Dekorator za določanje poti URL (npr. `/` za domačo stran).
- **`request`**: Uporablja se za pridobivanje podatkov iz obrazca (GET ali POST zahteva).
- **`render_template`**: Prikaže HTML datoteko.
- **`debug=True`**: Uporablja se za razvoj, omogoča sprotno posodabljanje aplikacije.

---

### **Naloge za študente**
1. Prilagodite HTML stran, da omogoča izbiro tem (npr. "Elektronika" ali "Mehanika").
2. Spremenite Python kodo tako, da se GPT-4 odziva glede na izbrano temo.
3. Preizkusite aplikacijo z različnimi vprašanji in prilagodite začetni `system` opis.

Če želiš, lahko pripravim bolj podrobne naloge ali dodatne razširitve!
