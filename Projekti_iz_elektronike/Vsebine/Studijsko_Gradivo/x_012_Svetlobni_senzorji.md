## SVETLOBNI SENZORJI

- delilnik napetosti
- izračun izhodne napetosti

$$ U_i = R_r I_r = R_r \frac{U_c}{R_r + R_{LDR}} $${#eq:izhodna_senzorja}

- pogoji za kompatibilnost s TTL digitalnimi vezji:
    - 0 = {-0.7V .. 0.6V}
    - 1 = [2.6V .. 5.25V]
    - vmesni interval .. ni definiran

- izračunajmo najprimernejši fotoupor:
    1. $U_1 = ...$
    2. $U_2 = ...$
    3. $\Delta U = ...$
    4. $\frac{\partial}{\partial R_r} \Delta U = ... = 0 (maximum)$
    5. $R_r(max \Delta U) = \sqrt{R_1 R_2}$

<!--
v wolframalpha:

- u_1 = r_0 * (u_0 /(r_0 + r_1))
- r_0 * (u_0 /(r_0 + r_1)) - r_0 * (u_0 /(r_0 + r_2))
- derivate(r_0 * (u_0 /(r_0 + r_1)) - r_0 * (u_0 /(r_0 + r_2)),r_0)
- spremeni r_0 v x
- solve(derivate(x * ( u_0 /(x +r_1)))-(x * ( u_0 /(x +r_2))) = 0),x)
-->

- fototranzistor je počasen...
- namesto njega uporabimo:
    - fotodiodo ali
    - fototranzistor (pri fischertechnik kockah)
- fotodiodo vs fototranzizstor
    - glej specifikacije:
        - [fototranzizstor LPT80A](https://search.datasheetcatalog.net/key/LPT80A)
        - [fotodioda BPW34](https://search.datasheetcatalog.net/key/BPW34)

