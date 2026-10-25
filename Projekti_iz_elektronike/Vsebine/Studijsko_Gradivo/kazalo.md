# Kazalo skripte Projekti iz elektronike

Kazalo je delovno vsebinsko ogrodje skripte. Številčenje datotek omogoča, da
lahko posamezno poglavje ali podpoglavje urejamo in generiramo ločeno.
Prvo poglavje je razdeljeno po dogovorjeni vsebinski strukturi, podpoglavja
druge ravni pa so shranjena v samostojnih datotekah.

## 0. Uvod

- [0.0 Uvod](./0.0_UVOD.md)

## 1. Optične komunikacije

- [1.0 Optične komunikacije](./1.0_OPTICNE_KOMUNIKACIJE.md)
  - Namen in področja uporabe optičnih komunikacij
  - Osnovni gradniki: oddajnik, optični kanal, sprejemnik in obdelava signala

  - [1.1 Digitalni optični prenos](./1.1_Digitalni_opticni_prenos.md)
    - Osnovni princip digitalnega optičnega prenosa
    - Prosti prostor in optični vodnik

  - [1.2 Svetlobni oddajnik](./1.2_Svetlobni_oddajnik.md)
    - Svetleča dioda (LED)
    - Omejevanje toka LED in izbira zaporednega upora
    - Krmiljenje LED z izhodom krmilnika
    - NPN-tranzistor kot stikalo
    - Darlingtonov spoj in integrirani gonilniki

  - [1.3 Svetlobni sprejemnik](./1.3_Svetlobni_sprejemnik.md)
    - LDR, fototranzistor in fotodioda
    - Delilnik z LDR in svetlobno stikalo
    - Potreba po ojačitvi oziroma obdelavi signala fotodiode in fototranzistorja

  - [1.4 Oblikovanje digitalnega signala](./1.4_Oblikovanje_digitalnega_signala.md)
    - Pretvorba analognega signala v logični signal s komparatorjem
      - TTL-napetostni nivoji
      - Komparator z odprtim kolektorjem
    - Schmittov sprožilnik in histereza
      - Digitalna vrata s Schmittovim sprožilnikom (74HC14)
      - Simetrično napajanje: histereza okoli 0 V
      - Enojno napajanje in nastavljiva sredina histereze
    - [Dodatni osnutek: komparator napetosti](./x_014_Komparator_napetosti.md)

  - [1.5 Optične povezave in praktična uporaba](./1.5_Opticne_povezave_in_prakticna_uporaba.md)
    - Svetlobna vrata z zaznavo smeri
    - Optični spojniki in galvanska ločitev
    - Predlogi praktičnih nalog
    - Povzetek in vprašanja za preverjanje

  - [1.6 Analogni optični prenos](./1.6_Analogni_opticni_prenos.md)
    - Prenos zvezno spremenljive informacije s svetlobo
    - Tokovno-napetostni pretvornik za fotodiodo

## 2. Modulacija signala

- [2.0 Modulacija signala](./2.0_MODULACIJA_SIGNALA.md)

  - [2.1 Frekvenčna modulacija](./2.1_Frekvenčna_modulacija.md)
    - Astabilni multivibrator
    - Napetostno-frekvenčni pretvornik

  - [2.2 Amplitudna modulacija](./2.2_Amplitudna_modulacija.md)
    - Napetostno krmiljeni ojačevalniki

  - [2.3 Pulzno-širinska modulacija](./2.3_Pulzno-širinska_modulacija.md)

## 3. Elektronski regulacijski sistemi

