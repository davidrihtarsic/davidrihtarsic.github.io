## Pogoste zmotne predstave v elektroniki

Poučevanje in učenje je vedno posreden proces. Kar pomeni, da učenec ne ponotranji vsebin v točno takšni obliki, kot mu jih poda učitelj. Vsebine, ki jih učenec prejme, vedno interpretira po svojih najboljših zmožnostih, ki temeljijo na njegovih preteklih izkušnjah. Zato je proces učenja bolj predvidljiv in učinkovit če:

- ima učenec veliko predhodnih izkušenj iz te tematike,
- so vsebine čim bolj konkretne in jih je možno zajeti s čim več čuti,
- je možna enostavna de-kompozicija problema (zožanje problema na eno spremenljivko),
- so vzročno-posledične situacije jasno predvidljive,
- lahko vsebino najprej obravnavamo s konkretnimi elementi in šele nato v abstraktni obliki.

Hitro lahko ugotovimo, da za področje elektronike prav nič od zgoraj naštetega ne velja in zato je učenje teh vsebin še posebej nepredvidljivo in si vsak posameznik interpretira podano znanje čisto po svoje. Tako je poučevanje in učenje elektronike zelo težaven proces. Mogoče vam bodo prišla prav izpostavljena nekatera pogosta napačna prepričanja s tega področja.

### Baterija zagotavlja vedno enak tok.
Ne! **Baterija je napetostni vir**, kar pomeni, da zagotavlja vedno enako napetost (v idealnem primeru). Na primer 9 V baterija nam bo zagotavljala napajalno napetost 9 V vse dokler se ne "izprazne".

### Ohmov zakon je U R I.
Enačbo $U=R I$ si je res enostavno zapomniti, vendar ta enačba namiguje, da je napetost odvisna od toka U(I). Kar pa ni res! **Tok je odvisen od napetosti** in prav tako je George Ohm zapisal svoj zakon:

$$ I = \frac{1}{R}U $${#eq:ohms_law}

### Ohmov zakon velja le lokalno.
Če se upornost nekega elementa spremeni, na primer da se poveča. Bo posledično skozenj tekel manjši električni tok. Vendar tu se zgodba ne konča! Manjši tok bo tekel tudi po ostalem delu vezja in električni tokovi in napetosti se bodo najverjetneje spremenili v celotnem vezju. Na zadnje bo manjši tok tekel iz baterije ali celo iz elektrarne, če ga napajamo preko vtičnice. Večino takih situacij rešujemo z uporabo:

1. Ohmovega zakona lokalno (na dotičnem elementu),
2. Ohmovega zakona globalno z upoštevanjem nadomestne upornosti in
3. obeh Kirchhoffovih izrekov (zlasti $\sum_{n=1}^{n}U_n=0V$).

### U2off odčitamo na x osi.
Glavna naloga ojačevalnega sistema je, da ojača nek vhodni napetostni potencial $U_1$ z izbranim faktorjem $A'$ in ga ponudi na izhodu kot izhodni napetostni potencial $U_2$. Tako sledi, če bi na vhod priključili $U_1 = 0V$, bi na izhodu prav tako pričakovali $U_2 = 0V$. Vendar temu ni tako! V realnem vezju izmerimo: 

$$U_2 = U_{2off} \quad \text{pri}\ U_1=0V\ .$${#eq:u2off}

$U_{2off}$ je napaka invertirajočega ojačevalnega sistema in jo sistem "podeduje" z napako operacijskega ojačevalnika, ki jo imenujemo preostala napetost in označujemo z $U_{off}$. Prenosna funkcija $U_2(U_1)$ invertirajočega ojačevalnega sistema je v svojin mejah kar linearna funkcija, odvisna od vhodnega napetostnega potenciala $U_1$:

$$ U_2 = A'U_1\ +\ (-A'+1)U_{off}\ ,$${#eq:inv_oj_sis_fun}

kjer je $U_1$ vhodni, $U_2$ izhodni napetostni potencial, $A'=-\frac{R_2}{R_1}$ je koeficient napetostnega ojačanja tega sistema in $U_{off}$ napetostni premik operacijskega ojačevalnika. Zato [@eq:inv_oj_sis_fun] zelo spominja na linearno funkcijo $y(x) = k x\ +\ n$. **Enostavno lahko ugotovimo, da je $(-A'+1)U_{off}$ prosti člen funkcije v [@eq:inv_oj_sis_fun] in ga odčitamo na presečišču funkcije z y osjo.** Če združimo [@eq:u2off] in [@eq:inv_oj_sis_fun]:

$$ U_{2off} = (-A'+1)U_{off}\ ,$${#eq:u2off_uoff}

dobimo zvezo, ki nakazuje kako napaka operacijskega ojačevalnika $U_{off}$ vpliva na napako celotnega ojačevalnega sistema $U_2off$.
