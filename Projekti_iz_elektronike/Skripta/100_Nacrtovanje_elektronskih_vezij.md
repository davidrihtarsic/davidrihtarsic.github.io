# NAČRTOVANJEM ELEKTRONSKIH VEZIJ
Tudi pri pedagoškem procesu je pomembno, da so vezja narisana nazorno (tako sheme,
kot tudi sestavljanje vezja na prototipni ploščici). V ta namen lahko uporabljate različna
orodja. Omenili bomo vsaj dva, ki sta prosto-dostopna in bi priporočali njihovo uporabo.

Blokovna razdelitev sheme:

- Vezje razdelite na smiselna pod-vezja (bloke) in jih primerno poimenujte in označite.
- Shemo vezja skušajte orientirati tako, da so na levi strani elementi in pod-vezja, ki so namenjena vhodnim funkcijam,
- na desni strani pa pod-vezja, ki so namenjena izhodnim funkcijam.

Označevanje elementov:

- Uporabljajte IEEE standard simbolov za elemente.
- Elemente opremite s pripadajočimi znakovnimi simboli iz zaporednimi številkami (npr.: R1, R2, L1, C1, C2, C3, IC1...).
- Ob simbolu elementa naj bo vpisana tudi njegova predvidena vrednost (100 Ohmov ali 3k3, 2.7 uF ...).

Označevanje napetostnih potencialov:

- Nedvoumno označite različne napetostne potenciale (Vcc, GND) in njihove vrednosti (+5V, 9V).
- Povezave istih napetostnih potencialov naj bodo v isti višini sheme.
- Višji potenciali naj bodo višje na shemi, nižji pa nižje.

Risanje povezav:

- Povezave naj bodo enostavno sledljive, brez nepotrebnih križanj in sprememb smeri.
- Povezave naj se ne vračajo v smer od koder so si izvirale povezave vhodnih signalov.
- Nedvoumno naj bodo označena stičišča povezav (z debelejšo piko).
- Pomembnejše povezave poimenujte z njihovimi funkcijami.

## Stikalne sheme
EasyEDA je spletno orodje, ki je namenjeno risanju elektronskih vezij, načrtovanju TIV in
izdelavi potrebnih datotek za njihovo izdelavo. Primer stikalne sheme krmilnika RobDuino lahko vidite
na [@fig:RobDuino_Power],[@fig:RobDuino_Inputs] in [@fig:RobDuino_Output].

![Stikalna shema modula RobDuino - napajalni del.](./slike/RobDuino_Power.png){#fig:RobDuino_Power}

![Stikalna shema modula RobDuino - vhodni del.](./slike/RobDuino_Inputs.png){#fig:RobDuino_Inputs}

![Stikalna shema modula RobDuino - izhodni del..](./slike/RobDuino_Output.png){#fig:RobDuino_Output}

> ### NALOGA: Stikalne sheme
> V programskem orodju EasyEDA narišite shemo astabilnegamultivibratorja, izvozite sliko sheme in jo vključite v poročilo.

## Tiskana vezja

> ### NALOGA: Risanje TIV
> Za to vezje izrišite TIV in izpišite seznam elektronskih komponent. Izgled TIV izvozite in vstavite v poročilo. Prav tako vstavite seznam komponent.

## Virtualna vezja

Sestavljanje vezij pa na prototipni plošči pa je drugačen proces in za začetnike precej zahteven,
zato je priporočljivo, da uporabljate orodja kot so TinkerCAD-Circuits.

> ### NALOGA: Sestavljanje virtualnih vezij
> V programskem orodju TinkerCAD-Circuits sestavite vezje na prototipni ploščici in sliko vstavite v poročilo.
>

