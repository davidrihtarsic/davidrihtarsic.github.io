# SNOVANJE TEMPERATURNEGA SENZORJA

## Temperaturni senzor LM35

Temperaturo bomo merili s senzorjem temperature LM35. Poglejmo si [dokumentacijo](https://www.ti.com/lit/ds/symlink/lm35.pdf) tega integriranega vezja in izpišite nekaj osnovnih podatkov.

> ### NALOGA: OSNOVNI PODATKI SENZORJA LM35  
>
> Odziv senzorja $K_{LM35} =$  
> Točnost senzorja $\Delta T =$  
> Temp. del. območje =  
>  
> **ELEKTRIČNE SPECIFIKACIJE:**  
>  
> Napajalna napetost $U_s =$  
> Izh. not. upornost. $R_{OUT} =$  
> Najv. izh. tok $I_{OUT-MAX} =$  

> ### NALOGA: PREIZKUS SENZORJA  
>  
> 1. Temperaturni senzor LM35 priključite na napajanje in ga postavite v okolje s konstantno temperaturo (posoda z vodo cca 35°C in preverite temperaturo z dodatnim termometrom.
> 2. Izhodni priključek povežite na vhod krmilnika ESP32_DevKitC in preverite napetostni odziv.
> 3. Krmilnik ESP32_DevKitC naj izmerjene podatke prikazuje v napetosti ter jih po serijski komunikaciji UART pošilja računalniku.
>  
> Z ustrezno dokumentacijo, ki naj vključuje:
>
>   1. fotografije poskusa,
>   2. elek.-teh. shema,
>   3. program krmilnika,
>   4. izpis vrednosti ter vaše ugotovitve
>
> opišite preskus temperaturnega senzorja.

Programske vrstice za povprečno vrednost meritve:

```cpp
int ADC = 0;
for (int i = 0; i < 128; i++) {
  ADC += analogRead(A7);
  delay(1);
}
float avg_ADC = float(ADC/128.0);
```

> ### NALOGA: OJAČANJE IZHODNE NAPETOSTI SENZORJA
>  
>  Z ustreznimi elektronskimi sistemi (npr.: ojačevalnik napetosti) prilagodite izhodni napetostni potencial temperaturnega senzorja tako, da bo območje izhodne napetosti $U_{OUT}=[0 .. 3,0]V$ ustrezalo temperaturnemu območje $T_{MIN-MAX}=[0 .. 40]^\circ C$.
>  
> Vhod krmilika tudi primerno zavarujte proti napetostim večjim od 3.3V.
>  
>  Dokumentacija naloge naj vsebuje:
>
>  1. el.-teh. shemo in
>  2. rezultate vsaj ene meritve z ugotovitvami (kako vam je transformacija uspela).
