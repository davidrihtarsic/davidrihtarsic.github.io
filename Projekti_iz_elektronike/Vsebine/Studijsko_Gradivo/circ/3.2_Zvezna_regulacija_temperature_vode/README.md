# Gradivo za 3.2 Zvezna regulacija temperature vode

Primeri za podpoglavje 3.2, razvrščeni po razdelkih: 3.2.3 (ojačevalnik moči), 3.2.4 (PWM), 3.2.5 (mikrokrmilnik) in 3.2.8 (preverjanje znanja). Shemi 320 in 322 sta namenjeni risbi, ne simulaciji
(modelov SPICE še ni); mapa 325 vsebuje simulacijo. Pregledni PDF, SVG in PNG so v mapah primerov; PNG (izvožen s `svg2png`
iz črno-belega SVG brez okvirja) je uporabljen kot slika v poglavju 3.2
(`fig:ojacevalnik-moci`, `fig:pwm-regulator`).

| Mapa | Vsebina |
|---|---|
| `3.2.3_Ojacevalnik_moci/320_Ojacevalnik_moci/` | Zvezna regulacija z ojačevalnikom moči: LM35 ($U_1$), nastavitev $U_R$ s potenciometrom in stalnima upornostma, odštevalnik z LM358 ($U_2=A'(U_R-U_1)$), druga enota LM358 kot sledilnik z ojačenjem 1 in močnostni tranzistor BD135 z emitorskim grelcem $R_{br}$; povratna zveza z emitorja na invertirajoči vhod. |
| `3.2.4_PWM_regulator/322_PWM_regulator/` | Pulzno-širinska regulacija: enaka vhodna stopnja, druga enota LM358 kot primerjalnik ($U_2$ proti žagasti napetosti $U_{tri}$, vhod Global Label) in stikalni tranzistor TIP122 z grelcem $R_{br}$ med $+U_C$ in kolektorjem. |
| `3.2.3_Ojacevalnik_moci/325_Odstevalnik_LM358/` | Simulacija ojačevalnika moči z odštevalnikom (KiCad/ngspice): štirje upori po $22\,\mathrm{k}\Omega$ ($A'=1$), vira $U_{TMP}$ (impulz 1 V → 3 V) in $U_{SET}$ (2,5 V), druga enota LM358 kot sledilnik, BD139 in grelec 100 $\Omega$, napajanje 9 V, `.tran 100m 12s`. Vsebuje še `325_Odstevalni_sistem.png` z rezultatom simulacije in varnostno kopijo `.kicad_sch-bak`. |
| `3.2.5_Mikrokrmilnik/` | Sorazmerna regulacija z Arduinom Uno v SimulIDE (`323_P_regulator.sim2`, posnetek `323_P_regulator.png`): senzor DS18B20 na D10 z uporom 4,7 k$\Omega$ proti 5 V, PWM na D3 krmili grelec 10 $\Omega$ / 12 V prek tranzistorja, osciloskop prikazuje izhod PWM. Program `3.2.5_Mikrokrmilnik.ino` (OneWire in DallasTemperature) in prevedeni `3.2.5_Mikrokrmilnik.hex`. |
| `3.2.8_Preverjanje_znanja/328_Analiza_vezja/` | Vezje za preverjanje znanja (analiza celotnega temperaturnega regulatorja), prerisano po Kocijančičevem gradivu (str. 27): LM35 ($\mathrm{ps}\,1$: filter RC, $\mathrm{ps}\,2$: neinvertirajoči ojačevalnik z ojačenjem 10, $\mathrm{ps}\,3$: Schmittov sprožilnik s histerezo $P_1$, $\mathrm{ps}\,4$ in $\mathrm{ps}\,5$: referenca $U_2$ iz Zenerjeve diode 3,9 V s sledilnikom), izhod s LED, MOSFET-om, relejem in bremenom ???. Namesto izvornih operacijskih ojačevalnikov je uporabljen simbol LM321. |

Številka 321 ni uporabljena, ker je v `circ/` že starejša shema
`321_Triangular_voltage_NE555.kicad_sch` (generator žagaste napetosti).

Shemi uporabljata simbole knjižnic KiCad; ojačenje $A'$ pomeni razmerje upornosti
$A'R/R$ odštevalnika. Vrednosti elementov (razen $R$, $A'R$) niso določene, ker
shemi ponazarjata zgradbo vezja.

## Simulacija 325

Projekt `325_Odstevalnik_LM358/` je bil prej neposredno v `circ/`; datoteke so
premaknjene v podmapo `3.2.3_Ojacevalnik_moci/` (imena in vsebina so nespremenjena).

Modela LM358 in BD139 imata v shemi absolutni poti:

`/home/david/.local/share/kicad/SpiceLibrary/Models/Operational Amplifier/LM358-dual.mod`
`/home/david/.local/share/kicad/SpiceLibrary/Models/Transistor/BJT/BD139.LIB`

Knjižnici nista vključeni v projekt. Na računalniku, kjer poti ne obstajata, je
treba izbrati ustrezni lokalni knjižnici in preveriti preslikavo priključkov.
Simulacija v tem okolju ni bila ponovno izvedena; slika
`325_Odstevalni_sistem.png` je shranjen rezultat iz prejšnje izvedbe.

## Simulacija 323 (SimulIDE)

Program `3.2.5_Mikrokrmilnik.ino` prevedemo v Arduino IDE (potrebni sta knjižnici
OneWire in DallasTemperature) in prevedeni `.hex` shranimo kot
`3.2.5_Mikrokrmilnik.hex`, na katerega kaže simulacija. Auto_Load je izklopljen,
zato program pred zagonom naložimo v mikrokrmilnik. Temperaturo senzorja DS18B20
nastavimo v simulatorju. Brez upora 4,7 k$\Omega$ med podatkovno žico in 5 V se
senzor ne odzove.

Simulacijo je z dejanskim programom preizkusil avtor gradiva; v tem okolju je
nisem mogel zagnati v SimulIDE 2.0. Na posnetku `323_P_regulator.png` je kanal
osciloskopa še poimenovan »PWM D9«, čeprav je izhod PWM na D3.
