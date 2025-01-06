# [ITTD](../../index)
[🏡DOMOV](../../index){: .btn}
[📝VSEBINE](../../Vsebine/index.md){: .btn}
[👨‍🎓INFO](../../info){: .btn}
[💾PRESNEMI](../../Presnemi/index){: .btn}

---

## Izdelava GPT agenta

- [Predloga seminarske naloge](./predloga_seminarske_naloge.md)

### **Prvi termin: Uvod in osnove**
1. **Uvod (30 min)**  
   - Namen in uporaba GPT asistenta pri poučevanju.  
   - Primeri, kaj lahko GPT asistent počne (pomoč pri projektih, iskanje napak, podajanje povratnih informacij).  

2. **Osnove programiranja z GPT (90 min)** 
    - Uvod v Python in razumevanje osnovne kode.  
        - [Kratka vaja z osnovami](./osnove_python_programiranja.md)
    - Pojasnilo API-ja: kako komunicirati z GPT (ključ, osnovni klici API-ja).  
        - [Text-davinci-003 vs gpt-4](./OpenAI_API_modeli.md)
    - Skupaj napišemo enostavnega GPT asistenta, ki odgovarja na vprašanja.
        - [Primer GPT agenta in uporaba openai](./Terminal_GPT_agent_v1.md)
    - Nekaj več o `Python` seznamih in slovarjih
        - [Primeri uporabe seznamov in slovarjev](./python_seznami_in_slovarji.md)
    - [Dodatne možnosti nastavitve message](./message_role.md)
    - Agenta dopolnimo z možnostjo dopisovanja z GPT asistentom...
        - [Pošiljanje zgodovine, pogovor, naloga as.](./Terminal_GPT_agent_v2.md)
        - [Izboljšajte berljivost programske kode](./Terminal_GPT_naloga.md)
        - [... ali celo preuredite strukturo programa](./Berljivost_programske_kode.md)
        - [shranjevanje pogovora](./shranjevanje_pogovora.md)

3. **Prilagajanje asistenta učnim potrebam**

    - pogovor z asistentom razstavite na ključne elemente učnega procesa npr.:
        - navodila_za_asistenta,
        - naloga_projekta,
        - učni cilji,
        - razumevanje_ucenca,
        - kontekst_pogovora ...

        - vse te elemente dodajajte v pogovor, da boste bobili najboljši odgovor.

    - [Jasna_navodila_GPT_asistenta](./Jasna_navodila_GPT_asistenta.md)

4. **Načrtovanje GPT tutorja**  
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

### **Drugi termin: Prilagoditev in funkcionalnosti**
1. **Uporabniški vmesnik**

    - Ustvarjanje Python strežnika s Flask knjižnico
        - [Flask knjižnica](./Flask_strežnik.md)

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
1. **Testiranje funkcionalnosti (45 min)**  
   - Študentje med seboj testirajo asistente in zbirajo povratne informacije.  

2. **Napredne prilagoditve (90 min)**  
   - Uvedba prilagoditev na podlagi povratnih informacij.  
   - Razlaga dodatnih možnosti (omejevanje odgovora, posebne fraze).  

3. **Priprava za predstavitev (15 min)**  

---

### **Četrti termin: Predstavitev in evalvacija**
1. **Predstavitev asistenta (90 min)**  
   - Vsak študent predstavi svojega asistenta in njegov namen.  

2. **Evalvacija (45 min)**  
   - Sošolci in učitelj ocenijo asistente glede na funkcionalnost, uporabnost in inovativnost.  
   - Razprava o možnih izboljšavah in izzivih.  

---
