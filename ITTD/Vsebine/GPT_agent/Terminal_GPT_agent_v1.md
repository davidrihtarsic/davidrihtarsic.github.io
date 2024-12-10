 Uporaba GPT API za izdelavo pomočnika za učitelje**
================================================================================

#### **Cilj učne ure:**
Študenti bodo spoznali, kako uporabiti GPT API za ustvarjanje preprostega asistenta, ki pomaga učiteljem pri poučevanju tehnike in tehnologije. Uporabljena bo praktična "hands-on" metoda, kjer bodo študenti korak za korakom izvajali naloge na podlagi dane kode.

---

### **1. Uvod (15 minut)**

#### **A. Teoretični del**
- Predstavitev **GPT modelov** in njihove uporabe v izobraževanju.
- Kratek pregled, kako API omogoča komunikacijo z GPT modeli.
- Pojasnilo strukture sporočil v GPT API:
  - **`role`**: določa, ali je sporočilo sistemsko, uporabniško ali od asistenta.
  - **`content`**: dejansko besedilo sporočila.
- Predstavitev strukture kode (prikazana datoteka).

#### **B. Cilji ure**
- Študenti bodo:
  - Razumeli osnovno delovanje GPT API.
  - Praktično nastavili API klice in konfigurirali sporočila.
  - Ustvarili preprostega asistenta za učitelje.

---

### **2. Priprava okolja (20 minut)**

#### **A. Namestitev knjižnice**
Študenti izvedejo namestitev potrebne knjižnice:
```bash
pip install openai
```

#### **B. Nastavitev API ključa**
1. Študenti dobijo API ključ za OpenAI (preko spletne strani).
2. Ključ shranijo kot okoljsko spremenljivko (na operacijskem sistemu):
   - **Linux/Mac:**  
     ```bash
     export OPENAI_API_KEY="tvoj-kljuc"
     ```
   - **Windows (Command Prompt):**  
     ```cmd
     set OPENAI_API_KEY=tvoj-kljuc
     ```
3. Preverijo dostop z enostavnim klicem:
   ```python
   import openai
   openai.api_key = "tvoj-kljuc"
   print("Ključ je pravilno nastavljen.")
   ```

---

### **3. Razumevanje dane kode (20 minut)**

#### **Analiza ključnih delov kode**
1. **Nastavitev API-ja**  
   - Razlaga inicializacije `OpenAI` objekta:
     ```python
     client = OpenAI(api_key="tvoj-kljuc")
     ```
   - Diskusija o uporabi sistemskih sporočil.

2. **Klic modela**  
   - Pregled `messages` strukture:
     ```python
     messages=[
         {"role": "system", "content": "Ti si pomočnik za pomoč učitelju ..."},
         {"role": "user", "content": "Predstavi se in nelo na kratko opiši tvojo nalogo."}
     ]
     ```
   - Nastavitev modela:
     ```python
     model="gpt-4o-mini", stream=True
     ```

3. **Prikaz odgovora**  
   - Uporaba `stream=True` za pridobivanje delčkov besedila:
     ```python
     for delcek_besedila in pogovor:
         print(delcek_besedila.choices[0].delta.content or "", end="")
     ```

---

### **4. Praktična vaja: Ustvarjanje asistenta (30 minut)**

#### **Naloge za študente**
1. **Nastavite pomočnika za učitelje**
   - Ustvarite sporočilo, kjer se asistent predstavi in razloži, kako lahko pomaga pri poučevanju.
2. **Spremenite namen asistenta**
   - Preoblikujte asistenta, da bo osredotočen na pomoč pri učenju specifičnega koncepta (npr. električni tokokrog).
   - Spremenite sistemsko sporočilo:
     ```python
     {"role": "system", "content": "Ti si pomočnik za razlago električnega tokokroga."}
     ```

3. **Dodajte vprašanja uporabniku**
   - Po prejemu odgovora GPT modela dodajte vprašanje za uporabnika:
     ```python
     {"role": "assistant", "content": "Kateri del ti je bil najbolj zanimiv? Povej več."}
     ```

4. **Prilagodite tok komunikacije**
   - Dodajte funkcionalnost, da uporabnik lahko odgovarja in GPT nadaljuje pogovor na podlagi prejšnjih sporočil.

---

### **5. Razširitev naloge: Raziskovanje možnosti (15 minut)**

#### **Predlogi za raziskovanje**
- **Dodajanje funkcionalnosti:** Naj študenti vključijo diagnostiko učencev z vprašanji, kot so:
  - "Kaj misliš, da je naslednji korak?"
- **Uporaba lokalne dokumentacije:** Preučite, kako vključiti zunanje vire (npr. datoteke z navodili).

---

### **6. Povzetek in diskusija (10 minut)**

- Študenti predstavijo svoje prilagoditve in ideje za izboljšanje asistenta.
- Razprava o etičnih vprašanjih in omejitvah uporabe AI pri poučevanju.

---

### **Dodatni viri**
- OpenAI Python SDK dokumentacija: [OpenAI GitHub](https://github.com/openai/openai-python)
- Primeri vprašanj za učence: Diagnostična vprašanja in prilagoditev učnega načrta.

---

**Rezultat:**
Študenti bodo praktično razumeli, kako uporabljati GPT API, in ustvarili personaliziranega asistenta, ki lahko pomaga pri poučevanju. Če želiš, lahko pripravim dodatne naloge ali prilagoditve za konkretne teme. 😊

### Priloga

```python

from openai import OpenAI

# -----------------------------------------
# Konfiguracija API-ja
# -----------------------------------------
# Nastavimo ključ za dostop do OpenAI API-ja.
# Prepričajte se, da je API ključ shranjen kot okoljska spremenljivka z imenom OPENAI_API_KEY.
# ta api ne  obstaja... potrebna menjava
client = OpenAI(
    api_key="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"  # Tukaj pridobimo API ključ iz okoljske spremenljivke
)

# -----------------------------------------
# Pošljemo sporočilo modelu
# glej navodila na:
#    https://github.com/openai/openai-python?tab=readme-ov-file#streaming-responses
# -----------------------------------------
try:
    pogovor = client.chat.completions.create(
        messages=[
            {
                "role": "system",   # Nastavitev kako naj pomočnik deluje
                "content": "Ti si pomočnik za pomoč učitelju pri poučevanju tehnike in tehnologije"
            },
            {
                "role": "user",     # Vloga pošiljatelja (uporabnik)
                "content": "Predstavi se in nelo na kratko opiši tvojo nalogo.",  # Vsebina sporočila
            }
        ],
        model="gpt-4o-mini",  # Izbrani model [gpt-40-mini je najcenejši]
        stream=True,          # Boljša izkušnja, če se delčki besedila dopolnjujejo...
    )

    # Prikaz odgovora modela
    print("GPT-4o-mini:")
    for delcek_besedila in pogovor:
        print(delcek_besedila.choices[0].delta.content or "", end="")

except Exception as e:
    print(f"Prišlo je do napake: {str(e)}")
```
