# QALC

nekaj uporabnih komand:

> Rv := 100 kOhm                      ; store variable
> R1 || R2                            ; vzporedna vezava uporov
> Uii := (Vcc*(Rr||Rv)/((Rr||Rv)+Rn)) ; add function
>   save((Vcc × (Rr or Rv)) / ((Rr or Rv) + Rn), Uii) ≈ 2.539503386 V
> Ui, Uii                             ; izpis vrednosti dveh fun.
>[Ui, Uii] ≈ [2.385083119 V, 2.282987226 V]

> \a^2 + \b^2 = \c^2                  ; uporaba "unknown" spremenljivk \a
>
> U1 := "R1" * "Ucc"/("R1"+"Rn1")     ; neznana spremenljivka je tudi "R1"
> U2 := "R1" * "Ucc"/("R1"+"Rn2")     ; U2  pa je znana, sicer sestavljena iz nezanaih spremenljivk
> Ud=U1-U2
> diff(Ud;"R1")                         ;odvajaj funkcijo Ud po R1
> solve(diff(Ud;"R1")=0)
> solve(diff(Ud, R1) = 0) = [√(Rn1 × Rn2), −√(Rn1 × Rn2)]
