# CALCURSE


## Uporaba v terminalu:

Izpis obveznosti za naslednje 3 dni:

    calcurse -Q --days 3


## Namestitev in povezava z Googlom

1. inštelirano moraš imeti:

    pip3 install --user python-oauth2client

2. Glej [navodila](https://calcurse.org/files/calcurse-caldav.html)

        calcurse-caldav --init two-way

    ...te preusmeri na URL... kjer se strinjaš, da lahko
    Calcurse dostopa do googla...
    in ti da en link:

        http://localhost/?code=neka_koda_ki_jo_moraš_skopirati

3. in še enkrat zaženeš komando:

        calcurse-caldav --init two-way --authcode 'neka_koda_ki_jo_moraš_skopirati'

