## PACMAN
Package manager za ARCH. Nekaj splo/nih ukazov:

|             Akcija | ukaz                                                           |
|-------------------:|----------------------------------------------------------------|
|        inštalacija | `sudo pacman -S ime_programa`                                  |
|           odstrani | `sudo pacman -Rns ime_programa`                                |
|          downgrade | `sudo pacman -U /var/cache/pacman/pkg/ime_programa.pkg.tar.xz` |
| installed pkg info | `pacman -Q --info ime_programa`                                |
|    remote pkg info | `pacman -S --info ime_programa`                                |
| reinstall all pkgs | `pacman -Syyu`                                                 |
|   find missing pkg | `sudo pacman -Fy ime_paketa_ali_fila`                          |

Nastavitev pacmana najdeš v datoteki: `/etc/pacman.conf`.

Direktorij kjer lahko najdeš vse pakete za nazaj pa imamo v  

    /var/cache/pacman/pkg

### TROUBLESHOOTING

> error while loading shared libraries: libpoppler.so.111: cannot open shared object file

Imamo lahko dve rešitvi:
1. da knjižnico "polinkamo" na novejšo naloženo knjižnico. Naprimer knjižnice so shranjene v:

        >ls /usr/lib

>/usr/lib/libpoppler-cpp.so          /usr/lib/libpoppler-qt5.so         /usr/lib/libpoppler.so.117
>/usr/lib/libpoppler-cpp.so.0        /usr/lib/libpoppler-qt5.so.1       /usr/lib/libpoppler.so.117.0.0
>/usr/lib/libpoppler-cpp.so.0.9.0    /usr/lib/libpoppler-qt5.so.1.29.0  /usr/lib/libpopt.a

in maredimo link:

        >sudo ln -s libpoppler.so.117 libpoppler.so.111

Vendar to ni vedno dobra ideja, lahko da so novejše knjižnice nekoliko spremenjene, in niso kompatibilne za nazaj.

2. Včasih so nekatere knjižnice inštalirane v:

        >ls /usr/local/lib

in jih lahko enostavno skopiramo v pravi direktorji:

        >sudo cp /usr/local/lib/* /usr/lib

#### Install RPM pacgage

Glej [install RPM](./prm_install.md)

### Cannot update packages: signature is unknown trust

Ker ne naredim `update` zelo pogosto, se zgodi, da pacman prepozna nekatere pakete kot nepravilne...
Rešitev je bila, da sem "zbrisal" `/etc/pacman.d/gnupg` direktorij (v bistvu sem ga najprej preimenoval in
šele na to zbrisal) in ponovno preveril ključe:

    pacman-key --init
    pacman-key --populate

Taka so navodila tudi na [ArchWiki](https://wiki.archlinux.org/title/Pacman/Package_signing#Resetting_all_the_keys) strani.
