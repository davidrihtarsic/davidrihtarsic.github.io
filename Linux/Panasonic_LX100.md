# Panasonic LX100

LX100II ima wgrajen wifi in ga lahko povežemo na telefon ali PC.
Za telefon so na voljo programi na Google trgovini... 

Za PC (Linux, Win in MAC) pa priporočam tole stran [lumix-link-destop](https://github.com/peci1/lumix-link-desktop).

## Koraki za povezavo s PCjem (Linux)

1. Presnameš program iz GitHuba
2. Na LX100II vključiš WiFi (modra lučka mora svetiti)
    1. potrebno je iti od začetka... `+ New connection`
3. S PCjem se povežemo na WiFi omrežje ...
    1. diskonektaš se od domačega roterja

        nmcli connection down Cut2.5G

    2. rescanaš wifi omrežje

        nmcli dev wifi rescan

    3. izpišeš razpoložljiva omrežja

        nmcli dev wifi list

    4. in se povežeš na `LX100M2-F0DAE6`

        nmcli device wifi connect LX100M2-F0DAE6
      > Device 'wlan0' successfully activated with '0b155818-a2e5-4bb9-9efb-cee50d4f171a'.

4. Nato preverimo povezavo:
    http://192.168.54.1/cam.cgi?mode=accctrl&type=req_acc&value=0&value2=Vexia%20Fcs

5. Odpremo stran `Control.html` v našem browserju 
6. in zaženemo java program za pregled streama:

        java -jar StreamViewer.jar 192.168.54.1 16
