# QALC

nekaj uporabnih komand:

> Rv := 100 kOhm                      ; store variable
> R1 || R2                            ; vzporedna vezava uporov
> Uii := (Vcc*(Rr||Rv)/((Rr||Rv)+Rn)) ; add function
>   save((Vcc × (Rr or Rv)) / ((Rr or Rv) + Rn), Uii) ≈ 2.539503386 V
> Ui, Uii                             ; izpis vrednosti dveh fun.
>   [Ui, Uii] ≈ [2.385083119 V, 2.282987226 V]
