# SimulIDE

![SimulIDE](https://1.bp.blogspot.com/-g0PfHcs2isw/XtlQcrj8DVI/AAAAAAAABRo/slmqFRdR6AA6sNNF59r1-NTUvEodcPH8gCLcBGAsYHQ/s1600/circuit.gif)

## Kako dodati simbol nekega integriranega vezja (čipa)

... si poglejte v videu na [tej povezavi](https://youtu.be/E40qK870Df4)  
Pomembno je, da imate datoteko shranjeno poleg datoteke čipa:  
- Linux: /usr/share/simulide/data...

Na primer: Če želimo dodati simbol za krmilnik Arduino UNO:
1. presnemite spodnjo datoteko `Uno_LS.package`
2. in dodajte v `/usr/share/simulide/data/arduino/Uno/`

## Nastavitve SimulIDE za delo s krmilnikom Arduino UNO (za Windows)

1. Namestite ArduinoIDE ... Najverjetneje se bo program namestil v:

        C:/Program Files x86/Arduino

2. Odprite SimulIDE in na vašo delovno površino dodajte krmilnik ArduinoNANO in
shranite projekt v svojo mapo npr:

        .../MyDocuments/SimulIDE_projects/First_project/Nano_test.sim1

3. V desnem oknu odprite novo datoteko in jo shranite skupaj z datoteko projekta:

        .../MyDocuments/SimulIDE_projects/First_project/Nano_blink.ino

4. Nastavite `Set Compiler Path` na mapo, kjer imate nameščen program ArduinoIDE

## Programiranje krmilnikov s firmware datoteko *.hex

... opazili smo, da na Windows op. sistemu nastavitve prevajalnika ne delujejo... zato 
norate na krmilink naložiti strojno kodo, ki ima končnico *.hex :

1. V ArduinoIDE nastavite prikazovenje prevanja kode:
    `File -> Preferences -> Show verbouse output during [x] compile`
2. ...napišite program in kliknite prevajanje kode:
    `Verify`
3. V spodnjem izpisu poiščite kam se je shranila strojna koda s končnic `.hex`

> Users\\UPORAB1\\AppData\\Local\\Temp\\arduino_build_891007/Blink.ino.elf" "C:\\Users\\UPORAB1\\AppData\\Local\\Temp\\arduino_build_891007\\sketch\\Blink.ino.cpp.o" "C:\\Users\\UPORAB1\\AppData\\Local\\Temp\\arduino_build_891007/..\\arduino_cache_832922\\core\\core_arduino_avr_uno_f3ee616dfd432525919d4991c3c967f5.a" "-LC:\\Users\\UPORAB1\\AppData\\Local\\Temp\\arduino_build_891007" -lm "C:\\Users\\uporabnik\\Downloads\\arduino-1.8.19-windows\\arduino-1.8.19\\hardware\\tools\\avr/bin/avr-objcopy" -O ihex -j .eeprom --set-section-flags=.eeprom=alloc,load --no-change-warnings --change-section-lma .eeprom=0 "C:\\Users\\UPORAB1\\AppData\\Local\\Temp\\arduino_build_891007/Blink.ino.elf" "C:\\Users\\UPORAB~1\\AppData\\Local\\Temp\\arduino_build_891007/Blink.ino.eep" "C:\\Users\\uporabnik\\Downloads\\arduino-1.8.19-windows\\arduino-1.8.19\\hardware\\tools\\avr/bin/avr-objcopy" -O ihex -R .eeprom "C:\\Users\\UPORAB1\\AppData\\Local\\Temp\\arduino_build_891007/Blink.ino.elf" "C:\\Users\\UPORAB1\\AppData\\Local\\Temp\\arduino_build_891007/Blink.ino.hex" "C:\\Users\\uporabnik\\Downloads\\arduino-1.8.19-windows\\arduino-1.8.19\\hardware\\tools\\avr/bin/avr-size" -A "C:\\Users\\UPORAB1\\AppData\\Local\\Temp\\arduino_build_891007/Blink.ino.elf"

...npr.: `C:\\Users\\UPORAB~1\\AppData\\Local\\Temp\\arduino_build_891007/Blink.ino.hex`

4. Nato odprite SimulIDE, dodajte krmilnik Arduino uno in sestavite vezje... Z desnim miškinim
    gubom kliknite na krmilnik in izberite `Load Firmware`.

5. V iskalno polje prilepite pot do vaše datoteke (brez imena datoteke in brez dvojnih `\\`) 
    npr.: `C:\Users\UPORAB~1\AppData\Local\Temp\arduino_build_891007`... ter izberite datoteko s
    končnico `.hex` (npr.: `Blink.ino.hex`)

6. Preskusite simulacijo in po potrebi preoblikujte programsko kodo v ArduinoIDE programu.
    Program ponovno prevedite v strojno kodo (`Verify`) in

7. v SimulIDE iz menija krmilnika ponovno izberite `Reload Firmware`.

<!--

1. Presnemite si [ArduinoIDE 1.8.19](https://downloads.arduino.cc/arduino-1.8.19-windows.zip) ... npr v 
2. nato razpakirajte zip arhiv v poljubno mapo npr.: Downloads\Arduino1.8\
3. in zaženite ArduinoIDE.
4. Odprite nek osnovni primer programa npr.: `File -> Examples -> 01.Basics -> Blink`
5. in ga shranite kot svoj projekt npr.: \

-->

## Nastavitev prevajalnika za Linux

Ker uporabljam ArchLinux in je v tem primeru program ArduinoIDE nameščen nekoliko drugače,
sem moral ponovno download-ati ArduinoIDE program in ga razpakirati v nek directory:

    /opt/arduino-1.8.19

... v tem directory-u je vse potrebno, kar program SimulIDE potrebuje.

Na to lahko v programu SimulIDE nastavimo (desni klik na zavihek programa) `Set Compiler Path`.

## SimulIDE elementi

- [Uno_LS.package](./SimulIDE/Uno_LS.package) - Arduino UNO simbol

