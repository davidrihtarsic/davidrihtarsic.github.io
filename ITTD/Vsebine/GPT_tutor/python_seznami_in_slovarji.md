# Uporaba seznamov in slovarjev v Pythonu

Python ponuja dve osnovni strukturi podatkov za shranjevanje in organizacijo podatkov: **seznami** (lists) in **slovarji** (dictionaries). Obe sta ključni za učinkovito delo s podatki.

---

### **1. Seznami (lists)**

- **Definicija**: Seznami so zbirke urejenih podatkov, ki jih lahko indeksiramo.
- **Lastnosti**:
  - Elemente lahko dodajamo, odstranjujemo ali spreminjamo.
  - Podatki v seznamu so indeksirani z ničelnim indeksom (prvi element ima indeks `0`).
  - Lahko vsebujejo različne tipe podatkov (npr. števila, nizi, druge sezname).

Seznami so zbirke podatkov, ki so urejene in omogočajo shranjevanje več elementov. Vsak element ima indeks, ki se začne pri 0.

#### **Ustvarjanje seznama:**
```python
# Primer praznega seznama
moj_seznam = []

# Primer seznama z elementi
stevila = [1, 2, 3, 4, 5]
besede = ["jabolko", "banana", "češnja"]
```

#### **Dostop do elementov:**
```python
# Dostop do prvega elementa
print(stevila[0])  # Izhod: 1

# Dostop do zadnjega elementa
print(stevila[-1])  # Izhod: 5
```

#### **Dodajanje elementov:**
```python
stevila.append(6)  # Doda 6 na konec seznama
print(stevila)  # Izhod: [1, 2, 3, 4, 5, 6]
```

#### **Odstranjevanje elementov:**
```python
stevila.remove(3)  # Odstrani element 3
print(stevila)  # Izhod: [1, 2, 4, 5, 6]
```

#### **Iteracija (zanka):**
```python
for stevilo in stevila:
    print(stevilo)
```

---
#### Primeri uporabe:
```python
# Ustvarjanje seznama
moj_seznam = [1, 2, 3, "tehnika", True]

# Dostop do elementov
print(moj_seznam[0])  # Prvi element: 1

# Dodajanje elementov
moj_seznam.append("novo")
print(moj_seznam)  # [1, 2, 3, 'tehnika', True, 'novo']

# Odstranjevanje elementov
moj_seznam.remove(3)
print(moj_seznam)  # [1, 2, 'tehnika', True, 'novo']

# Spreminjanje elementov
moj_seznam[1] = "spremenjeno"
print(moj_seznam)  # [1, 'spremenjeno', 'tehnika', True, 'novo']
```

---

### **2. Slovarji (dictionaries)**

- **Definicija**: Slovarji so zbirke neurejenih podatkov v obliki parov **ključ-vrednost**.
- **Lastnosti**:
  - Namesto indeksov uporabljamo ključe za dostop do vrednosti.
  - Ključi so unikatni, vrednosti pa se lahko ponavljajo.
  - Uporabni za shranjevanje podatkov, kjer ima vsak podatek identifikator.

Slovarji so zbirke podatkov, ki shranjujejo pare **ključ: vrednost**. Ključi so unikatni, vrednosti pa se lahko ponavljajo.

#### **Ustvarjanje slovarja:**
```python
# Primer praznega slovarja
moj_slovar = {}

# Slovar s podatki
student = {
    "ime": "Ana",
    "starost": 21,
    "predmeti": ["Matematika", "Fizika"]
}
```

#### **Dostop do vrednosti:**
```python
# Dostop do vrednosti po ključu
print(student["ime"])  # Izhod: Ana
print(student["predmeti"])  # Izhod: ['Matematika', 'Fizika']
```

#### **Dodajanje ali spreminjanje vrednosti:**
```python
student["letnik"] = 3  # Dodaj nov par ključ: vrednost
student["starost"] = 22  # Posodobi obstoječo vrednost
print(student)
```

