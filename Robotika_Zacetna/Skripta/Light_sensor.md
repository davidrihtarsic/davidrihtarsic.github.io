# SVETLOBNI SENZOR

Svetlobni senzor lahko naredimo na več načinov. Velikokrat ga naredimo kot delilnik napetosti, v katera uporabimo nek element, katerega upornost je odvisna od osvetljenosti. Kot svetlobno občutljiv element navadno uporabljamo:

- foto-upor,
- foto-diodo ali
- foto-tranzistor.

## DELILNIK NAPETOSTI S SPREMENLJIVIM UPOROM

V naši izvedbi svetlobnega senzorja bomo uporabili foto-tranzistor, ki ga bomo vezali v delilnik napetosti z uporom konstantne upornosti. Temu uporu rečemo tudi referenčni upor.

> ### NALOGA: IZBERITE NAJPRIMERNEJŠI REFERENČNI UPOR
>
> 1. Zvežite delilnik napetosti s foto-tranzistorjem in referenčnim uporom ter preverite odziv senzorja na dveh površinah različne osvetljenosti.
> 2. Menjajte referenčne upore in ugotovite pri katerem referenčnem uporu ima senzor največji odziv = se izhodna napetost najbolj spremeni.
> 3. Za vsako meritev nato izmerite/izračunajte (in jih vpišite v tabelo):
>     1. izhodni napetostni potencial senzorja $U_{iz}$ na svetli površini,
>     2. napetost $U_{R_{ref}}$ na referenčnem uporu $R_{ref}$,
>     3. napetost na foto-tranzistorju $U_{Tr}$,
>     4. tok $I_{R_1}$, ki teče skozi $R_{ref}$,
>     5. tok skozi foto-tranzistor - $I_{Tr}$,
>     6. upornost foto-tranzistorja $R_{Tr}$,
>     7. ... nato vse korake od 1. do 6. ponovite še za primer, ko je senzor nad temno površino in izračunajte odziv senzorja - $\Delta U_{iz}$.
> 4. Nato izberite referenčni upor $R_{ref}$ pri katerem ste dobili največji odziv = razlika izhodnega napetostnega potenciala senzorja pri različni osvetljenosti.


| površina | $R_{ref}$ | $U_{iz}$ | $U_{ref}$ | $U_{Tr}$ | $I_{R_{ref}}$ | $I_{Tr}$ | R_{Tr} |
|:--------:|:---------:|:--------:|:---------:|:--------:|:-------------:|:--------:|:------:|
|          |           |          |           |          |               |          |        |
|          |           |          |           |          |               |          |        |
|          |           |          |           |          |               |          |        |
|          |           |          |           |          |               |          |        |
|          |           |          |           |          |               |          |        |
|          |           |          |           |          |               |          |        |
|          |           |          |           |          |               |          |        |
|          |           |          |           |          |               |          |        |
|          |           |          |           |          |               |          |        |
|          |           |          |           |          |               |          |        |
Table: Tabela merite odziva senzorja. {#tbl:odziv_senzorja}

# VOŽNJA ROBOTA PO ČRTI

Ko ste skonstruirali svetlobni senzor z najboljšim odzivom ste že na pol poti do uspeha. Ta korak iz elektronike je zelo pomemben, saj ga kasneje ne moremo nadoknaditi ne programsko in ne mehansko.

## IDEJNA ZASNOVA VOŽNJE PO ČRTI

Pravzaprav robot ne bo vozil po črti ampak po robu črte. Predvidimo, da imamo na levi strani robota črno črto, robot pa se trenutno nahaja vzporedno z njo na desni strani. Logika, ki jo bomo programsko sestavili bo naslednja:

1. Če se robot nahaja na beli površini naj zavije levo naprej. Tako bo zavil levo in zašel na črno površino.
2. Če se robot nahaja na črni površini, pa naj robot zavije desno naprej. Tako bo zavil desno in se zopet znašel na beli površini... tako se bosta ta dva koraka ponavljala.

> ### NALOGA: VOŽNJA PO ČRTI
>
> Sprogramirajte robota tako, da bo vozil po robu črte. V poročilo pa oddajte programsko kodo vaše rešitve.

<!--
```cpp
void loop()
{
  int osvetljenost_tal = analogRead(A0);
  if (osvetlejnost_tal > 300){
    //smo na beli površini...
  }else{
    //smo na črni površini...
  }
}
```
-->

