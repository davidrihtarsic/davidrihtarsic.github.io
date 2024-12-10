UPORABA GPT API ZA USTVARJANJE INTERAKTIVNEGA TUTORJA
================================================================================

#### **Cilj učne ure:**
Študenti se naučijo, kako vključiti zgodovino pogovora v GPT asistenta za izboljšanje konteksta odgovorov. Program bo prilagojen za sledenje zgodovini pogovorov in ohranjanje konteksta skozi iteracije.

---

### **1. Pregled in uvod (10 minut)**

#### **Kaj je novo?**
- V tem programu se zgodovina pogovorov shrani v obliki seznama slovarjev.
- GPT asistent uporablja zadnjih 5 sporočil iz zgodovine za generiranje odgovorov.
- Uporaba `stream=True` omogoča sprotno generiranje in prikaz odgovorov.

#### **Povezava s prejšnjo uro:**
- Študenti so spoznali osnovno strukturo GPT klicev.
- Zdaj razširjamo funkcionalnost z vključitvijo zgodovine pogovora za bolj smiselne in koherentne odgovore.

---

### **2. Razlaga nadgrajene kode (15 minut)**

#### **Ključne izboljšave v kodi:**

1. **Uvedba zgodovine pogovora:**
   - Zgodovina je seznam slovarjev, kjer vsak element predstavlja sporočilo.
   - Primer začetne konfiguracije:
     ```python
     zgodovina_pogovora = [
         {
             "role": "system",
             "content": "Ti si pomočnik za pomoč učitelju pri poučevanju tehnike in tehnologije"
         }
     ]
     ```
   - Vloga `"system"` določa osnovni kontekst za asistenta.

2. **Dinamično dodajanje uporabniških sporočil:**
   - Ob vsakem vprašanju uporabnika se to doda v `zgodovina_pogovora`:
     ```python
     zgodovina_pogovora.append({"role": "user", "content": vprasanje})
     ```

3. **Uporaba zadnjih 5 sporočil:**
   - Omejitev na zadnjih 5 sporočil zmanjšuje število tokenov in izboljša učinkovitost:
     ```python
     messages=zgodovina_pogovora[-5:]
     ```

4. **Streaming odgovorov:**
   - Omogoča sprotno pridobivanje delov odgovora, kar izboljša uporabniško izkušnjo:
     ```python
     for delcek_besedila in pogovor:
         print(delcek_besedila.choices[0].delta.content or "", end="")
     ```

5. **Obravnava napak:**
   - Uporaba `try-except` za obravnavo izjem, če API klic ne uspe:
     ```python
     except Exception as e:
         print(f"Prišlo je do napake: {str(e)}")
     ```

---

### **3. Praktična vaja (35 minut)**

#### **Naloge za študente:**

1. **Preizkusite obstoječo funkcionalnost:**
   - Zaženite program in vnesite več vprašanj.
   - Opazujte, kako GPT asistent uporablja zgodovino pogovora za oblikovanje odgovorov.

2. **Dodajte shranjevanje zgodovine v datoteko:**
   - Ustvarite funkcijo za zapis `zgodovina_pogovora` v JSON datoteko:
     ```python
     import json
     def shrani_zgodovino(ime_datoteke="zgodovina.json"):
         with open(ime_datoteke, "w", encoding="utf-8") as datoteka:
             json.dump(zgodovina_pogovora, datoteka, indent=4, ensure_ascii=False)
     ```

3. **Implementirajte nalaganje zgodovine iz datoteke:**
   - Ustvarite funkcijo za nalaganje shranjene zgodovine:
     ```python
     def nalozi_zgodovino(ime_datoteke="zgodovina.json"):
         try:
             with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
                 return json.load(datoteka)
         except FileNotFoundError:
             return []
     ```

4. **Prilagodite kodo za nadaljevanje pogovora:**
   - Na začetku programa preverite, ali obstaja shranjena zgodovina, in jo naložite:
     ```python
     zgodovina_pogovora = nalozi_zgodovino()
     ```

5. **Preverjanje vpliva zgodovine na odgovore:**
   - Poskusite spremeniti število sporočil, ki jih GPT uporablja iz zgodovine (npr. zadnjih 3 sporočil namesto 5).

---

### **4. Razširitve (10 minut)**

#### **Ideje za nadaljnje raziskovanje:**
- **Dodajanje uporabniških identitet:**  
  - Prilagodite `system` vlogo glede na uporabnika (npr. učitelj, učenec).
- **Vizualizacija zgodovine pogovora:**  
  - Prikaz zgodovine pogovora v terminalu pred vsakim novim vprašanjem.
- **Analiza pogovora:**  
  - Dodajte funkcijo, ki analizira, ali je GPT asistent uspešno ohranil kontekst.

---

### **5. Povzetek in diskusija (10 minut)**

#### **Ključna vprašanja za študente:**
- Kako zgodovina pogovora vpliva na odgovore GPT asistenta?
- Kako bi izboljšali tok informacij, da bi bil asistent bolj učinkovit?
- Katere dodatne funkcionalnosti bi želeli vključiti?

---

### **Rezultat:**
Študenti bodo nadgradili svojega GPT asistenta, da bo uporabljal zgodovino pogovorov za bolj kontekstualne odgovore. Prav tako bodo razumeli, kako delati z datotekami za shranjevanje in nalaganje podatkov.

Če želiš, lahko pripravim še dodatne naloge ali razširitve na podlagi tega programa! 😊
