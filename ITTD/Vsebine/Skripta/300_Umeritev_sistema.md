# UMERITEV SISTEMA

## Interpolacija

> ### NALOGA: UMERITEV SENZORJA  
>  
> Napravite umeritev senzorja po celem temperaturnem območju $T_{MIN-MAX}=[0 .. 40]^\circ C$. Dokumentacija vaje naj vsebuje:
>
> 1. tabelo meritev (temperatura | ADC_vrednost),
> 2. graf umeritve $T(ADC\_vrednost)$,
> 3. dodan ustrezen trend funkcije (verjetno nek polinom n-te stpnje) in
> 4. njene enačbe.

V kolikor želite primeren izpis podatkov tabele sestaviti že na krmilniški strani, lahko podatek o izmerjeni temperaturi z referenčnim termometrom posredujete krmilniku po serijski komunikaciji. Za sprejemanje pa uporabite dodatno funkcijo `serialEvent()` z nasladnim programom:

```cpp
String input_temp = "";
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();  // get the new byte:
    if (inChar == '\n') {               // if ENTER was pressed
      int ADC = analogRead(A0);
      Serial.print(input_temp);Serial.print("\t");Serial.println(ADC);
      //Serial.printf("%d\t%d",input_temperature,ADC);
      input_temp="";
    } else {
      input_temp+= inChar;      // add it to the input_temperature:
    }
  }
}
```

> ### NALOGA: IZPIS TEMPERATURE
>
> S pomočjo enačbe umeritvene krivulje napišite program za krmilnik tako, da bo ustrezno podajal že izračunan podatek o temperaturi. Izračunan podatek primerjajte s temperaturo, ki jo izmerite z referenčnim termometrom. V poročilo vključite:
>
> 1. fotografijo preskusa meritve,
> 2. program krmilnika,
> 3. izpis vrednosti in
> 4. vaš komentar meritve.

Pri preračunu vrednosti polinoma 6. stopnje po [@eq:izr_poli] 
$$ y = k_5x^5 + k_4x^4 + k_3x^3 + k_2x^2 + k_1x^1 + k_0x^0 $${#eq:izr_poli}
si lahko pomagate z naslednjimi programskimi vrsticami.

```cpp
  float k[6] = { -74.9, 530E-3, -1.68E-3, 3.25E-6, -3.12E-9, 1.22E-12};
  float y = 0;
  float ADC = analogRead(A0);
  for (int i = 0; i <= 5; i++) {
    y += k[i] * pow(ADC, i);
  }
```

> ### NALOGA: NAPOVED NA PODLAGI 3-H IZMERJENIH TOČK
>
> Na podlagi eksponentnega časovnega poteka segrevanja temperaturnega senzorja, ki ga podaja [@eq:cooling_law] lahko z meritvijo le treh meritev določimo končno temperaturo. Za ta preračun uporabite [@eq:t_end_calc], ki predvideva, da sta časa med posameznimi meritvami enaki. 
>
> Napišite tak program, ki bo končno temperaturo ocenil na podlagi časovnega odziva. Meritev naj se začne s pritiskom na tipko in uporabniku nudi informacijo o časovnem poteku meritve (pričetek merjenja, vmesni čas, konec meritve). V poročilo vključite:
>
> 1. fotografijo preskusa meritve,
> 2. program krmilnika,
> 3. izpis meritve in uporabniških navodil ter
> 4. vaš komentar.

$$ T(t) = T_k+(T_z - T_k)e^{\frac{t}{\tau}} $${#eq:cooling_law}

$$ T_k = T_1 - \frac{(T_1 - T_2)^2}{T_1 - 2T_2 + T_3} $${#eq:t_end_calc}
