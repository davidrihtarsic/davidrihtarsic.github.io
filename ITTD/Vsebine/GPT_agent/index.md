# [ITTD](../../index)
[🏡DOMOV](../../index){: .btn}
[📝VSEBINE](../../Vsebine/index.md){: .btn}
[👨‍🎓INFO](../../info){: .btn}
[💾PRESNEMI](../../Presnemi/index){: .btn}

---
## Etične smernice uporabe GUI

- [Etične smernice uporabe GUI](./PeF_Smernice_za_GUI.pdf)

## Izdelava GPT agenta

- [Predloga seminarske naloge](./predloga_seminarske_naloge.md)

### **Prvi termin: Uvod in osnove**
1. **Uvod (30 min)**  
   - Namen in uporaba GPT asistenta pri poučevanju.  
   - Primeri, kaj lahko GPT asistent počne (pomoč pri projektih, iskanje napak, podajanje povratnih informacij).  

2. **Osnove programiranja z GPT (90 min)** 
    - Uvod v Python in razumevanje osnovne kode.  
        - [Kratka vaja z osnovami](./100_osnove_python_programiranja.md)
    - Pojasnilo API-ja: kako komunicirati z GPT (ključ, osnovni klici API-ja).  
        - [Komunikacija z OpenAI modeli](./200_OpenAI_API_modeli.md)
    - Skupaj napišemo enostavnega GPT asistenta, ki odgovarja na vprašanja in se pogovarja z uporabnikom.
        - [Primer GPT agenta in uporaba openai](./300_Terminal_GPT_agent_v1.md)
>
>    - Nekaj več o `Python` seznamih in slovarjih
>        - [Primeri uporabe seznamov in slovarjev](./310_python_seznami_in_slovarji.md)
>    - [Dodatne možnosti nastavitve message](./320_message_role.md)
    - Asistenta dopolnimo z možnostjo beleženja zgodovine pogovora. Tako lahko Asistent ohranja kontekst pogovora.
        - [Beleženje pogovora, conversation_id](./350_Terminal_GPT_agent_v2.md)
        - [Shranjevanje pogovora v json datoteko](./600_shranjevanje_pogovora.md)

3. **Ustvarjanje gradiva za vektorsko skladišče**

