# SNOVANJE TEMPERATURNEGA SENZORJA 

Termistor je element, katerega upornost je odvisna od tempreature. Poznamo
dva tipa termistorjev:

- NTC: pri katerih je upornost termistorja v obratnem razmerju s termperaturo
    (t.j. če se termperatura poveča, se njegova upornost zmanjša in obratno) in
- PTC: pri katerih je upornost termistorja v pozitivnem razmerju s termperaturo
    (t.j. če se termperatura poveča, se tudi upornost termistorja poveča).

## Steinhart–Hart model termistorja

Upornost NTC termistorja v odvistnosti od temperature lahko dobro opišemo z
Steinhart–Hart modelom z [@eq:stainhart_eq]:

$$ \frac{1}{T}=A + B ln R + C(lnR)^3,$${#eq:stainhart_eq}

kjer je $T$ trenutna temperatura termistorja v kelvimih, $R$ trenutna upornost
termistorja in konstante $A, B, C$, ki so odvistne od modela in tipa termistorja.

Če [@eq:stainhart_eq] preuredimo v bolj splošno obliko, lahko zapišemo tudi:

$$ R_{NTC} = R_0\ e^{\beta(\frac{1}{T}-\frac{1}{T_0})}, $${#eq:r_ntc_betha}

kjer je $R_{NTC}$ trenutna upornost termistorja, $R_0$ standardna upornost termistorja
pri $T_0$ in $\beta$ koeficient termistorja.

Načeloma lahko te karakteristične podatke pridobimo iz kataloških dokumentov.
Vendar v praksi to vedno ni mogoče in koeficient $\beta$ določimo eksperimentalno.
To storimo tako, da izmerimo upornost termistorja pri dveh različnih temperaturah in
meritve vstavimo v ločeni [@eq:r_ntc_betha]. Te dve enačbi uporabimo in izpostavimo
faktor $\beta$:

$$ \beta=\frac{ln\frac{R_{T_1}}{R_{T_2}}}{\frac{1}{T_1}-\frac{1}{T_2}} $${#eq:beta_experimental}

> ### NALOGA: KARAKTERISTIČNI PODATKI TERMISTORJA
>
> Pridobi karakteristične podatke termistorja, ki jih predvideva [@eq:r_ntc_betha]:
>
> - $R_0$=
> - $T_0$=
> - $\beta$=
>
> V kolikor teh podatkov ni možno pridobiti, jih lahko eksperimentalno določiš
> z [@eq:beta_experimental].
> 
>
>
> 

## Konstruiranje temperaturnega senzorja s termistorjem

Območje : T= [10 .. 40] stopinj Celzija

$$ R_{REF} = \sqrt{R_{NTC_{min}} R_{NTC_{max}}} $${#eq:r_ref_equ}

> ### NALOGA: DELILNIK NAPETOSTI Z REFERENČNIM UPOROM
>
> 1. Sestavite delilnik napetosti z referenčnim uporom, ki ga določite tako, da bo
> imel temperaturni senzor najboljši odziv v danem območju.
>
> - $R_{NTC_{min}}=$
> - $R_{NTC_{max}}=$
> - $R_{REF}=$
>
> 2. Senzor priključite na krmilnik ESP32_DevKitC in odčitajte izhodno napetost
> senzorja. Ta podatek prikazujte na zaslonu računalnika (po UART komunikaciji).
>
> 3. Program dopolnite tako, da izračunate upornost termistorja in izpisujte še 
> ta podatek.
>

## Izračun temperature

<!--
https://circuitdigest.com/microcontroller-projects/interfacing-Thermistor-with-arduino
-->

> ### NALOGA: PREIZKUS SENZORJA  
>  
> 1. Iz [@eq:r_ntc_betha] izpeljite izračun temperature.
>
> 2. Program dopolnite tudi s preračunom upornosti termistorja v temperaturo in
> izpistjte tudi ta podatek.
>  
> Podajte ustrezno dokumentacijo, ki naj vključuje:
>
>   1. fotografije poskusa,
>   2. elek.-teh. shema,
>   3. program krmilnika,
>   4. izpis vrednosti ter vaše ugotovitve o točnosti in pomanjkljivosti sistema.
>

## Ojačanje izhodnega signala


> ### NALOGA: OJAČANJE IZHODNE NAPETOSTI SENZORJA
>  
>  Z ustreznimi elektronskimi sistemi (npr.: diferencialnim ojačevalnim sistemom)
>  prilagodite izhodni napetostni potencial temperaturnega senzorja tako,
>  da bo območje izhodne napetosti $U_{OUT}=[0 .. 3,0]V$ ustrezalo temperaturnemu
>  območje $T_{MIN-MAX}=[0 .. 40]^\circ C$.
>  
> Vhod krmilnika tudi primerno zavarujte proti napetostim večjim od 3.3V.
>  
>  Dokumentacija naloge naj vsebuje:
>
>  1. el.-teh. shemo in
>  2. rezultate vsaj ene meritve z ugotovitvami (kako vam je transformacija uspela).

