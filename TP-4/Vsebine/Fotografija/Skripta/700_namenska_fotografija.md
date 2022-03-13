# NAMENSKA FOTOGRAFIJA

## PORTRET


## NOČNA ASTRO-FOTOGRAFIJA

### Nastavitve

#### primernost opazovanja

- na spletni strani:
    - [light pollution](www.lightpollutionmap.info) - kako svetlo je nebo zaradi luči (čim manj tem bolje)
    - [full moon dates](https://clearoutside.com) - kakšni bodo pogoji za opazovanje (luna, vreme)
    - [heavens above](https://www.heavens-above.com/) - neverjetno velika baza podatkov o vidnosti satelitov

#### nastavitev fotoaparata
- F = naj bo najbolj odprta F2.8 zato, da dobimo čim več svetlobe
- 2s delay = da se malce umerijo tresljaji
- RAW = da imamo podatek za vsak pixel posebej (ne JPG ker je že skompresirano)
- auto rotate = OFF, če imamo tracker se lahko orientacija fotografije spremeni
- noise reduction = OFF to bomo naredili v programu
- ISO = načeloma z ISO povečamo ojačanje... zato povečamo tudi šum. Vendar vedno pa temu ni tako (novi fotoaparati).
  Vendar ko povečamo ISO, izgubimo dinamični razpon v temnih delih slike. Zato tale [vir]() predlaga, da raje fotografiramo z ISO 200 in s tem obdržimo nekoliko večji dinamični razpon temnejših delov fotografije.
  Vendat [naslednji vir](https://www.youtube.com/watch?v=mYucAuUrdTs) predlaga nastavitev ISO na višje vrednosti, ker imamo tako manjši input-referred read noise - povzeto po [Photons to Photos](https://www.photonstophotos.net/index.htm).
- t = če imamo trcker ni težav - lahko tudi 2 min 

#### poravnanje s severnico
- najprej zbalansiramo fotoaparat in pritrdilno ploščo
- odstranimo ploščo in začnemo s poravnoamo
- na oko ocenimo poravnavo s severnico
- nastavimo zemljepisno širino 46.5°
- z vijaki točno nastavimo smer severnice
- za bolj točno nastavitev lahko uporabimo app. PolarFinder Pro (Android) saj je severnica 0.5° odmaknjena od severa

#### ostrenje
- fotoaparat nastavimo na manual focus 
- v povečanem oknu opazujemo zvezde in jih skušamo narediti čim manjše.
- ko imamo zadovoljivo izostreno, se navadno pojavi več zvezd

- nastavitev ostrine z `Bathinovo masko`:
    - na objektiv dodamo bathinovo masko in
    - nastavimo ostrino nastavimo tako, da se žarki sekajo točno v enem presečišču...
    - če slika ni ostra, nastane razlika med presečiščem od X-žarkov in I-žarkov

![Primer ostrenja z Bathinovim filtrom.](https://upload.wikimedia.org/wikipedia/commons/9/99/Bahtinov_mask_example.jpg){#fig:bathinov_filter}

#### čas osvetljevanja
- pri nastavitvah časa osvetljevanja smo najverjetneje omejeni s kvaliteto naše opreme = ali tracker lepo sledi vrtenju zemlje
- s traskerjem in objektivom f=200mm in če smo nekoliko bolj previdni lahko dobimo dobre fotografije že pri 30s.

- nastavitev časa lahko ugotovimo preko `histograma`:
    - na zaslon dodamo `histogram`
    - in čas nastavimo tako, da imamo krivuljo nekoliko ločeno od levega roba 1/4 od roba
        - tako zagotovimo, da smo podatke ločili od `ground noise flore`-a
        - lahko `histogram` pogledamo za vsako barvo `RGB` tako da vemo, da so vse tri barve ločene od robu

- če nimamo trackerja 
    - `MFN rule` lahko najdete na tej [tej strani](https://sahavre.fr/wp/regle-npf-rule/) in vpišete podatke npr.: 4/3", 4736px, 3.64um, 75mm, ... in dobimo, da lahko slikamo 3.1s, da se ne bodo videlo premikov zvezd zaradi rotacije zemlje
    dsegljivo tudi na PhotoPill app (android)


#### število posnetkov

Število vseh posnetkov mora biti tako, da se čas vseh fotk sešteje v cca 30 min... 
to pomeni, pri času 3s potrebujemo 600 posnetkov... več je bolje... vsaj 30 fotk.

#### kalibracija

Posnamemo kalibracijske posnetke...:

- `darkens` ob enakem času in enakih ISO ter enaki temperaturi, nastavitveh posnamemo nekaj fotk (dobimo podatke o šumu zaradi temperature, ojačanja...)
- `baiases` ob zelo kratkem času t=1/4000s posnamemo nekaj fotk, tako dobimo podatke o šumu zaradi elektronike ADC ojačanje...
- `flats` pri istih nastavitvaf in temperaturi času damo čez objektiv belo blago in ga osvetljimo z enakomerno belo svetlobo (telefon z belo sliko), čas osvetljevanja nastavimo na 50% pri enaki ISO vrednosti.

