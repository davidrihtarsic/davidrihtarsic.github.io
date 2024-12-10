SHRANJEVANJE POGOVORA
================================================================================

Funkcija za shranjevanje pogovora v datoteko je zaželena, saj je spremljanje učnega 
toka zelo pomembno iz didaktičnega vidika. Najenostavneje je, da pogovor shranimo v
`json` datoteko, tako so podatki lepo urejeni.

```python
import json

def shrani_pogovor(zgodovina_pogovora, ime_datoteke="pogovor.json"):
    """
    Shrani zgodovino pogovora v JSON datoteko.
    Args:
        zgodovina_pogovora (list): Seznam sporočil v zgodovini pogovora.
        ime_datoteke (str): Ime datoteke, kamor se shrani pogovor (privzeto: "pogovor.json").
    Delovanje:
    - Pretvori seznam sporočil v JSON format.
    - Shrani JSON podatke v datoteko.
    - Preveri, če datoteka že obstaja, in jo prepiše, če je to potrebno.
    """
    try:
        # Odpremo datoteko za pisanje
        with open(ime_datoteke, "w", encoding="utf-8") as datoteka:
            json.dump(zgodovina_pogovora, datoteka, indent=4, ensure_ascii=False)
        print(f"Pogovor je bil uspešno shranjen v datoteko '{ime_datoteke}'.")
    except Exception as e:
        print(f"Prišlo je do napake pri shranjevanju pogovora: {str(e)}")
```

---

### **Ključne značilnosti funkcije:**
1. **Vhodni parametri:**
   - `zgodovina_pogovora`: Seznam, ki vsebuje sporočila v obliki slovarjev (npr. `{"role": "user", "content": "vprašanje"}`).
   - `ime_datoteke`: Ime datoteke, kamor se shrani pogovor (privzeto `pogovor.json`).

2. **JSON format:**
   - Podatki se shranijo v čitljiv JSON format z zamiki (indent=4) in brez kodiranja znakov (`ensure_ascii=False`).

3. **Prepisovanje datoteke:**
   - Če datoteka že obstaja, jo funkcija prepiše z novo zgodovino.

4. **Obravnava napak:**
   - Če pride do težave (npr. težave z dostopom do datoteke), funkcija izpiše ustrezno sporočilo.

---

### **Primer uporabe funkcije:**

```python
# Primer zgodovine pogovora
zgodovina_pogovora = [
    {"role": "system", "content": "Ti si pomočnik za tehniko in tehnologijo."},
    {"role": "user", "content": "Kaj je električni tok?"},
    {"role": "assistant", "content": "Električni tok je tok električnih nabojev skozi prevodnik."}
]

# Shrani zgodovino v datoteko
shrani_pogovor(zgodovina_pogovora)
```

---

NALAGANJE POGOVORA OB ZAGONU PROGRAMA
================================================================================
---

### **Funkcija za nalaganje zgodovine pogovora**

```python
def nalozi_pogovor(ime_datoteke="pogovor.json"):
    """
    Naloži zgodovino pogovora iz JSON datoteke.
    Args:
        ime_datoteke (str): Ime datoteke, iz katere se naloži pogovor (privzeto: "pogovor.json").
    Returns:
        list: Seznam sporočil iz zgodovine pogovora (če datoteka obstaja in je veljavna).
              Če datoteka ne obstaja ali je prazna, vrne prazen seznam.
    Delovanje:
    - Preveri, ali datoteka obstaja.
    - Če obstaja, prebere podatke iz datoteke in jih pretvori v Pythonov seznam.
    - Če datoteka ne obstaja ali je prazna, vrne prazen seznam.
    """
    try:
        # Poskusi odpreti in prebrati datoteko
        with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
            pogovor = json.load(datoteka)
            print(f"Zgodovina pogovora je uspešno naložena iz '{ime_datoteke}'.")
            return pogovor
    except FileNotFoundError:
        print(f"Datoteka '{ime_datoteke}' ne obstaja. Ustvarjen bo nov pogovor.")
        return []
    except json.JSONDecodeError:
        print(f"Datoteka '{ime_datoteke}' je poškodovana ali ni veljaven JSON. Ustvarjen bo nov pogovor.")
        return []
    except Exception as e:
        print(f"Prišlo je do napake pri nalaganju pogovora: {str(e)}")
        return []
```

---

### **Ključne značilnosti funkcije:**
1. **Vhodni parametri:**
   - `ime_datoteke`: Ime datoteke, ki vsebuje shranjeno zgodovino pogovora.

2. **Obravnava napak:**
   - Če datoteka ne obstaja (`FileNotFoundError`), funkcija vrne prazen seznam in ustvari novo zgodovino.
   - Če datoteka ni veljaven JSON (`JSONDecodeError`), se uporabnika opozori in vrne prazen seznam.
   - Drugi nepredvideni problemi so obravnavani z generično izjemo.

3. **Rezultat:**
   - Funkcija vrne zgodovino pogovora kot seznam sporočil ali prazen seznam, če datoteka ne obstaja ali je poškodovana.

---

### **Primer uporabe funkcije:**

```python
# Naloži zgodovino pogovora (če obstaja)
zgodovina_pogovora = nalozi_pogovor()

# Dodaj nov pogovor (če želimo nadaljevati ali začeti na novo)
zgodovina_pogovora.append({"role": "user", "content": "Kako deluje motor na električni pogon?"})

# Shrani posodobljeno zgodovino
shrani_pogovor(zgodovina_pogovora)
```

---

### **Integracija v program**
Tukaj je, kako bi povezali obe funkcionalnosti v obstoječi program:

1. Ob zagonu programa najprej poskusimo naložiti obstoječo zgodovino:
   ```python
   zgodovina_pogovora = nalozi_pogovor()
   ```

2. Ob vsakem novem vprašanju uporabnika posodobimo zgodovino:
   ```python
   def poslji_vprasanje(prompt):
       ...
       # Posodobi zgodovino
       shrani_pogovor(zgodovina_pogovora)
   ```

---

### **Zakaj je to koristno?**
- Uporabnik lahko kadarkoli nadaljuje pogovor tam, kjer je končal.
- Zgodovina pogovora je trajno shranjena in dostopna za kasnejšo analizo ali pregled.

Če želiš, lahko dodamo še funkcionalnost za izbiro različne zgodovine (npr. uporabnik lahko shrani pogovore pod različnimi imeni). Kaj meniš?

