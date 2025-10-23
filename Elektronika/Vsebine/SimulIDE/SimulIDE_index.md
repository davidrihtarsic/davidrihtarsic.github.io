# [ELEKTRONIKA](../index) ↪ SimulIDE

[🏡DOMOV](../../index){: .btn}
[📝VSEBINE](../../Vsebine/index.md){: .btn}
[👨‍🎓INFO](../../info){: .btn}
[💾PRESNEMI](../../Presnemi/index){: .btn}

---

![SimulIDE](https://1.bp.blogspot.com/-g0PfHcs2isw/XtlQcrj8DVI/AAAAAAAABRo/slmqFRdR6AA6sNNF59r1-NTUvEodcPH8gCLcBGAsYHQ/s1600/circuit.gif)

## Kako dodati simbol nekega integriranega vezja (čipa)

... si poglejte v videu na [tej povezavi](https://youtu.be/E40qK870Df4)  
Pomembno je, da imate datoteko shranjeno poleg datoteke čipa:  
- Linux: /usr/share/simulide/data...

Na primer: Če želimo dodati simbol za krmilnik Arduino UNO:
1. presnemite spodnjo datoteko `Uno_LS.package`
2. in dodajte v `/usr/share/simulide/data/arduino/Uno/`

## Nastavitev prevajalnika za Linux

Ker uporabljam ArchLinux in je v tem primeru program ArduinoIDE nameščen nekoliko drugače,
sem moral ponovno download-ati ArduinoIDE program in ga razpakirati v nek directory:

    ~/.local/build/arduino-1.8.19

... v tem directory-u je vse potrebno, kar program SimulIDE potrebuje.

Na to lahko v programu SimulIDE nastavimo (desni klik na zavihek programa) `Set Compiler Path`.

## SimulIDE elementi

- [Uno_LS.package](./Uno_LS.package) - Arduino UNO simbol

