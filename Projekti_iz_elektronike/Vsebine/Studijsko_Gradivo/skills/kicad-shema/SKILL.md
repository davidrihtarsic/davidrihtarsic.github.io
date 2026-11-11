---
name: kicad-shema
description: Create or rearrange editable KiCad electrical schematics for electronics study notes, especially from KiCAD SHEMA comments in Markdown. Align related components to show signal or current flow and route short, direct connections. Use for circuit schematics, not block diagrams or decorative images.
metadata:
  input-parameters: "$OPIS_SHEME, $SCALE"
---

# KiCad sheme za teoretično razlago

Izdelaj električno pravilno shemo, katere postavitev jasno pokaže delovanje vezja. Glavni oblikovni merili sta **poravnava povezanih elementov** in **neposredno ožičenje z malo lomi**. Pravilen netlist sam ne potrjuje preglednosti risbe.

## Vhod in obseg

- `$OPIS_SHEME` je opis naloge. Če ni podan, poišči ustrezni komentar `<!-- KiCAD SHEMA: ... -->` v Markdownu ter preberi okoliško razlago in slikovno povezavo. Upoštevaj tudi stare zapise `KiCAD RISBA` oziroma `KIČAD RISBA`. Vprašaj le, če manjka podatek, ki vpliva na pravilno izvedbo.
- `$SCALE` je neobvezen: privzeto `1`, za kompaktno postavitev `0.5`. Druge vrednosti najprej razjasni. Parameter določa razmike, ne velikosti simbolov in pisave.
- Iz `circ/README.md` in obstoječih datotek ugotovi pot, ime in pripadnost projektu. Pri preurejanju ohrani knjižnične simbole, reference, UUID-je, vrednosti, projektne povezave in električno topologijo. Posebne zahteve konkretnega opisa imajo prednost pred privzetim slogom.
- Pred spremembo obstoječe sheme shrani varnostno kopijo in izvozi izhodiščni netlist. Obstoječih varnostnih kopij ne odstranjuj.

## 1. Najprej določi osi postavitve

Pred ožičenjem razdeli vezje na logične podsklope: skupine elementov, ki skupaj prikazujejo eno nalogo, na primer LED z omejilnim uporom, napetostni delilnik ali ojačevalnik s povratno zvezo. Podsklop je tudi vizualna skupina; njegova električna pravilnost ne nadomesti poravnane postavitve.

Za vsak podsklop zapiši kratek načrt: glavno os (skupni X ali Y), vrstni red elementov, koordinate povezanih pinov in mesta odcepov. Splošna navedba »kompaktno« ne zadošča. Nato postavi simbole in njihove veje:

1. **Zaporedne elemente iste poti poravnaj po dejanskih priključkih.** Povezana priključka naj imata enako koordinato Y za vodoravno oziroma X za navpično povezavo. Upoštevaj zamik priključkov glede na grafično sredino simbola. Grafično poravnani sredini ne zadoščata, če je med priključkoma potreben nepotreben zavoj.
2. **Os naj ponazarja potek delovanja.** Signal praviloma potuje od leve proti desni. Pot od višjega napajalnega potenciala do nižjega praviloma poteka od zgoraj navzdol. Podsklopa ne razporedi v stopničasto ali cikcak obliko, če lahko iste povezave pokažeš v eni ravni vrsti ali koloni.
3. **Zaporedni upor in LED** postavi na isto vodoravno ali navpično os. **Delilnik med VCC in GND** praviloma postavi navpično, z VCC zgoraj in GND spodaj. **Upora, ki skupaj tvorita delilnik v signalni ali povratni poti**, praviloma postavi vodoravno, kadar tako jasno pokažeš pot od izhoda prek delilnika do vhoda. Orientacijo določa položaj podsklopa v vezju.
4. Pri glavni poti toka, na primer breme–kolektor–emitor–merilni upor, poravnaj zaporedne tokovne priključke. Pomožne povezave odcepi od te ravne poti.
5. Pri aktivnem elementu najprej določi vhodno in izhodno os, položaj povratne veje ter neposredna napajanja. Povratno vejo postavi na stran, kjer ne obkroža vhodnega signala; pri običajni postavitvi OZ je to praviloma pod njim. Uporabi najbližjo pregledno traso, ki ima dovolj prostora za napajalne simbole in oznake.
6. Veje od glavne osi odcepi pravokotno. Elemente iste vrste in enakovredne veje poravnaj na skupne vrstice ali kolone. Praznega dela lista ne zapolnjuj z razmikanjem komponent.

