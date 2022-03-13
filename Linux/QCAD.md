# QCAD

## Nastavitve kotirnih črt

Edit -> Drawing Properties -> Dimension -> Dimension Settings:

Text height: 3.5
Extension line extension: 2
Extension line offset: 0
Dimension line gap: 1.5
Arrow size: 3.5
Dimension line increment: 7

## Nastavitve fontov pri kotah

Za fonte je zelo prepričljivo uporabljat `ISOCPEUR`, ker se debelina
črte spreminja z velikostjo in oblika je usklajena z ISO standardom.

Pri "pro" verziji je to v nastavitvah, pri "free" pa je workaround:

1. označiš koto in
2. ji spremeniš parameter `Label`
3. v okence napišeš: `\fISOCPEUR;<>`
