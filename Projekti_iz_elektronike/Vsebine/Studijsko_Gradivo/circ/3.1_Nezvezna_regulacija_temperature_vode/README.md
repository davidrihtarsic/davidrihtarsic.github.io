# Gradivo za 3.1 Nezvezna regulacija temperature vode

## Slike iz izvornega študijskega gradiva

Vir je [Slavko Kocijančič: Projekti iz elektronike](../../Proj-eltron_2020.pdf),
UL PeF, Ljubljana 2011, 2020, gradivo za interno uporabo.

| Datoteka | Vsebina | Tiskana stran / stran PDF |
|---|---|---|
| `310_Rele_simbol_in_primer.png` | Simbol menjalnega releja in fotografija splošnega primera. Fotografija ne predstavlja računskega primera RT424005. | 22 / 25 |
| `312_Termostat_brez_histereze.png` | Izvedbi z LM311 in LM358; temperaturni delilnik je na vhodu (+), grelec na mirovnem kontaktu. | 23 / 26 |
| `313_Termostat_s_histerezo.png` | Izvorna shema z LM358, pozitivno povratno zvezo R–hR in sledilnikom reference. | 24 / 27 |

Sliki 310 in 312 sta izrisani neposredno iz delov izvornih strani pri 300 dpi.
Slika 313 je nespremenjena rastrska slika, izločena iz PDF-ja. To so izvorne
ilustracije, ne nove urejljive KiCadove sheme.

Pri sliki 313 upoštevamo popravek, pojasnjen tudi v besedilu 3.1:
temperaturni signal je na vhodu ($-$), zato je izhod visok pri prenizki
temperaturi. Grelec mora biti za opisano ogrevanje na delovnem kontaktu NO,
ki se sklene ob vzbujeni tuljavi. V izvorni risbi je priključen na mirovni
kontakt; povezavo grelca zato prestavimo na desni kontakt. Izvorna slika
je ohranjena brez retuširanja.

## KiCad/SPICE primer izklopa induktivnega bremena

Celotni dosedanji primer je premaknjen v
`311_Vklop_induktivnega_bremena/`. Skupaj so ohranjeni projekt `.kicad_pro`,
shema `.kicad_sch`, nastavitve `.kicad_prl`, delovni zvezek `.wbk`,
PNG, SVG, PDF in imenik varnostnih kopij.

Imena projektnih datotek in njihova vsebina niso spremenjeni. PNG je bil
prej v `slike/`, projektne datoteke pa neposredno v `circ/`.

Primer prikazuje tuljavo L1 z zaporednim uporom R2 in tranzistorski preklop.
D1 in C1 sta v ohranjenem izhodišču narisana ločeno, brez električne povezave.
Za preizkus zaščitne diode jo je treba pravilno priključiti vzporedno s
tuljavo: katoda proti pozitivnemu napajanju, anoda proti kolektorju.
Pred simulacijo preverimo tudi časovne parametre krmilnega vira in analize.

Model BC108 ima v shemi podedovano absolutno pot:

`/home/david/.local/share/kicad/SpiceLibrary/Models/Transistor/BJT/BJTN.LIB`

Ta knjižnica ni vključena v projekt in v trenutnem delovnem okolju ni na voljo.
Na računalniku, kjer pot ne obstaja, je treba izbrati ustrezno lokalno knjižnico
in preveriti preslikavo priključkov modela. Simulacija ob tej razvrstitvi ni
bila ponovno izvedena; premik datotek sam po sebi ne odpravi zunanje odvisnosti.
