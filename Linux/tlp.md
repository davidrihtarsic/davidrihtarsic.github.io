# TLP

[TLP](https://linrunner.de/tlp/index.html) je zelo dober program upravljanja
z zmogljivostjo prenosnika in porabo električne energije. Omogoča tudi raznovrstne
nastavitve, ki jih lahko nastavimo v datoteki:

    /etc/tlp.conf

Dobre informacije lahko najdete rudi v [ArchWiki](https://wiki.archlinux.org/title/TLP) 
dokumentaciji.

## Namestitev

Za namestitev moramo narediti naslednje

    sudo pacman -S --noconfirm --needed tlp tlp-rdw
    sudo systemctl enable tlp.service
    sudo systemctl start tlp-sleep.service
    sudo systemctl mask systemd-rfkill.service
    sudo systemctl mask systemd-rfkill.socket

## Ukazi

Ročno vsiljevanje načina delovanja:

    sudo tlp ac
    sudo tlp bat

Status temperature CPU-ja

    sudo tlp-stat -t

Status trenutne konfiguracije:

    sudo tlp-stat -c
