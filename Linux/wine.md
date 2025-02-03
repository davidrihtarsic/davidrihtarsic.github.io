# WINE

## Namestitev Acrobat Readed DC

2023-03-20: Namestitev iz AUR je delala namestil sem Acrobat Reader 11

        yay -S adobe-reader-11

## Wine-mono

Imela sem težave, da nisem imel nameščenega pketa `wine-mono` na [ArchWikiju](https://wiki.archlinux.org/title/Wine#Installation) piše,

> Consider installing wine-gecko and wine-mono for applications that depend on Internet Explorer and .NET, respectively.

zato sem namestil še tedva paketa:

    sudo pacman -S wine-mono wine-gecko

in težava se ni pojavila več...

--- 
>tle je pa starejše in mi ni delalo...

Tale link me je rešil:
[Namestitev Acrobat Readerja](https://www.reddit.com/r/archlinux/comments/c88qbc/acrobat_reader_dc_on_wine/)

naredil sem tole, kar predlaga tukaj:

[namestitev fontoc za inputbox](https://askubuntu.com/questions/1238844/adobe-reader-on-wine-not-rendering-text-entry-boxes)

in nato še neka kljukica:

>steps:Launch Reader > Edit > Preferences > Signatures .Under Creation & Appearance > click More > uncheck use modern user interface for signing.... Relaunch Reader and check. Also, try signing another pdf file using certificates and try again.
