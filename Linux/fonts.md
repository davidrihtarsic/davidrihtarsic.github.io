# FONTS

List all fonts installed:

    fc-list
    fc-list | more
    fc-list | grep Hermit

naprimer za zadnji ukaz dobiš tale ozpis:

    /usr/share/fonts/OTF/Hermit-Light.otf: Hermit,Hermit Light:style=Light,Regular
    /usr/share/fonts/OTF/Hermit-BoldItalic.otf: Hermit:style=BoldItalic
    /usr/share/fonts/OTF/Hermit-Bold.otf: Hermit:style=Bold
    /usr/share/fonts/OTF/Hermit-RegularItalic.otf: Hermit:style=RegularItalic,Italic
    /usr/share/fonts/OTF/Hermit-LightItalic.otf: Hermit,Hermit LightItalic:style=LightItalic,Regular
    /usr/share/fonts/OTF/Hermit-Regular.otf: Hermit:style=Regular

**BOLD 123 0 O mn t**  to pa ni bold
_ITALIC_ to naj bi bilo italic

```cpp
int i=0;
  digitalWrite(4,HIGH);
```

## CONSOLE(tty) FONTS

fonti za tty terminal se nahajajo v 

        /usr/share/kbd/consolefonts/

da imajo foti tudi slovenske znake morajo biti mapirane po sistemu

- ISO 8859-2
- ISO 8859-16
- ISO 16

v mojem primeru je ok, če imam

        ter-220.psf.gz
        ter-g20.psf.gz

fonte lahko nastavimo:

    setfonts ter-220.psf.gz

za permnentno nastavite fontov v konzoli pa uredite file:

    /etc/vconsole.conf

>KEYMAP=slovene
>FONT=ter-220

Fonti se nahajajo v AUR odložišču v paketu

    terminus-fonts
