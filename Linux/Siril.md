# Siril

Program za obdelavo slik v astronomiji... nekaj namenov uporabe:

- iz več fotografij naredi eno
- izloči najzarličnejše motnje (ISO šum, dead pixli, migetanje atmosfere...)

# Osnove

Direktorji s fotografijami uredimo v 4 pod-direktorije:

- biases
- darks
- flats
- lights

## biases

- detekcija šumov zaradi elektronike
- nastavimo tisto ISO vrednost s katero bomo posneli fotografijo = ojačanje
- posnamemo "črno" fotografijo (s pokrovčkom na objektivu)
- in s čim krajšim časom cca 1/4000 s
- posnamemo cca 10x fotografij 

## darks

- detekcija šuma na samem senzorju
- fotografije posnamemo z enakim časom kot običajne fotografije cca 10 - 30 s
- in tudi enak ISO
- MORA pa biti "črna" fotografija (s pokrovčkom na  objektivu)
- cca 10x fotografij

## flat

- teleskopi / objektivi lahko neenakomerno razpršijo svetlobo
- fotografiramo enakomerno osvetljen predmet
- ISO / čas osv. / zas. št. nastavimo tako, da je fotografija osvetljena na 50%
- cca 10x

## lights

- dejanske fotografije 
- pomembna je nastavitev časa, da zvezde ne puščajo sledi zaradi vrtenja zemlje
- na palec lahko izračunamo tako, da uporabimo  `pravilo 500` = 500/f
- naprimer f=30mm -> 500/30 = 16 ; pomeni, da moramo fotografirati s časom t manjšim od 16s
- moje nastavitve:
    - t = 2s
    - f = 75mm
    - ISO = 400

# Uporaba

1. slikaš 10x s pravim ISO, in 1/4000s
2. slikaš 10x s pravim ISO in t
3. slikaš enakomerno osvetljen predmet (bela tabla)
4. slikaš n-krat nek objekt (zvezde, andromedo, herkules)

5. fotke razporediš v dirrektorije: biases, darks, flats in lights

6. če želiš sledenje se poigraš z `Redistration`
7. nato slike sestaviš s `Stack`

8. `Linear` view spremenimo na `AutoStreach` da bolje vidiš kakšni so pravzaprav podatki v fotki
9. `Color calibration` in nastaviš povprečen background in foreground
10. če je kak gradient v barvi na sliki ga lahko portimaš z `Background Extraction...`
11. `Remove Green Noise` da odstraniš zelenkasto obarvan odtenek
12. Z `Asinh Transformation` nastavimo kako vidne naj bodo svetli deli in kako temni naj bodo temnejši deli fotografije
13. Fotko nekoliko osvetljimo z `Histogram Transformation`
14. In nazadnje še poudarimo barve z orodjem `Color Saturation`

# NAvodila za astro-fotografijo

1. potrebuješ (dark sky)[https://www.lightpollutionmap.info/]
2. izbira ISO (LX100II = 800)
    Paziti moramo na razmerje mes šumom in dinamičnim razponom. Če 
    povečamo ISO, bomo imeli večjo občutljivost a tudi manjši dinamični razpon.
    Na strani [PhotonsToPhotos](https://www.photonstophotos.net/) najdemo povezavo
    [Input-referred Read Noise Chart](https://www.photonstophotos.net/Charts/RN_e.htm) in poiščemo naš fotoaparat
    Izberemo prvega, kjer se krivulja zravna naprimer za Panasonic_LX100 izberemo ISO 800
3. izbira časa za panasonic LX100II ne več kot 3s
    


