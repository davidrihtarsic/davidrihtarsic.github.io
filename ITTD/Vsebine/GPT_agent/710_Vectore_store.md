# USTVARJANJE GRADIVA - VECTOR STORE

Kratek okvir napotkov za gradivo v vektorno skladišče (vector store)

Namen tega navodila je podati orientacijo, kako ustvariti kakovostno in učinkovito gradivo, ki ga uvrstimo v vektorskem skladišču za podporo učnemu procesu z umetno inteligenco. Gradivo naj omogoča zanesljivo iskanje, ponujanje natančnih odgovorov in enostavno nadgradnjo pri prihodnjih posodobitvah. Upoštevajmo načela jasnosti, doslednosti in spoštovanja avtorskih pravic.

1. Namen in obseg gradiva
- Določi jasen cilj zapisa: katere teme obravnava, za katere predmetne sklope in katere učne cilje podpira.
- Zapiši, katere vrste vsebin vključuješ (razlage, primeri, vaje, vprašanja, ilustracije) ter kakšne so zahteve glede formata in dolžine posameznih delov.

2. Zbiranje in priprava gradiva

- Izberi zanesljive in dovoljene vire (avtorstvo, licence, avtorske pravice). Preveri, ali lahko vsebino brez omejitev vključuješ v učni material.
- Opravi standardizacijo jezika: poenoti terminologijo, enote mer, zapis pogojev in vzorce, da se izognemo več jasnim razlikam.
- Po potrebi odstrani osebne podatke ali občutljive informacije ter poskrbi za anonimizacijo, če je to potrebno.

Praktično dopolnilo: priprava gradiva v Markdown obliki:  
- Priprava v Markdown obliki omogoča enostavno pretvorbo v različne formate (učbenik, spletni vodiči, PDF preko Pandoca ali LaTeXa) ter večjo preglednost in razčlenljivost vsebin.
- Omogoča vključitev metapodatkov, povezav in vizualnih elementov ter hiter poskus iskanja in filtriranja znotraj učnega materiala.
- Prispeva k dosledni uporabi terminologije in enot mer skozi celotno zbirko gradiva ter olajša verzioniranje v verzioniranih repozitorijih.

3. Struktura in metapodatki
- Za vsak del gradiva določi jasen naslov, kratek opis, ključna vprašanja in ciljne izide.
- V metapodatke vključuj: predmet, raven študija, predznanje, ciljno skupino, vir materiala, datum zadnje posodobitve, licenco.
- Uporabi znamenje enotnosti: isti zapis za datume, enote (mm, cm, stopnje), enak način označevanja ilustracij in tabel.

```markdown
---
id: gradivo_02
naslov: Zbiranje in priprava gradiva
predmet: Tehnika in tehnologija
cilji_učenja: [razumevanje pravil zbiranja gradiva, standardizacija terminologije]
---

# Zbiranje in priprava gradiva

Ta del obravnava, kako izbrati zanesljive vire, zagotoviti skladnost z avtorskimi pravicami ter standardizirati jezik in zapis mer. Namen je omogočiti enostavno vključevanje gradiva v učni proces in njegovo ponovljivo uporabo v vektorskem skladišču.

Kratek opis: izberi vire z jasnimi licencami, standardiziraj terminologijo in enote ter poskrbi za anonimizacijo osebnih podatkov, kjer je potrebno.
```

4. Tehnike razdeljevanja (chunking)
- Razdeli daljše besedilo na logične enote (odstavki ali podpoglavja) s poudarkom na semantiki: izrabljaj prehode med temi, ne spreminjaj pomena pri združevanju.
- Priporočljivo velikostno okvirno določiti: vsak “chunk” naj pokriva en koncept ali operacijo (npr. eno merjenje, ena tehnika, en primer uporabe).
- Vsakemu chunku dodaj kratek povzetek in povezavo na naslednji del, da ohrani kontinuiteto branja.

5. Predstavitev ključnih konceptov (embeddings in iskanje)
- Določi, katere dele gradiva bodo vdelani kot besedilne vsebine in katere bodo spremljani z dodatnimi metapodatki (npr. koraki postopka, varnostna opozorila).
- Uporabi vsebinske oznake in oznake znanj (npr. osnovno/napredno, prerequisites), da olajšaš razvrščanje in iskanje v skladišču.

6. Kakovost in preverjanje
- Uredi dva ali več primerkov iste teme, da lahko primerjaš natančnost in doslednost; izvedi ročni pregled ali vključi učitelja-mentorja.
- Določi merila za ocenjevanje natančnosti in relevantnost (npr. pravilnost terminologije, doslednost meritev, jasnost navodil).
- Redno preverjaj in posodabljaj gradivo glede na nove učne potrebe ali spremembe v programu.

7. Varnost, avtorske pravice in etika
- Poskrbi za spoštovanje avtorskih pravic in licenc: navedbe virov, licensing zgodovino in pogoje ponovne uporabe.
- Izogibaj se vključevanju občutljivih ali zasebnih podatkov učencev ali drugih oseb.
- Zagotoviti moraš, da gradivo spodbuja etično uporabo umetne inteligence in varno, odgovorno poučevanje.

8. Uporaba in integracija z AI agentom
- Oblikuj gradivo sosednje elemente, ki olajšajo forenzično iskanje in odzive AI agenta: jasni pojmi, standardni izrazi, primerni primeri.
- Pripravi priročne vzorčne lupine (prompt templates) za iskanje po skladišču, povzetek ali razlago, ki lahko AI agent uporabi brez dodatne ročne prilagoditve.
- Razmisli o verzioniranju: vsak posodobljen del naj prejme novo različico ali oznako verzije in jasno sledljivost virov.

9. Zgledna struktura zapisov (predlog)
- Vsak zapis lahko vsebuje: id, naslov, predmet, cilj učenja, vir/avtor, licenca, ključna vprašanja, glavni povzetek, povezave na dodatno gradivo, metapodatke o temi in primeri uporabe.
- Primer kratke zapisne šablone (v obliki YAML ali JSON v kode blok): 

```
id: module_vektor_01
naslov: Uvod v ustvarjanje gradiva za vect store
predmet: Tehnika in tehnologija
cilji_učenja: [razumevanje pojma vektornega skladišča, sposobnost priprave metapodatkov]
vir: "učbenik_tehnika_2025"
chunks:
  - id: c1
    naslov: Uvod v gradivo za vect store
    dolzina: 350-450 besed
    ključne_besede: [embeddings, chunking, metapodatki]
```

10. Praktičen začetek implementacije
- Začni z zbiranjem ključnih tem in izvorov, ki jih želiš vključiti v vektor store.
- Oblikuj kratek, jasen seznam metapodatkov za vsak del gradiva.
- Zgradi nekaj začetnih chunkov in poveži z uvodnimi navodili ter z vnaprej pripravljenimi prompti za AI agenta.

