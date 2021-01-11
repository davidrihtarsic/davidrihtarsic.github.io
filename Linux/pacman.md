## PACMAN
Package manager za ARCH. Nekaj splo/nih ukazov:

|             Akcija | ukaz                                                           |
|-------------------:|----------------------------------------------------------------|
|        inštalacija | `sudo pacman -S ime_programa`                                  |
|           odstrani | `sudo pacman -Rns ime_programa`                                |
|          downgrade | `sudo pacman -U /var/cache/pacman/pkg/ime_programa.pkg.tar.xz` |
| installed pkg info | `pacman -Q --info ime_programa`                                |

Nastavitev pacmana najdeš v datoteki: `/etc/pacman.conf`.

Direktorij kjer lahko najdeš vse pakete za nazaj pa imamo v  

    /var/cache/pacman/pkg

### TROUBLESHOOTING

