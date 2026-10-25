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
| 1.6 Analogni optični prenos | Trenutno ni samostojnega KiCad/SPICE primera za tokovno-napetostni pretvornik. |

Projektne datoteke `.kicad_pro`, sheme `.kicad_sch`, izrisane slike, PDF-ji in
varnostne kopije so pri posameznem primeru ohranjeni skupaj. Pri simulaciji
odpri projektno datoteko `.kicad_pro`, če je na voljo, saj tako KiCad ohrani
nastavitve projekta in povezave med shemami.
