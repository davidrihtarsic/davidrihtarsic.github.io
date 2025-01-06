# [ITTD](../../index)
[🏡DOMOV](../../index){: .btn}
[📝VSEBINE](../../Vsebine/index.md){: .btn}
[👨‍🎓INFO](../../info){: .btn}
[💾PRESNEMI](../../Presnemi/index){: .btn}

---

PREDLOGA SEMINARSKE NALOGE
================================================================================

Seminarsko nalogo strukturirajte po modelu znanstvenega članka (IMRAD), pri čemer se osredotočite na **metodologijo, rezultate** in **analizo izboljšav**. Cilj je predstaviti, kako ste zasnovali, izboljšali in testirali AI tutorja, pri čemer naj bo vsebina jedrnata in tehnično natančna.

### **Struktura seminarske naloge**

1. **Naslov in povzetek**
   - **Naslov**: Kratek in jasen, da odraža vsebino dela.
   - **Povzetek**: Največ 200 besed. Na kratko povzemite glavni cilj, metodologijo in ključne ugotovitve.

   *Primer:*

   > V tej seminarski nalogi opisujemo razvoj in izboljšave AI tutorja za podporo učencem pri izdelavi temperaturnega senzorja z izpisom na LCD. Tutor je zasnovan s pomočjo Python knjižnice OpenAI in shranjuje pogovore za nadaljnjo analizo. Vključili smo izboljšave, kot so dodatna navodila in optimizacija interakcije, ki so bile testirane s konkretnimi primeri. Rezultati kažejo, da spremembe izboljšajo razumevanje in učinkovitost učencev ...

2. **Uvod**
   - Predstavite kratek pregled problema in ciljev naloge. Vključite lahko izkušnje, ki ste
    jih pridobili med vajami pri izdelavi temperaturnega senzorja.
   - **Ne izgubljajte časa z obširno teorijo. Pomembnejša je predstavitev vašega dela.**

   *Primer:*

   > Namen seminarske naloge je raziskati, kako lahko AI tutor pomaga pri tehničnem izobraževanju, še posebej pri zasnovi elektronskih vezij. V središču naloge je praktična implementacija in izboljšanje delovanja tutorja ...

3. **Metodologija**
   - Natančno opišite, kako ste izdelali AI tutorja. Vključite:
     - **Tehnične specifikacije** (uporabljena knjižnica, API ključi).
     - **Prikaz kode** s komentarji.
     - Pojasnite, kako ste shranjevali pogovore in jih analizirali.

   *Primer:*
   ```python
   import openai

   openai.api_key = "YOUR_API_KEY"

   def chat_with_tutor(prompt):
       response = openai.ChatCompletion.create(
           model="gpt-4",
           messages=[{"role": "user", "content": prompt}]
       )
       return response["choices"][0]["message"]["content"]

   # Example of storing conversation
   with open("conversation_log.txt", "a") as log:
       log.write("User: How to connect the sensor?\n")
       log.write(f"Tutor: {chat_with_tutor('How to connect the sensor?')}\n")
   ```

4. **Rezultati**
   - Predstavite rezultate testiranja tutorja, vključno z izboljšavami.
   - Uporabite **loge pogovorov** za podporo analizi.
   - Dodajte tabele ali grafe, če je potrebno.

   *Primer:*

    > **Opis izboljšave:**

    > Ena od izboljšav je bila dodajanje dodatnih vprašanj za preverjanje razumevanja navodil pri povezovanju temperaturnega senzorja. Prej je AI tutor podal neposredna navodila, vendar ni preverjal, ali jih je uporabnik razumel. Po izboljšavi AI tutor postavlja vmesna vprašanja, kot so: 

    > - *"Ali razumete, kako deluje vezje s temperaturnim senzorjem?"*
    > - *"Kateri priključek na Arduinu je povezan s signalnim pinom senzorja?"*
    > 
    > Te spremembe so izboljšale razumevanje konceptov in zmanjšale število napačnih povezav med komponentami.
    > 
    > **Tabela 1: Učinkovitost pred in po izboljšavi**
    > 
    > | Funkcionalnost                      | Pred izboljšavo (%) | Po izboljšavi (%) |
    > |-------------------------------------|---------------------|-------------------|
    > | Razumevanje osnovnih konceptov      | 65                  | 90                |
    > | Uspešno povezovanje komponent       | 70                  | 95                |
    > | Število vprašanj za dodatna pojasnila | 15                  | 5                 |
    > 
    > **Pojasnilo:**
    > Po uvedbi dodatnih vprašanj je tutor bolj proaktivno preverjal razumevanje, kar je povzročilo občutno povečanje uspešnosti pri povezovanju komponent in zmanjšanje števila napačnih povezav. Študentje so izpostavili, da so se zaradi vprašanj počutili bolj samozavestne in bolje pripravljene na izvedbo naloge ...
    
---

5. **Diskusija**
   - Pojasnite, kaj rezultati pomenijo in kako ste izboljšali AI tutorja.
   - Predlagajte, kako bi lahko delo še izboljšali v prihodnje.

   *Primer:*

   > Uvedba dodatnih vprašanj, ki preverjajo razumevanje, je pripomogla k boljšemu sledenju navodil. V prihodnje bi lahko vgradili tudi vizualno podporo, kot so diagrami vezij ...

6. **Zaključek**
   - Kratek povzetek ključnih dosežkov in ugotovitev.

7. **Literatura**
   - Navedite uporabljene vire.

---

### **Kriteriji za ocenjevanje**
1. **Tehnična izvedba (40%)**: 
   - Koda mora biti natančno komentirana, brez napak, in omogočati enostavno prilagoditev.
2. **Analiza in izboljšave (30%)**: 
   - Jasno pokažite vpliv sprememb na delovanje tutorja, podkrepite z logi.
3. **Predstavitev in struktura (20%)**: 
   - Naloga mora slediti IMRAD strukturi, biti jedrnata in jasna.
4. **Inovativnost (10%)**: 
   - Upošteva se izvirnost pri izboljšavah AI tutorja.

---
