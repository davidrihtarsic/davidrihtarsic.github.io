BERLJIVOST PROGRAMSKE KODE
================================================================================

Python omogoča modularno programiranje, kjer lahko funkcije in drugo kodo razdelimo na ločene datoteke (module) in jih vključimo v glavni program. Tukaj je, kako to naredimo:

---

### **1. Struktura projektne mape**
Ustvarimo projektno mapo s to strukturo:

```
moj_program/
├── main.py          # Glavni program
├── funkcije.py      # Modul s funkcijami
└── pomozne_funkcije/
    ├── __init__.py  # Omogoča, da je mapa 'pomocne_funkcije' modul
    └── shranjevanje.py # Modul za funkcije shranjevanja
```

---

### **2. Modul s funkcijami (npr. `funkcije.py`)**

V datoteko `funkcije.py` shranimo splošne funkcije, ki jih želimo uporabiti v glavnem programu.

#### Primer: `funkcije.py`
```python
def pozdravi_uporabnika():
    """
    Pozdravi uporabnika.
    """
    print("Dobrodošli v programu!")

def izhod():
    """
    Izpiše sporočilo ob izhodu iz programa.
    """
    print("Hvala za uporabo programa. Nasvidenje!")
```

---

### **3. Modul za shranjevanje (npr. `pomozne_funkcije/shranjevanje.py`)**

V podmapo `pomozne_funkcije` dodamo funkcije za shranjevanje in nalaganje podatkov.

#### Primer: `pomozne_funkcije/shranjevanje.py`
```python
import json

def shrani_podatke(podatki, ime_datoteke="podatki.json"):
    """
    Shrani podatke v JSON datoteko.
    """
    try:
        with open(ime_datoteke, "w", encoding="utf-8") as datoteka:
            json.dump(podatki, datoteka, indent=4, ensure_ascii=False)
        print(f"Podatki so bili uspešno shranjeni v datoteko '{ime_datoteke}'.")
    except Exception as e:
        print(f"Napaka pri shranjevanju: {str(e)}")

def nalozi_podatke(ime_datoteke="podatki.json"):
    """
    Naloži podatke iz JSON datoteke.
    """
    try:
        with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
            return json.load(datoteka)
    except FileNotFoundError:
        print(f"Datoteka '{ime_datoteke}' ne obstaja. Ustvarjeni bodo novi podatki.")
        return {}
    except Exception as e:
        print(f"Napaka pri nalaganju podatkov: {str(e)}")
        return {}
```

---

### **4. Glavni program (npr. `main.py`)**

V datoteki `main.py` uvozimo in uporabimo funkcije iz modulov.

#### Primer: `main.py`
```python
# Uvoz funkcij iz različnih modulov
from funkcije import pozdravi_uporabnika, izhod
from pomozne_funkcije.shranjevanje import shrani_podatke, nalozi_podatke

# Glavna funkcija programa
def main():
    pozdravi_uporabnika()

    # Nalaganje obstoječih podatkov
    podatki = nalozi_podatke()
    print("Obstoječi podatki:", podatki)

    # Dodajanje novih podatkov
    podatki["nova_kljuc"] = "nova vrednost"

    # Shranjevanje posodobljenih podatkov
    shrani_podatke(podatki)

    izhod()

if __name__ == "__main__":
    main()
```

---

### **5. Zagon programa**
Zaženi `main.py`:
```bash
python main.py
```

---

### **Prednosti modularnega pristopa**
1. **Večja preglednost:**
   - Funkcije so organizirane v logične sklope.
2. **Ponovna uporabnost:**
   - Funkcije v modulih lahko uporabimo v več različnih projektih.
3. **Lažje vzdrževanje:**
   - Spremembe v funkcijah so centralizirane v modulih.

---

