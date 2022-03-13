# DISK CLEANING

Pri vzdeževanju Arch linux-a boste s časmo zapolnili kar precej prostora na 
disku, saj si package manager shrani vse posodobitve paketov, za primer,
če bi novejše različice imele kakega hrošča.

Zato je priporočljivo, da večkrat počistimo disk. V ta namen lahko naredite naslednje korake:

## CLEAN PACKAGE CACHE

1. Check disk space:

        du -sh /var/cache/pacman/pkg/

2. Clean not installed pkg:

        sudo pacman -Sc

