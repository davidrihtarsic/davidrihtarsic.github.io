# ENOSMERNI MOTOR

Navor enosmernega motorja je premo sorazmeren s tokom skozi navitje motorja in ga lahko predstavimo z [@eq:k_t_equation]:

$$ M = k_T I, $${#eq:k_t_equation}

kjer je M navor na gredi motorja, I tok skoz navitje motorja in $k_T$ konstanta motorja, ki podaja razmerje med navorom in tokom. Prav tako je premo sorazmerna povezava med vrtilno hitrostjo gredi motorja in inducirano napetostjo, ki se pojavi na navitju. To razmerje podaja [@eq:omega_uind]

$$ \omega = \frac{U_i}{k_V},$${#eq:omega_uind}

kjer je $\omega$ vrtilna hitrost (v rad/s), $U_i$ inducirana napetost in $k_V$ ta konstanta. Izkaže se, da sta konstanti $k_T$ in $k_V$ identični, a jih proizvajalci pogosto podajajo ločeno zaradi namena in praktičnosti uporabe [@DC_tech_data].

V teoretičnih opisih delovanja enosmernega motorja pa sta ti dve konstanti predstavljeni z [@eq:konstanta_motorja]

$$ k_T = k_V = k_M \Phi_m,$${#eq:konstanta_motorja}

kjer je $k_M$ - konstanta motorja, $\Phi_m$ pa magnetni pretok skozi zanke navitja. Če poznamo konstanto $k_T$ lahko izračunamo konstanto motorja $k_M$ po [@eq:km]

$$k_M = \frac{k_T}{\sqrt{R_n}},$${#eq:km}

kjer je $R_n$ omska upornost navitja.

## KONSTANTA MOTORJA

> ### NALOGA: KONSTANTA MOTORJA  
> Za več različnih DC motorjev izmerite potrebne meritve, da boste lahko določili konstanto motorja $k_M$. Potrebne meritve vpišite v [@tbl:k_motorja ] in jih označite z \* tako, da se bodo izmerjene vrednosti ločile od izračunanih. Račune tudi nakažite vsaj za en primer motorja.

|                       | DC Motor 1 | DC Motor 2 | DC Motor 3 |
|:----------------------|:----------:|------------|------------|
| opis motorja ->       |            |            |            |
| $R_n[\Omega]$         |            |            |            |
| $U_0[V]$              |            |            |            |
| $I_R[A]$              |            |            |            |
| $[vrt/min]$           |            |            |            |
| $\omega[rd/s]$        |            |            |            |
| $I_0[A]$              |            |            |            |
| $k_V[\frac{V}{rd/s}]$ |            |            |            |
| $k_T[\frac{Nm}{A}]$   |            |            |            |
| $M[Nm]$               |            |            |            |
| $k_M[Nm/sqrt{W}]$     |            |            |            |
| $P_M[W]$              |            |            |            |
| $P_E[W]$              |            |            |            |
| $\eta[\%]$            |            |            |            |
Table: Meritve osnovnih karakteristik motorja. {#tbl:k_motorja}

Pri meritvah in izračunu naj vam bodo v pomoč enačbe v študijskem gradivu Elektrotehnika [@Koci_ElektroTehnika]
