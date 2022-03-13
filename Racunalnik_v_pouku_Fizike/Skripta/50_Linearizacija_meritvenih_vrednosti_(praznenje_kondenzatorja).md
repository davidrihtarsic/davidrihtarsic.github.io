# LINEARIZACIJA MERITVENIH VREDNOSTI (PRAZNENJE KONDENZATORJA)

Izvedli bomo poskus, pri katerem bomo lahko meritve odvisne spremenljivke (napetost) opravili pri različnih vrednostih neodvisne spremenljivke (čas). Iz rezultatov bomo skušali izluščiti kapaciteto kondenzatorja (kot iskano konstatnto sistema). Ker je fizikalni pojav nelinearen, ga bomo najprej linearizirali, in šele nato izračunali iskano konstanto (kapaciteto kondenzatorja). Tako lahko v izračun enostavno vključimo vse meritve...

> ### NALOGA: Izračun vrednosti s pomočjo regresijske premice.
> Izvedite poizkus praznjenja kondenzatorja in izmerite $U_C(t)$. Podatke linearizirajte tako, da jim boste lahko dodelili regresijsko premico.\
> Izračunajte:\
> - resresijski koeficient: $R²$:_________,\
> - enačba smernega koeficienta lienaricacije:\
> - vrednost smernega koeficienta:\
> - vrednost kapacitete kondenzatorja:

## Vezje in zajem podatkov

Vezje sestavimo po sliki [@fig:Cap_uK.png]:

![Vezava vezja za zajem napetosti na kondenzatorju.](./slike/Cap_uK.png){#fig:Cap_uK.png height=7cm}

## Linearizacija

$$ f(x) = k x + n $${#eq:linearna}

$$ U_C(t) = U_0 e^{-\frac{t}{R C}} $${#eq:praznenje_kondenzatorja}

$$ ln U_0 = -\frac{1}{R C} t + ln U_C $${#eq:praznenje_lin}

ali ...

$$ ln(\frac{U_C}{U_0}) = - \frac{1}{R C} t $${#eq:praznenje_log}

## Koeficienti regresijske premice

```
=SLOPE(y-Range,x-Range)
```

```
=INTERCEPT(y-Range,x-Range)
```

```
Korelacija med x in y.
=CORREL(y-Range,x-Range)
```

```
Korelacija med y_0 in y.
=RSQ(y-Range,x-Range)
```

