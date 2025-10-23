# Nastavitev messages parametra

Nastavitev `messages` z uporabo **GPT-4 chat modela** temelji na strukturi seznama sporočil, kjer vsako sporočilo vsebuje tri ključne elemente:

1. **`role`** (vloga): Označuje, kdo "govori" v določenem delu pogovora.
2. **`content`** (vsebina): Dejanski tekst, ki ga poda vloga.
3. **`name`** (opcijsko): Ime "subjekta", ki govori. Ta je bolj relevanten pri sistemskih sporočilih ali pri posebnih implementacijah.

---

### **Vloge v pogovoru (`role`)**
1. **`system`**  
   - Uporablja se za nastavitev začetnega konteksta ali navodil za asistenta.  
   - Vsebina določa, kako naj se asistent obnaša, kakšen je njegov ton in namen.  
   - Primeri:  
     - `"Ti si pomočnik za poučevanje tehnike in tehnologije."`  
     - `"Odgovarjaj kratko in jedrnato."`  
     - `"Govori formalno in izobraženo."`

2. **`user`**  
   - To predstavlja vhod uporabnika, torej vprašanja ali zahteve, ki jih poda uporabnik.
   - Vsebina je dinamična, saj se spreminja z vsakim novim vhodom.

3. **`assistant`**  
   - To predstavlja odgovore, ki jih generira GPT.  
   - GPT-4 sam doda to vlogo, ko generira odgovor, vendar jo lahko tudi ročno dodajamo, če gradimo kontekstualne pogovore.

---

### **Kako nastavimo `conversation`**
`conversation` je seznam slovarjev, kjer vsak slovar predstavlja eno sporočilo. Tukaj je primer:

```python
messages = [
    {"role": "system", "content": "Ti si pomočnik za poučevanje tehnike in tehnologije."},
    {"role": "user", "content": "Kaj je to spajkanje?"},
    {"role": "assistant", "content": "Spajkanje je postopek povezovanja dveh kovinskih predmetov z uporabo taljivega materiala, imenovanega spajka."}
]
```

### **Prilagoditev `system` sporočila**
S sistemsko vlogo lahko prilagajamo vedenje asistenta. Nekaj primerov:

1. **Formalni učitelj**  
   ```python
   {"role": "system", "content": "Ti si strogo formalni učitelj tehnike in tehnologije. Odgovarjaj v celih stavkih."}
   ```

2. **Prijazen mentor**  
   ```python
   {"role": "system", "content": "Ti si prijazen mentor, ki pomaga dijakom razumeti osnove tehnike in tehnologije. Spodbujaj jih z motivacijskimi komentarji."}
   ```

3. **Tehnični strokovnjak**  
   ```python
   {"role": "system", "content": "Ti si tehnični strokovnjak za elektroniko in razlagaš procese na poglobljen način."}
   ```

4. **Igra vlog (roleplay)**  
   - Asistent kot tehnična podpora:  
     ```python
     {"role": "system", "content": "Ti si tehnična podpora za uporabo 3D tiskalnikov. Odgovarjaj le z navodili in ne s teorijo."}
     ```
   - Simulacija izpraševalca:  
     ```python
     {"role": "system", "content": "Ti si izpraševalec na izpitu iz tehnike in tehnologije. Postavljaj vprašanja in ocenjuj odgovore."}
     ```

---

### **Prilagoditev odgovora z dodajanjem lastnosti**
GPT-4 omogoča prilagoditve tudi preko drugih parametrov, ki jih nastavimo pri klicu API:

1. **`temperature`**  
   - Vrednost med 0 in 1, določa "kreativnost" odgovorov.
   - **Nizka vrednost (npr. 0.2):** Bolj predvidljivi in konzervativni odgovori.
   - **Visoka vrednost (npr. 0.8):** Bolj ustvarjalni in raznoliki odgovori.

2. **`max_tokens`**  
   - Določa maksimalno število znakov (toknov) v odgovoru.  
   - Primer: `max_tokens=50` vrne kratek odgovor.

3. **`top_p`**  
   - Alternativa `temperature`, nadzoruje "verjetnostno porazdelitev" odgovorov.  
   - Manj pogosto uporabljano.

---

### **Praktični primer: Dinamično prilagajanje pogovora**

```python
# Spreminjanje vedenja asistenta glede na namen
messages = [
    {"role": "system", "content": "Ti si prijazen mentor za tehniko. Odgovarjaj jedrnato in spodbudno."}
]

# Vhod uporabnika
user_input = "Kako deluje elektromotor?"

# Dodamo uporabnikovo vprašanje
messages.append({"role": "user", "content": user_input})

# Simuliran GPT odgovor
assistant_reply = "Elektromotor pretvarja električno energijo v mehansko energijo z uporabo magnetnih polj."

# Dodamo odgovor asistenta v zgodovino
messages.append({"role": "assistant", "content": assistant_reply})

# Prikažemo celoten pogovor
for msg in conversation:
    print(f"{msg['role'].capitalize()}: {msg['content']}")
```

---

### Povzetek:
1. **`system`** določa začetni kontekst in ton pogovora.
2. **`user`** predstavlja vprašanja uporabnika.
3. **`assistant`** vsebuje odgovore, ki jih generira GPT.

S prilagoditvijo `system` sporočila lahko popolnoma oblikuješ obnašanje asistenta glede na potrebe. Če želiš, ti pripravim še dodatne primere za konkretne scenarije!