**Pred risanjem žic preveri položaje.** Če bi bila med neposredno povezanima elementoma potrebna dva loma samo zaradi njunega zamika, najprej premakni ali zasukaj element. Preveri tudi povezave tega elementa s sosedi. Izberi postavitev, ki izboljša celoten podsklop.

## 2. Ožičenje naj sledi poravnavi

Pri izbiri med več električno enakovrednimi postavitvami uporabi ta vrstni red:

1. Nedvoumni spoji in prost prostor brez prekrivanja simbolov, besedil ali nepovezanih vodnikov.
2. Jasna smer delovanja in skupne osi povezanih elementov; križanja odpravi s premikom elementa ali cele veje, kadar je to mogoče.
3. Najmanj nepotrebnih sprememb smeri; nato najkrajša pregledna dolžina povezav.
4. Kompaktna, uravnotežena postavitev z enakomernimi razmiki.

Križanje ali nujen zavoj je sprejemljiv, kadar z njim ohraniš jasno ločitev podsklopov ali rešitev brez njega povzroči slabšo postavitev drugje. Velik obvoz okoli vezja ne šteje kot izboljšava samo zato, ker odstrani eno križanje.

- Poravnana priključka poveži z ravno žico. Za povezavo v isti osi uporabi nič lomov, za prehod med dvema osema praviloma en lom. Dva loma potrebujeta prostorski razlog, na primer obhod nepovezanega simbola ali povezavo vzporednih vrstic.
- Žice naj bodo vodoravne ali navpične. Ne dodajaj kratkih stopnic, žepov, vračanja nazaj ali dodatnih vogalov zgolj zaradi izbrane mreže oziroma naključnih koordinat.
- Veja iz stičišča naj takoj potuje v smeri nadaljnje trase. Če najprej naredi kratek odsek v drugo smer in šele nato zavije, prilagodi stičišče ali bližnji element.
- Stičišče postavi na naraven vogal ali na ravni odsek med elementi. Zaradi njegovega odmika ne dodajaj novega zavoja. T-stičišča označi s spojno piko; štirismernim spojem se izogibaj, kadar je na voljo jasnejša rešitev. Nepovezana križanja naj bodo nedvoumna.
- Vsak vodnik zaključi natančno na priključku ali predvidenem stičišču. Vodnik, ki zgolj poteka prek pina, ni dokaz povezave. Odstrani odcepe, ki so ostali po odstranitvi oznake ali simbola in nimajo več namena.
- Pri povratnih povezavah ohrani bližnjo pot ob ojačevalniku. Najprej postavi elemente povratne veje na skupno os, nato poveži njen odcep do vhoda. Ne obkrožaj vhodnih oznak ali neodvisnih podsklopov.

## 3. Razmiki in merilo

Osnovna mrežna enota je **G = 5,08 mm**. Za povezave uporabljaj mrežo **1,27 mm** ali ustrezno finejšo KiCadovo mrežo, kadar to zahteva položaj knjižničnega pina. Koordinate zaokrožuj dosledno, da ne nastanejo skoraj spojeni konci.

| Razdalja | Privzeta postavitev | Vpliv `$SCALE` |
|---|---|---|
| Žica od zunanjega vhoda/izhoda vezja do globalne oznake | 2 G = 10,16 mm, ravno | Vedno 10,16 mm |
| Neposredno povezana sosednja elementa istega podsklopa | Cilj 1 G = 5,08 mm od pina do pina | Množi s `$SCALE` |
| Stičišče do priključka sosednjega elementa | Cilj 1 G | Množi s `$SCALE` |
| Vodnik mimo nepovezane grafike elementa ali napajanja | Cilj 1 G od roba grafike | Množi s `$SCALE` |
| Vzporedni vodniki, na primer podatkovna vodila | Praviloma vsaj 0,5 G | Množi s `$SCALE` |
| Vidna ločitev neodvisnih podsklopov | Orientacijsko 3 G | Množi s `$SCALE` |
| Oznaka do pripadajočega simbola | Približno 0,5 G = 2,54 mm | Se ne spreminja |

Razmiki znotraj podsklopa so ciljne vrednosti. **Ne smejo razbiti skupne osi, ustvariti novega loma ali povečati povratne zanke.** Krajši odsek je dovoljen, če ostane povezava čitljiva in dovolj oddaljena od nepovezanih grafik. Odmik meri od dejanskega priključka oziroma zunanjega roba grafike, ne od središča simbola.

