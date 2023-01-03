# SVETLOBNI SPOJNIKI

Pred davnimi časi, ko svet še ni slišal za digitalno tehnologijo, se je gospod Samuel Morse
domislil, da bi črke kodiral v kratke in dolge pulze. Te pa bi lahko kar najlažje pošiljal od
ene točke do druge na najrazličnejše načine ... in telekomunikacije so prijokale na svet.

## Vklop porabnika s tranzistorjem

Pogosto moramo porabnike skozi katere tečejo večji tokovi ($I\ >\ 500\ mA$) vključiti
s tranzistorjem.

> ### NALOGA: Vklop žarnice s tranzistorjem
>
> 1. Za pošiljanje Morsejevih znakov uporabite žarnico. Ali nek drug vir z večjo
> svetilnostjo.
>
> 2. Dolge in kratke pulze bomo pošiljali s svetlobnim oddajnikom. Načrtujete
> ustrezno rešitev (narišite shemo vezja) tako, da bomo s pritiski na tipko
> vklapljali in izklapljali svetilo (uporabite žarnico [12V in 0,6 A]).
> 3. Bodite pozorni, na električne omejitve tipke, ki jih najdete v
> [navodilih za uporabo](https://www.ic-elect.si/fileuploader/download/download/?d=0&file=custom%2Fupload%2FFile-0-48295100-1594733936.pdf) tipke. Načrtujte ustrezno rešitev.

## Komparator napetosti

V kolikor želimo ločiti med dvema napetostnima nivojema, lahko uporabimo komparator napetosti s
primerno izbrano (ali celo nastavljivo) referenčno vrednostjo.

> ### NALOGA: Komparator napetosti
>
> 1. Načrtujte (shema vezja) in izdelajte svetlobni sprejemnik, v katerega boste za zaznavanje
> osvetljenosti uporabili elektronski element s hitrim odzivom.
>
> 2. Analogni signal senzorja modificirajte tako, da boste lahko nedvoumno
> podajali informacijo (npr. LED svetilo), ki jo je poslal svetlobni
> oddajnik.
>
> 3. Z osciloskopom zajemite časovni potek napetostnega potenciala na 
> vhodnem in na izhodnem priključku komparatorja.

## Schmittov sprožilnik

Iz prejšnje naloge lahko ugotovimo, da je izhodni signal svetlobnega senzorja
opremljen z neželeno motnjo. Če v tem primeru želimo ločiti dve različni stanji senzorja,
komparator napetosti ni dobra rešitev. Ob prehodu senzorja iz enega stanja v drugega tako dobimo
na izhodu komparatorja več prehodov, čeprav se je osvetljenost senzorja spremenila le enkrat. Tako
lahko ugotovimo potrebo po histerezi s katero bomo bomo mejno vrednost razmejili na dve
mejni vrednosti. Tako ločevanje nam omogoča schmittov sprožilnik.

> ### NALOGA: Komparator napetosti s šmitovim sprožilnikom
>
> 1. Iz grafa prejšnje naloge, ki predstavlja časovno odvisnost napetostnega potenciala vhodnega in izhodnega signala, odčitajte nove mejne vrednosti ( $U_{h1}\ in\ U_{h2}$).
>
> 2. Komparator napetosti iz prejšnje naloge zamenjajte s komparatorjem napetosti s šmitovim sprožilnikom (narišite stikalno shemo).
>
> 3. Z osciloskopom zajemite časovni potek napetostnega potenciala na 
> vhodnem in na izhodnem priključku komparatorja napetosti s šmitovim sprožilnikom.