- [3.0 Elektronski regulacijski sistemi](./3.0_ELEKTRONSKI_REGULACIJSKI_SISTEMI.md)

  - [3.1 Nezvezna regulacija temperature vode](./3.1_Nezvezna_regulacija_temperature_vode.md)
    - Komparator brez histereze
    - Analogni Schmittov sprožilnik

  - [3.2 Zvezna regulacija temperature vode](./3.2_Zvezna_regulacija_temperature_vode.md)
    - Ojačevalnik moči
    - Merjenje temperature

  - [3.3 Splošno o regulacijski tehniki](./3.3_Splošno_o_regulacijski_tehniiki.md)
    - Krmiljenje in regulacija
    - Zvezne in nezvezne regulacije
    - Konstantna in spremenljiva želena vrednost
    - Dinamične lastnosti regulacijskih sistemov

## 4. Napetostni ojačevalniki

- [4.0 Napetostni ojačevalniki](./4.0_NAPETOSTNI_OJAČEVALNIKI.md)
  - Idealne lastnosti operacijskih ojačevalnikov
  - Tipični predstavniki in njihove lastnosti

  - [4.1 Kompenzacija mirovnega toka in napetostnega premika](./4.1_Kompenzacija_mirovnega_toka_in_napetostnega_premika.md)
    - Kompenzacija napetostnega premika
    - Kompenzacija mirovnega toka

  - [4.2 Digitalno programirljivi ojačevalni sistemi](./4.2_Digitalno_programirljivi_ojačevalni_sistemi.md)

  - [4.3 Diferencialni ojačevalniki](./4.3_Diferencialni_ojačevalniki.md)
    - Osnovni diferencialni ojačevalnik
    - Instrumentacijski ojačevalnik s tremi operacijskimi ojačevalniki

  - [4.4 Uporabna vezja z operacijskimi ojačevalniki](./4.4_Uporabna_vezja_z_operacijskimi_ojačevalniki.md)
    - Logaritemski ojačevalnik

## 5. Digitalna elektronika – sekvenčna vezja

- [5.0 Digitalna elektronika – sekvenčna vezja](./5.0_DIGITALNA_ELEKTRONIKA-SEKVENČNA_VEZJA.md)

  - [5.1 Flip-flopi](./5.1_Flip-flopi.md)
    - R-S flip-flop
    - Sinhroni flip-flop

  - [5.2 Števniki](./5.2_Števniki.md)
    - Asinhroni števniki
    - Sinhroni števniki

  - [5.3 Pomnilni in pomikalni registri](./5.3_Pomnilni_in_pomikalni_registri.md)
    - Pomikalni register

## 6. Uporaba mikrokrmilnikov

- [6.0 Uporaba mikrokrmilnikov](./6.0_UPORABA_MIKROKRMILNIKOV.md)
  - Mikrokrmilnik ATmega328
  - Krmilnik Arduino UNO

  - [6.1 Izhodne enote](./6.1_Izhodne_enote.md)
    - Digitalni izhod in DAC
    - Pulzno-širinska modulacija

  - [6.2 Vhodne enote](./6.2_Vhodne_enote.md)
    - Digitalni vhod
    - Upor proti napajanju
    - Preklopni elementi

  - [6.3 Komunikacijski vmesniki](./6.3_Komunikacijski_vmesniki.md)
    - Serijski periferni vmesnik
    - I²C
    - Internet stvari (IoT)

## 7. Rezervirano poglavje

Poglavje 7 je za zdaj rezervirano, da se ohrani prostor za morebitno vsebinsko
razširitev brez preštevilčenja naslednjih poglavij.

## 8. Druga uporabna vezja

- [8.0 Druga uporabna vezja](./8.0_DRUGA_UPORABNA_VEZJA.md)
  - Napetostni regulatorji
  - TL431
  - Pretvornik za zviševanje napetosti
  - NE555
  - Generator trikotniške napetosti

## 9. Načrtovanje ohišja

- [9.0 Načrtovanje ohišja za elektronsko vezje](./9.0_NACRTOVANJE_OHISJA.md)
  - Načrtovanje vezja v KiCAD-u
  - 3D-podpora in izdelava tiskanega vezja
  - Načrtovanje ohišja v FreeCAD-u