Razmika 3 G ne uporabljaj med elementi enega delilnika, zaporedne veje ali ojačevalnika s povratno zvezo. Kadar je neposredna povezava znotraj podsklopa daljša od 2 G, preveri, ali jo lahko skrajšaš s premikom elementa; daljšo povezavo ohrani zaradi konkretnega prostora za simbol, besedilo ali drugo vejo. Nobena posamezna žica nima zahtevane najmanjše dolžine samo zato, ker je samostojen odsek.

Napajalni simbol lahko priključiš neposredno na pin. Napajalno žico podaljšaj le, če to izboljša preglednost. Velikosti simbolov in pisave ne zmanjšuj zaradi `$SCALE`.

## 4. Oznake in napajanja

- Sheme so praviloma namenjene teoretični razlagi. Prednost imajo funkcionalne oznake, npr. `R_{breme}`, `R_{REF}`, `R_{B}`. Številčene reference `R1`, `R2` prikaži, kadar je vloga elementov trivialna, so potrebne za razlikovanje ali jih zahteva opis. Interne enolične KiCadove reference vedno ohrani; kadar jih ne želiš prikazati, skrij polje Reference in prikaži funkcionalno ime v polju Value. Ne podvajaj iste informacije v dveh vidnih poljih.
- Če opis zahteva reference in vrednosti, prikaži oboje. Oznake postavi neposredno ob pripadajoči simbol, vodoravno in čitljivo; pri vodoravnem uporu praviloma nad simbol, pri navpičnem ob stran. Po zasuku simbola posebej prestavi besedilna polja in preveri njihovo orientacijo v izvozu; kot polja 0° sam po sebi ne zagotavlja vodoravnega prikaza pri zasukanem simbolu. Če se besedili prekrivata, popravi položaj obeh ali bližnjega elementa; ne pošiljaj oznake daleč od njenega simbola.
- **Številke pinov skrij na vseh simbolih.** Definicij in številk v električnem modelu ne odstranjuj. Ohrani pomenske oznake, kot sta + in − pri OZ. Dejanski izvoz mora biti brez vidnih številk pinov.
- Imena signalov začni z veliko tiskano črko in uporabi oblikovan podpis, npr. `U_{C}`, `U_{AM}`, `V_{REF}`. Podpis je lahko z velikimi ali malimi črkami. Uporabi `R_{breme}`, ne `R_breme`. Enačbe sodijo v spremljajoče besedilo.
- Zunanje signale celotnega vezja označi z Global Label: oblika `Input` za vhod, `Output` za izhod. Vhod naj bo levo od vezja, z napisom levo od priključka in priključkom proti desni (praviloma zasuk 180°). Izhod naj bo desno, s priključkom na levi in napisom desno (praviloma zasuk 0°). Preveri obliko in dejansko orientacijo v izvozu. Sam napis ne določa oblike. Označi le dejanske zunanje signale iz opisa; ne dodajaj izhoda brez vsebinskega razloga. Notranja vozlišča označi le izjemoma.
- Uporabljaj knjižnične napajalne simbole in uveljavljena imena `VCC`, `GND`, `VEE`, `V_{REF}`. Izogibaj se zapisom, kot je `V=0`. Pozitivni potencial naj bo zgoraj in njegov simbol usmerjen navzgor; negativni ali nižji potencial spodaj, simbol navzdol. Ime postavi tik ob simbol in po zasuku popravi njegov položaj.
- **Shema nikoli ne sme vsebovati `PWR_FLAG`.** Odstrani ga tudi iz obstoječe sheme ter odstrani njegove nepotrebne slepe odcepe. Dejanske napajalne povezave ohrani.

## 5. Izvedba in datoteke