#### **Odstranjevanje parov:**
```python
del student["letnik"]  # Odstrani par s ključem 'letnik'
print(student)
```

#### **Iteracija skozi slovar:**
```python
for kljuc, vrednost v student.items():
    print(f"{kljuc}: {vrednost}")
```

---
#### Primeri uporabe:
```python
# Ustvarjanje slovarja
moj_slovar = {"ime": "Tehnika", "število_ur": 45, "obvezno": True}

# Dostop do vrednosti
print(moj_slovar["ime"])  # 'Tehnika'

# Dodajanje parov ključ-vrednost
moj_slovar["opis"] = "Predmet za učitelje tehnike"
print(moj_slovar)

# Spreminjanje vrednosti
moj_slovar["število_ur"] = 50
print(moj_slovar)  # {'ime': 'Tehnika', 'število_ur': 50, 'obvezno': True, 'opis': 'Predmet za učitelje tehnike'}

# Odstranjevanje parov
del moj_slovar["obvezno"]
print(moj_slovar)  # {'ime': 'Tehnika', 'število_ur': 50, 'opis': 'Predmet za učitelje tehnike'}
```

---

### **Primerjava**

| Lastnost               | Seznami          | Slovarji             |
|------------------------|------------------|----------------------|
| **Urejeni**            | Da               | Ne                   |
| **Dostop do podatkov** | Po indeksu       | Po ključu            |
| **Shranjuje**          | Poljubne podatke | Ključ-vrednost pare  |
| **Primer**             | `[1, 2, 3]`      | `{"ime": "Tehnika"}` |

---

### **3. Kombinacija seznamov in slovarjev**
Sezname in slovarje lahko kombiniramo za shranjevanje bolj kompleksnih podatkovnih struktur.

#### **Primer: Seznam slovarjev**
```python
# Seznam študentov
studenti = [
    {"ime": "Ana", "starost": 21},
    {"ime": "Marko", "starost": 23},
    {"ime": "Lara", "starost": 20}
]

# Dostop do imena prvega študenta
print(studenti[0]["ime"])  # Izhod: Ana
```

#### **Primer: Slovar s seznami**
```python
# Slovar s podatki o predmetih in ocenah
predmeti = {
    "Matematika": [5, 4, 3],
    "Fizika": [4, 4, 5]
}

# Povprečna ocena pri Matematiki
print(sum(predmeti["Matematika"]) / len(predmeti["Matematika"]))  # Izhod: 4.0
```

---

### **Zakaj so pomembni za `conversation`?**
1. **Seznam** hrani celotno zgodovino pogovora (vsako sporočilo kot ločen element).  
2. **Slovar** predstavlja posamezno sporočilo z natančno opredeljenimi polji (`role`, `content`).  

#### **Primer: Pogovor z GPT v Pythonu**
```python
conversation = [
    {"role": "system", "content": "Ti si pomočnik za poučevanje tehnike."},
    {"role": "user", "content": "Kaj je električni tok?"},
    {"role": "assistant", "content": "Električni tok je tok električnih nabojev skozi prevodnik."}
]

# Dodajanje novega vprašanja
conversation.append({"role": "user", "content": "Kaj je napetost?"})

# GPT-jev odgovor (simuliran)
conversation.append({"role": "assistant", "content": "Napetost je razlika električnega potenciala med dvema točkama."})

# Izpis celotnega pogovora
for msg in conversation:
    print(f"{msg['role'].capitalize()}: {msg['content']}")
```

---

### **Naloge za študente**
1. Ustvarite seznam svojih najljubših predmetov in dodajte nov predmet.
2. Ustvarite slovar, ki opisuje študenta (ime, starost, predmet) in dodajte novo lastnost.
3. Kombinirajte sezname in slovarje za simulacijo pogovora z GPT, podobno kot zgoraj.