Za potrebe učnega procesa ne moremo mimo [UČNEGA NAČRTA za TIT](https://www.gov.si/assets/ministrstva/MVI/Dokumenti/Osnovna-sola/Ucni-nacrti/Ucni-nacrti/2025/UN_OS/Didakticna_priporocila_k_ucnemu_nacrtu_tehnika_in_tehnologija_2025.pdf), ki ga predpiše ministerstvo. To gradivo ni najbolj primerno za vključitev v vektorsko skladišče ai asistenta. To lahko storimo tako:

- [Primer povezave AI asistenta z vektorskim skladiščem.](./712_VectorStore_ai_agent_call.md)

Pogosto moramo gradiva nekoliko preurediti, da dobimo kar najboljše rezultate. Pri ustvarjanju gradiva za [vektorsko skladišče](./710_Vectore_store.md) je dobro upoštevati nekaj smernic:

- Namen in obseg gradiva
- Zbiranje in priprava gradiva - primer [Energetika](./711_Primer_gradiva_Energetika_TIT.md)
- Struktura in metapodatki (nekaj več o [markdown](https://www.markdownguide.org/basic-syntax/) načinu pisanja ), preskusite se lahko tudi v [spletnih orodjih mardown](https://markdownlivepreview.com/)
- Razdelitev gradiva na enote
- Uporaba gradiva za iskanje in odzive v AI
- Kakovost, preverjanje in vzdrževanje
- Varnost, avtorske pravice in etika
- Začetek implementacije in priporočen postopek (kopičenje virov, seznam metapodatkov, izdelava prvih enot)

4. **Prilagajanje asistenta učnim potrebam**

    - pogovor z asistentom razstavite na ključne elemente učnega procesa npr.:
        - navodila_za_asistenta,
        - naloga_projekta,
        - učni cilji,
        - razumevanje_ucenca,
        - kontekst_pogovora ...
        - vse te elemente dodajajte v pogovor, da boste dobili najboljši odgovor.

    - [Jasna_navodila_GPT_asistenta](./700_Jasna_navodila_GPT_asistenta.md)


### **Drugi termin: Prilagoditev in funkcionalnosti**

**Načrtovanje GPT tutorja**  

- Študentje načrtujejo svojega GPT tutorja, ki bo vodil učenca pri izdelavi zamišljenega projekta.
- Študent naj si zamisli preprosto projektno nalogo in 
- z ozirom nanjo načrtuje GPT tutorja.

- Nato naj posredujejo svojega GPT tutorja svojemu kolegu, le-ta pa naj ga preskusi,
- kako dobro GPT tutor deluje. Pri tem si lahko pomagate s kriteriji kot so:
    - Ali asistent zagotavlja pravilne in jasne informacije?
    - Stopnja pravilnosti odgovorov (npr. tehnične ali vsebinske napake).
    - Jasnost in strukturiranost podanih razlag.
    - Skladnost odgovorov z učnimi cilji.
    - Primerjava odgovorov asistenta z učnimi gradivi.
    - Ali asistent prilagaja učne poti glede na odzive učenca?
    - Ali preverja razumevanje učenca in ustrezno prilagodi naslednje korake.
    - Ali uspešno identificira in odpravi napačna prepričanja (misconceptions).
    - Sposobnost generiranja vprašanj, ki spodbujajo kritično razmišljanje.
    - ...
---

1. **Uporabniški vmesnik**

    - Ustvarjanje Python strežnika s Flask knjižnico
        - [Flask knjižnica](./800_Flask_strežnik.md)

2. **Načrtovanje (45 min)**  
   - Vsak študent določi namen svojega asistenta (ciljno rutinsko nalogo).  
   - Razprava o možnih funkcionalnostih.

3. **Dodajanje funkcionalnosti (90 min)**  
   - Razlaga in implementacija večstopenjskih odgovorov (npr. preverjanje predznanja).  
   - Pomoč pri projektih: kako GPT vodi skozi korake.  
   - Naloga: vsak študent prilagodi osnovno kodo svojemu načrtu.

4. **Kratka predstavitev napredka (15 min)**  

---

### **Tretji termin: Testiranje in izboljšave**

**TESTNO OKOLJE**  

1. Prilagodite `AI_AGENT_INSTRUCTIONS` tako, da bo jasno, da naj ai asistent kar najblje sledi vsebini v vektorskem skladišču, na primer:

```Python
AI_AGENT_INSTRUCTIONS = """
Deluješ kot **AI učiteljev asistent** za predmet *Tehnika in tehnologija*.

Tvoja glavna naloga je pomagati učitelju pri **pripravi na učno uro**: 
predlagaj učne cilje, aktivnosti, potek ure, refleksijo in potrebne materiale,
vendar vedno ohrani strokovnost, skladnost z učnimi načrti in jasnost zapisa.

---

## Temeljna pravila: 
1. **Odgovarjaj v slovenščini.**

2. **Piši v Markdown formatu**, strukturirano z razdelki:
   - `## {NASLOV}`
      - {sestavek s tvojim odgovorom}
   - `## Viri:`
      - [chunk_id]: {prvih nekaj besed iz odseka besedila}

3. **Ne izmišljuj si informacij.**
   - Če v priloženih virih ni dovolj podatkov, napiši:  
     > "Ni podatka v gradivu."
   - Če predlagaš nekaj, česar ni v virih, **označi to z opombo**:  
     > "Dopolnitev AI asistenta:"

4. **Vse izjave morajo izhajati iz učnih vsebin ali splošno veljavnih didaktičnih načel.**

5. **Tone naj bo strokoven, a prijazen in podporen.**

6. Glavni cilj je **pomagati učitelju ustvariti uporabno, premišljeno pripravo.**

"""
```

2. Pripravite testne vektorje: to so eksperimentalna vprašanja. Taka, ki jih pričakujete, da bi jih lahko učitelj zastavit Ai Asistentu v procesu priprave na učno uro. Ta del je bistven del testiranja, zato naj bo vprašanj več (10 - 15), osredotočena na bistvene sestavne elemente učne ure. Ta vprašanja naj bodo enaka skozi celotno fazo testiranja tako, da jih boste lahko vrednotili (verjetno kvalitativno analizirali) med spremembami. Na primer:
        - Naštej učne cilje te enote.
        - Kateri materiali in IKT so potrebni?
        - ...
3. Pripravite kontrolne vektroje: to so vprašanja, s katerimi testirate robustnost sistema. Teh vprašanj naj bo bistveno manj (3-5). Na primer:
        - Negativni odgovor: zastavite vprašanje, za katerega veste, da odgovora ni v vektorskem skladišču in bi morali dobiti odgovor : "Ni podatka v gradivu."
        - Preoblikujte dve od eksperimentalnih vprašanj in primerjajte podobnost odgovora.
        - Zastavite neprimerno vprašanje in ocenite primernost odgovora.
    4. Pripravite metriko analize -  kriterij ocenjevanja odgovorov. Kriteriji naj vsebujejo na primer:
        - vsebinsko točnost (3t),
        - utemeljitev (3t),
        - jedrnatost (2t),
        - upoštevanje Markdown strukture (2t)

**TESTIRANJE**:

1. V vsaki fazi testiranja začnite z novim pogovorom tako, da sistem ne bo razpolagala s predhodnimi pogovori.
2. Preverite odzive vseh testnih in kontrolnih vektorjev.

**ANALIZA**:

1. Analizirajte odgovore in pripravite smernice za popravek sistema. Predvsem se osredotočite na:
   - Popravek gradiva vektorskega skladišča,
   - popravek spremenljivke v AI_AGENT_INSTRUCTIONS, če ugotovite, da jim asistent ne sledi dovolj dosledno,
   - popravek nastavitev funkcije `client.responses.create(...`

4. **EKSPERIMENTIRANJE**:

1. Popravki naj bodo postopni - spremenite le eno spremenljivko naenkrat in ponovite točko **2. TESTIRANJE**. Najverjetnejši popravki so:
  - Popravek gradiva vektorskega skladišča ustrezno dopolnite z dodatnimi navodili ali vsebino,  ter ga ponovno naložite v vektorsko skladišče.
  - Popravek navodil za ai asistenta in
  - popravek nastavitev funkcije `client.responses.create(...` za komunikacijo z openai: 

```Python
response = client.responses.create(
    model="gpt-5-nano",
    conversation=CONVERSATION_ID,
    input=input_messages,
    temperature=1.0,          # Nižja vrednost (npr. 0.0–0.3) pomeni bolj dosledne in ponovljive odgovore.
    top_p=1.0,                # Če je top_p=0.9, model izbira samo med 90 % najverjetnejšimi naslednjimi zlogi.
    max_output_tokens=1024,   # Omeji največje število generiranih zlogov v izhodu.
    tools=[
       {
           "type": "file_search",
           "vector_store_ids": ["vs_68fa2c8d7eb08191bd360f955ecd1de5"],
       }
    ],
)
```

**REZULTATI**:
   - Pripravite povzetek rezultatov.

---

### **Četrti termin: Predstavitev in evalvacija**
1. **Predstavitev asistenta (90 min)**  
   - Vsak študent predstavi svojega asistenta in njegov namen.  

2. **Evalvacija (45 min)**  
   - Sošolci in učitelj ocenijo asistente glede na funkcionalnost, uporabnost in inovativnost.  
   - Razprava o možnih izboljšavah in izzivih.  

---