1. Zapiši povezave po vozliščih: komponente, pine, napajanja in zunanje signale. Pri preurejanju uporabi izhodiščni netlist kot električno izhodišče in ga primerjaj z opisom. Za konkretno integrirano vezje preveri razpored pinov v uradnem podatkovnem listu, če ga še nisi preveril. Ne izmišljaj si vrednosti ali neuporabljenih pinov.
2. Uporabi **KiCad MCP kot prvi način urejanja**. Najprej naloži shemo, preberi priključke in njihove koordinate, nato postavljaj in povezuj. Če nalaganje ali potrebna operacija ni podprta, zabeleži konkretno omejitev in uporabi lokalni KiCad CLI ter previdno urejanje izvorne datoteke. Ne ponavljaj iste neuspešne operacije in ne zavrzi obstoječih knjižničnih definicij. Če neposredno urejaš datoteko, spreminjaj samo potrebne objekte in nato preveri, da jo KiCad pravilno odpre oziroma izvozi.
3. Pred urejanjem žic določi osi in položaje po razdelku 1. Ob premiku simbola preračunaj koordinate vseh njegovih pinov, vključno z napajanji in neuporabljenimi priključki. Pri zasuku preveri identiteto pinov tudi pri simetričnih pasivnih simbolih: električna zamenljivost obeh koncev upora ne pomeni, da je netlist po paru referenca–pin ostal enak. Premakni tudi vezana besedila in oznake No Connect.
4. Shrani `.kicad_sch` na obstoječo oziroma ustrezno pot pod `circ/`. Markdown, slikovno pot in identifikator figure ohrani; spremeni jih le, kadar je to del naloge ali je povezava napačna. Običajna sprememba postavitve ne spreminja vsebine poglavja ali drugih shem.
5. **Med oblikovanjem pripravi samo črno-beli PDF**, osvežuj isto datoteko za ogled v Zathuri. Za vizualni pregled lahko PDF začasno rasteriziraš v `/tmp`; to ni končni PNG za gradivo. SVG in PNG za Markdown pripravi šele po potrditvi postavitve.
6. Pri končnem izvozu naredi črno-beli SVG brez okvirja (`--black-and-white --exclude-drawing-sheet`), nato uporabi `svg2png ime.svg`. Če ukaz ni na voljo, uporabi Inkscape in sliko obreži do sheme z majhnim robom. Upoštevaj zahtevano ozadje; če ni drugače določeno, uporabi belo. Sliki ohrani velikost, primerno za gradivo, in jo kopiraj na obstoječo pot oziroma v `./slike`, če ta mapa obstaja in se tako sklicuje Markdown.

## 6. Pregled pred dostavo

Vizualni in električni pregled izvedi ločeno. Nobeden ne nadomesti drugega.

**Vizualni pregled izvoženega PDF-ja:**

- Ali imajo zaporedni elementi istega podsklopa skupno os po priključkih? Preveri vsako povezano dvojico; LED–upor in upora delilnika ne smeta biti zamaknjena brez razloga.
- Ali smer postavitve pokaže signalni oziroma tokovni potek in pravilno razporedi napajalne potenciale?
- Ali lahko premik ali zasuk enega elementa odpravi nepotreben zavoj? Če lahko, popravi postavitev in znova izvozi PDF.
- Ali so povratna veja, napajanja in njene oznake dovolj blizu ojačevalniku? Ali se veja iz stičišča takoj nadaljuje v pričakovani smeri?
- Ali se elementi, besedila, No Connect oznake in žice prekrivajo? Ali so vsa besedila jasno povezana s svojim simbolom? Ali so pin številke dejansko skrite?
- Ali imata vhod/izhod pravilno obliko Global Label, orientacijo in raven zunanji odsek 10,16 mm?
- Ali ostaja nepotrebna praznina znotraj podsklopa, ki jo lahko zapreš brez izgube preglednosti? Preveri dolge ravne odseke in velike zanke.

**Električni pregled:**

- Izvozi netlist. Pri spremembi postavitve primerjaj skupine povezanih parov `(referenca, pin)` pred in po spremembi, ne zgolj imen vozlišč, ki se lahko samodejno spremenijo. Preveri tudi napajalne simbole in neuporabljene pine. Razliko odpravi ali jo utemelji z izrecno zahtevano spremembo vezja.
- Zaženi ERC in primerjaj z izhodiščem. Odpravi nove nepovezane pine, nepravilne spoje in viseče oznake ali žice.
- Samo `[power_pin_not_driven]` je samodejna izjema za konceptualno zunanje napajanje. Napajalni pini morajo biti kljub temu pravilno povezani; `PWR_FLAG` je vedno prepovedan.
- Druga sporočila presodi posamično. Na primer `[pin_not_driven]` na zunanjem vhodu je lahko posledica tega, da vir ni prikazan; to razloži kot preostalo opozorilo in ne dodajaj izmišljenega gonilnika. Opozoril ne razglasi za odpravljenih samo zato, ker so bila prisotna že prej.

V zaključku navedi popravljeno shemo in pregledni PDF, glavne vizualne spremembe ter rezultat primerjave netlistov in ERC. Povej, ali sta SVG/PNG ostala za končni izvoz.
