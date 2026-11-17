# KiCad in SPICE primeri po poglavjih

Primeri v tem direktoriju so razvrščeni po številkah poglavij skripte, kadar gre
za samostojne projekte. Nekatere sheme so del večjega KiCadovega projekta, zato
so ohranjene skupaj; v tabeli so navedene vsebinske povezave na posamezna
podpoglavja.

| Podpoglavje | Primeri |
|---|---|
| 1.0 Optične komunikacije | Celotni projekt v `1.0_OPTICNE_KOMUNIKACIJE/100_Opticna_komunikacija/`; vsebuje glavno shemo optične povezave, Arduino Nano, LED-oddajnik in fototranzistorski sprejemnik. |
| 1.1 Digitalni optični prenos | Ni samostojnega simulacijskega primera. Optična povezava je del celotnega projekta v mapi 1.0. |
| 1.2 Svetlobni oddajnik | SPICE/KiCad projekt Darlingtonovega gonilnika: `1.2_Svetlobni_oddajnik/110_Darlington_open_collector/`. V celotnem projektu v mapi 1.0 sta še shemi `omejilni_upor.kicad_sch` in `darlington_uln2803a.kicad_sch`. |
| 1.3 Svetlobni sprejemnik | Fototranzistorski sprejemnik je v glavni shemi celotnega projekta v mapi 1.0. Za tokovno-napetostni pretvornik fotodiode samostojnega KiCad/SPICE primera še ni. |
| 1.4 Oblikovanje digitalnega signala | Komparatorja: `1.4_Oblikovanje_digitalnega_signala/komparator_120/` in `komparator_1_1/`. Schmittova sprožilnika: `1.4_Oblikovanje_digitalnega_signala/schmitt_122/`. |
| 1.5 Optične povezave in praktična uporaba | Celotni optični sistem z LED, fototranzistorjem, 74HC7014 in Arduinom je v mapi 1.0. |
| 1.6 Analogni optični prenos | Napetostno-tokovna pretvornika: `1.6_Analogni_opticni_prenos/160_...` in `161_...`; tokovno-napetostni pretvornik s fotodiodo: `1.6_Analogni_opticni_prenos/162_Tokovno_napetostni_pretvornik_fotodioda.kicad_sch`. |
| 2.1 Frekvenčna modulacija | KiCadov projekt oscilatorja s 74HC14: `2.1_Frekvenčna_modulacija/210_Oscilator_74HC14.kicad_pro` in `.kicad_sch`; model je pripet na simbol in direktive simulacije so v shemi. Črno-beli pregledni PDF je v isti mapi. Samostojni ngspice primer: `210_Oscilator_74HC14.cir` z idealiziranim modelom `74HC14_idealiziran.lib`. |
| 3.0 Elektronski regulacijski sistemi | Blokovna shema povratne zanke: `3.0_ELEKTRONSKI_REGULACIJSKI_SISTEMI/300_Regulacijska_zanka.png`; izvor je naveden v README te mape. |
| 3.1 Nezvezna regulacija temperature vode | Slike releja, izvornega termostata brez histereze in Schmittove izvedbe so v `3.1_Nezvezna_regulacija_temperature_vode/`. KiCadovi shemi termostata z LM358 sta v podmapah `312_Termostat_brez_histereze/` (brez histereze) in `313_Termostat_s_histerezo/` (s Schmittovim sprožilnikom). Celotni KiCad/SPICE projekt izklopa tuljave, vključno z nastavitvami in varnostnimi kopijami, je v podmapi `311_Vklop_induktivnega_bremena/`. |
| 3.2 Zvezna regulacija temperature vode | KiCadovi shemi zvezne regulacije z LM35 in LM358 sta v podmapah `3.2_Zvezna_regulacija_temperature_vode/3.2.3_Ojacevalnik_moci/320_Ojacevalnik_moci/` (ojačevalnik moči) in `3.2.4_PWM_regulator/322_PWM_regulator/` (PWM regulator). Vezje za preverjanje znanja: `3.2_Zvezna_regulacija_temperature_vode/3.2.8_Preverjanje_znanja/328_Analiza_vezja/`. Simulacija sorazmernega regulatorja z Arduinom Uno in DS18B20 (SimulIDE): `3.2_Zvezna_regulacija_temperature_vode/3.2.5_Mikrokrmilnik/`. Simulacija ojačevalnika moči z odštevalnikom LM358: `3.2_Zvezna_regulacija_temperature_vode/3.2.3_Ojacevalnik_moci/325_Odstevalnik_LM358/`. Starejši generator žagaste napetosti z NE555: `321_Triangular_voltage_NE555.kicad_sch`. |

Projektne datoteke `.kicad_pro`, sheme `.kicad_sch`, izrisane slike, PDF-ji in
varnostne kopije so pri posameznem primeru ohranjeni skupaj. Pri simulaciji
odpri projektno datoteko `.kicad_pro`, če je na voljo, saj tako KiCad ohrani
nastavitve projekta in povezave med shemami.
