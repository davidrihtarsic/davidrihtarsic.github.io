# Uporaba digitalnih vhodov

Za digitalne spremembe kot so naprimer: pritisk na tipko, prehod predmeta mimo svetlobnih vrat... najpogosteje uporabljamo digitalne vhodne priključke krmilnika. Le-te lahko najdemo na priključkih **D0..D13** in tudi na **A0..A7**. Primer enostavne vezave tipke na krmilnik prikazuje slika [@fig:SW_uK6.png].

## Različne možnosti vezave tipke

![Vezava tipke na digitalni vhod krmilnika Arduino.](./slike/PBSw_All.png){#fig:SW_uK6.png height=7cm}

> ### NALOGA: Zaznavanje digitalnih vrednosti
>
> 1. Preskusite delovaje vseh teh vezav tipke, ki so prikazani na shemi.
> 2. Napišite program s katerim boste lahko zaznali spremembo digitalnega vhoda (pomagajte si s funkcijo, ki jo prikazuje [@lst:dig_chg]).

```cpp
void waitForInputChange(int INPUT_PIN){
    bool zacetno_stanje = digitalRead(INPUT_PIN);
    bool trenutno_stanje = zacetno_stanje;
    while (trenutno_stanje == zacetno_stanje)
        trenutno_stanje = digitalRead(INPUT_PIN);
}
```
: Primer funkcije za zaznavanja spremembe na digitalnem vhodu. {#lst:dig_chg}
