# OPERACIJSKI OJAČEVALNIK

Tranzistorje smo v preteklosti uporabljali kot ojačevalnike ali celo v nekih bolj kompleksnih krmilnih elementih. Te funkcije danes pretežno opravljamo z integriranimi vezji kot so operacijski ojačevalniki, ker so precej bolj enostavni za uporabo. Z uporabo operacijskega ojačevalnika in le nekaj dodatnih elementov lahko z njimi sestavimo vrsto različnih vezij, kot so različni ojačevalniki, pretvorniki, sita, seštevalniki, odštevalniki množilniki itd.

## KOMPARATOR NAPETOSTI

Najbolj preprosta vezava operacijskega ojačevalnika je komparator napetosti. To vezje primerja vhodni napetosti. Torej napetosti, ki sta na invertirajočem (označen z "-") in neinvertirajočem (označen s "+") priključku komparatorja. Če je napetost na neinvertirajočem vhodu večja, bo vezje na izhodnem opiključku imelo najvišji možen napetostni potencial - **zgornje nasičenje**. Če pa je situacija obratna torej, da je na invertirajočem vhodu večja napetost, pa bo vezje imelo na izhodu **spodnje nasičenje**.

**NAPAJANJE OPERACIJSKIH OJAČEVALNIKOV**

Pri tako enostavnih vezjih navadno lahko uporabljamo kar baterijsko napajanje (9V ali 4.5V), vendar moramo biti pri operacijskih ojačevalnikih bolj pozorni. V taki situaciji (uni- polarno napajanje = le dva potenciala eden za 9v in drugi za 0 V) lahko uporabljamo z o.o. z oznako 358 ali temu podobnimi. Operacijski ojačevalnik z oznako 741 pa lahko delujejo tudi z bipolarnim napajanjem (npr.: +5V , -5V in 0V). Napajalnih napetostnih potencialov pogosto v električne sheme ne rišemo, saj so načeloma določene in bi zmanjševale preglednost shem.

**IZHODNA NAPETOST PRI KOMPARATORJU NAPETOSTI**

Izhodna napetost komparatoja je vedno v enem nasičenju (v zgornjem ali spodnjem). To pomeni, da je izhodna napetost odvisna od napajalne napetosti. Omeniti pa moramo, da se o.o. razlikujejo tudi v tej lastnosti, saj nekateri od njih lahko izhodno napetost (=nasičenje) čisto približajo napajalni napetosti; medtem, ko je pri drugih le-ta lahko različna tudi do 1.5 V.

> ### NALOGA: VKLOP ŽARNICE  
> Sestavite elektronsko vezje, ki bo vključilo žarnico, ko bomo na to vezje posvetili z drugim svetlobnim telesom. Tako vezje bo delovalo kot navadna sveča, ki jo moramo prižgati z vžigalico. To vezje lahko razdelimo na štiri osnovne sestavne dele, ki jih najdete v regulacijskih vezjih:  
> 1. Senzorski del: v katerem imamo senzor osvetljenosti za detekcijo tujega svetlobnega telesa.  
> 2. Nastavitveni člen: s katerim nastavimo referenčno napetost na katero se ozira primerjalna logična enota.  
> 3. Komparator napetosti: ki bo primerjal napetost senzorja z napetostjo nastavitvenega člena.  
> 4. Močnostna elektronika: ki bo na podlagi izhodnega napetostnega potenciala komparatorja poskrbela za vklop žarnice.  
>  
> Vsak sestavni del najprej načrtujte in ga nato realizirajte v fizični obliki. Narišite sheme vsakega sestavnega dela posebej, ga preizkusite in povežite v celoto.
