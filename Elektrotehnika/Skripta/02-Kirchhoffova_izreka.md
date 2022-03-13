# KIRCHHOFFOVA IZREKA

Omenili smo že, da pri reševanju elektrotehniških problemov, zelo pogosto uporabljamo Ohmov zakon. Prav tako pogosto, pa nam prideta prav še oba Kirchhoffova izreka. 

## 1. Kirchhoffov izrek

Prvi Kirchhoffov izrek govori, da je **vsota električnih tokov v izbranem vozlišču enaka nič**. Ta izrek lahko predstavimo z [@eq:kirck1]

$$ I_1 + I_2 + (-I_3) + ... = 0 $${#eq:kirck1}

in nakazuje, da se naboj ne more kopičiti v vodnikih. To pomeni, da če po neki žici naboj priteče v vozlišče, ga bo od tam tudi prav toliko odteklo. Za [@eq:kirck1] velja, da smo vse pritekajoče tokove v sumacijsko točko definirali kot pozitivne. Medtem ko imajo odtekajoči tokovi negativen predznak (npr.: $I_3$).

> ### NALOGA: SUMACIJSKA TOČKA EL. TOKOV  
> Sestavite električno vezje s poljubno napajalno napetostjo. V to vezje vključi 3 upore različnih upornosti (npr.: $R_{1..3}= 100\Omega .. 10 k\Omega$) - izberete lahko isto električno vezje iz 1. vaje o Ohmovem zakonu. Vezava naj bo neka kombinacija vzporednih in zaporednih vezav.
> Za vsaj dva različna primera napajalnih napetosti predstavite, da velja 1. Kirchhoffov izrek. Odgovor naj vsebuje:
>
>   1. električno shemo vezja s ključnimi el. veličinami,
>   2. označite (kompleksnejšo) poljubno sumacijsko točko v vezju,
>   3. izmerite vse pritekajoče in odtekajoče tokove sumacijske točke in
>   4. pravilno zapišite [@eq:kirck1] z vstavljenimi podatki.

## 2. Kirchhoffov izrek

Drugi Kirchhoffov izrek predpostavlja, da je **vsota vseh razlik napetostnih potencialov v zaključenem električnem tokokrogu enaka 0**. Za primer žepne svetilke, bi ta izrek lahko zapisali tudi z [@eq:kirch21]

$$ U_{G_1} + U_{G_2} + U_{G_3} + (-U_R) + (-U_{LED}) = 0 $${#eq:kirch21}

pri čemer velja, da če se napetostni potencial v izbrani smeri poveča, je razlika pozitivna in negativna, če se napetostni potencial v izbrani smeri zmanjša (npr.: napetost na žarnici $U_{LED}$).

Ta isti izrek boste večkrat našli zapisan tudi tako, da je: **vsota vseh gonilnih napetosti v zaključenem električnem krogu enaka vsoti vseh razlik napetostnih potencialov na porabnikih.** Ko imamo v vezju le en napetostni vir (v večini primerih), bi ta izrek lahko predstavili z [@eq:kirch2]:

$$U_{G_1} = U_{R_1} + U_{R_2} + ... $$ {#eq:kirch2}

> ### NALOGA: NAPETOSTNI POTENCIAL V TOKOKROGU  
> Na primeru vezja iz prejšnje naloge nastavi poljubno znano napajalno napetost (novo, ki je še nisi preskusil) :
>
> 1. sestavi zapise enačb 2. Kirchhoffovega izreka za vse tokokroge v vezju,
> 2. sestavite zapise enačb za vse sumacijske točke v vezju,
> 3. za vse upore sestavite enačbo Omovega
> 4. rešite sistem enačb ter izračunajte napetosti in tokove skozi vse elemente ter
> 5. jih primerjajte z izmerjenimi vrednostmi.


