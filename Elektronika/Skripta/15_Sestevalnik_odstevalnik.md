## SEŠTEVALNI IN ODŠTEVALNI SISTEMI Z OPERACIJSKIM OJAČEVALNIKOM

Z operacijskimi ojačevalnimi sistemi lahko napetostne signale tudi logaritmiramo, integriramo, odvajamo, itd. Izvedemo lahko celo kako drugo matematično funkcijo, ki vključuje celo več napetostnih signalov, kot na primer: seštevanje, odštevanje, množenje ... Prednost takih sistemov pred programirljivo elektroniko je predvsem v hitrosti izvršene operacije, pri čemer ne potrebujemo žrtvovati procesorskega časa.

PRIMER REGULACIJE TEMPERATURE V AVTOMOBILU:  
Skoraj vsak današnji avtomobil ima v prostoru za potnike razporejenih več temperaturnih senzorjev. Najbolj pogosta lokacija njih je: v armaturni plošči, v stropnem delu poleg stropne osvetlitve in v prezračevalni konzoli za zadnjo klop. Torej vsaj trije senzorji merijo temperaturo prostora. Tako mora regulacijska tehnika upoštevati vrednosti vseh senzorjev.

> ### NALOGA: SEŠTEVALNI SISTEM
> Skonstruirajte vezje, ki bo izračunalo povprečno vrednost 3-h senzorjev temperature (npr.: v avtomobilski kabini). Prenosna funkcija tega vezja mora ustrezati [@eq:povprecje_T]  
> $$ U_2 = \frac{1}{3} (U_{T_1}+U_{T_2}+U_{T_3}). $${#eq:povprecje_T}
> Izmerite nekaj vzorčnih primerov meritev, s katerimi lahko pokažete zanesljivo delovanje predlagane rešitve.Meritve vpišite v [@tbl:meritve_sestevalnega_sistema ].

| No.# | $U_{T_1}[V]$ | $U_{T_2}[V]$ | $U_{T_3}[V]$ | $U_2[V]$ |
|:----:|:------------:|:------------:|:------------:|:--------:|
|   1  |              |              |              |          |
|   2  |              |              |              |          |
|   3  |              |              |              |          |
|   4  |              |              |              |          |
|   5  |              |              |              |          |
Table: Primeri meritev seštevalnega sistema. {#tbl:meritve_sestevalnega_sistema}

PRIMER MERJENJA POSAMEZNIH LI-ION AKUMULATORSKIH CELIC  
Pri polnjenju Li-Ion akumulatorjev je priporočljivo spremljati napetost vsake celice posebej. Ker je za regulacijo polnjenja zadolžena elektronika taki regulacijski sestavi vsebujejo vezje, ki odšteje napetostna potenciala na vsaki strani akumulatorske celice in tako dobimo napetost na njej. Na primer, če je akumulator sestavljen iz 3-h zaporedno vezanih celic (t.i. razporeditev vezave 3S) nam to vezje lahko prikazuje napetost vsake celice posebej.

> ### NALOGA: ODŠTEVALNI SISTEM
> Skonstruirajte vezje, ki bo merilo napetosti posamezne akumulatorske celice v katerem so zaporedno vezane tri celice - 3S. Vezje naj ima 4 vhodne priključke $U_{S_x}$ (GND, S1, S2 in S3) in 3 izhodne priključke $U_{S_y}$ na katerih lahko izmerimo napetostni potencial, ki ustreza napetosti posamezne celice. Torej napetosti na celici S1, napetost na S2 in S3.
> Izmerite nekaj vzorčnih primerov meritev, s katerimi lahko pokažete zanesljivo delovanje predlagane rešitve.Meritve vpišite v [@tbl:meritve_sestevalnega_sistema ].

| $S_x$ | $U_{S_x}[V]$ | $U_{S_y}[V]$ |
|:-----:|:------------:|:------------:|
|   1   |              |              |
|   2   |              |              |
|   3   |              |              |
Table: Meritve napetosti akumulatorskih celic. {#tbl:meritve_odstevalnega_sistema}

