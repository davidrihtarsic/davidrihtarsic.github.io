OSNOVE PYTHON PROGRAMIRANJA
================================================================================

Ta vaja je namenjena začetnikom, da se seznanijo z osnovami programiranja v Pythonu. Program vključuje več ključnih elementov Pythona: spremenljivke, pogoje, zanke, funkcije, sezname, slovarje in datoteke.

---

## **Vsebina:**
1. **Spremenljivke in formatiran izpis:**
   - Uporaba `input()` in formatiranega niza (`f-string`).

2. **Pogoji:**
   - Preverjanje starosti z `if-else`.

3. **Zanke in seznami:**
   - Ustvarjanje seznama z `for` zanko.
   - Iteracija po seznamu za prikaz podatkov.

4. **Slovarji:**
   - Ustvarjanje slovarja za shranjevanje kompleksnih podatkov.

5. **Funkcije:**
   - Definicija funkcije za preverjanje starosti in njena uporaba.

6. **Delo z datotekami:**
   - Shranjevanje podatkov v JSON format.
   - Nalaganje podatkov iz JSON datoteke.

---

## **Naloge za študente:**
1. Dodajte nov ključ v slovar `uporabnik`, ki shrani vaš najljubši hobi.
2. Spremenite funkcijo `preveri_starost`, da preveri, ali je uporabnik starejši od 21 let.
3. Dodajte možnost za ročno brisanje enega predmeta s seznama najljubših predmetov.

---

## **Celoten program**


```python
"""
Vaja: Osnove programiranja v Pythonu
Ta program vključuje:
1. Delo s spremenljivkami.
2. Uporabo pogojev (if-else).
3. Uporabo zank (for in while).
4. Delo s seznami in slovarji.
5. Pisanje in nalaganje datotek.
6. Funkcije za modularno programiranje.
"""

# 1. SPREMENLJIVKE IN OSNOVNI IZPIS
# Uporabimo spremenljivke za shranjevanje podatkov
ime = input("Vnesite svoje ime: ")  # Vnos uporabnika
starost = int(input("Vnesite svojo starost: "))  # Pretvorba vnosa v celo število

# Izpis pozdravnega sporočila
print(f"Pozdravljeni, {ime}! Starost: {starost} let.")  # Formatiran izpis

# 2. POGOJI (IF-ELSE)
# Preverimo, ali je uporabnik polnoleten
if starost >= 18:
    print("Ste polnoletni.")
else:
    print("Niste še polnoletni.")

# 3. SEZNAMI IN ZANKE
# Ustvarimo seznam najljubših predmetov
predmeti = []  # Prazni seznam
print("\nVnesite svoje tri najljubše predmete:")
for i in range(3):  # Zanka za vnos treh predmetov
    predmet = input(f"Predmet {i+1}: ")
    predmeti.append(predmet)  # Dodajanje predmeta na seznam

# Izpišemo predmete
print("\nVaši najljubši predmeti so:")
for predmet in predmeti:  # Iteracija po seznamu
    print(f"- {predmet}")

# 4. SLOVARJI
# Shranimo podatke uporabnika v slovar
uporabnik = {
    "ime": ime,
    "starost": starost,
    "najljubši_predmeti": predmeti
}

# Izpišemo podatke iz slovarja
print("\nPodatki uporabnika:")
for kljuc, vrednost in uporabnik.items():
    print(f"{kljuc.capitalize()}: {vrednost}")

# 5. FUNKCIJE
# Funkcija za preverjanje, ali je uporabnik starejši od določene starosti
def preveri_starost(starost, prag=18):
    """
    Preveri, ali je starost večja ali enaka določenemu pragu.
    """
    return starost >= prag

# Uporabimo funkcijo za preverjanje polnoletnosti
polnoleten = preveri_starost(uporabnik["starost"])
print(f"\nPolnoletnost: {'Da' if polnoleten else 'Ne'}")

# 6. SHRANJEVANJE IN NALAGANJE DATOTEK
# Shranimo uporabnikove podatke v datoteko
import json  # Modul za delo z JSON

ime_datoteke = "podatki_uporabnika.json"
with open(ime_datoteke, "w", encoding="utf-8") as datoteka:
    json.dump(uporabnik, datoteka, indent=4, ensure_ascii=False)
print(f"\nPodatki so bili shranjeni v datoteko '{ime_datoteke}'.")

# Naložimo podatke iz datoteke in jih prikažemo
with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
    nalozeni_podatki = json.load(datoteka)
print("\nNaloženi podatki:")
for kljuc, vrednost in nalozeni_podatki.items():
    print(f"{kljuc.capitalize()}: {vrednost}")
```

---

