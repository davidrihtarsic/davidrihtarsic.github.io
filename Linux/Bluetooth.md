# Bluetooth

Ker uporabljam 'Blueberry' nisem mogel sprejemati file-ov preko BTja. Blueberry ne podpira ravno najbolje OBEX (OBject EXchange) zato je najbolje, da v Blueberry settings:

1. izključiš opcijo: `Receving files from remote device` in
2. štartaš svojega

        bt-obex -y -s "/home/david/Downloads"

... razmišljam, da bi to funkcionalnost dodal v `Ranger` in bi odprl OBEX agenta v tisti directory v katerem se nahajaš...
mogoče najprej pogledam če bt-obex laufa in ga kill-aš, nato pa poženeš bt-obex... ja bo treba eno skriptico...
