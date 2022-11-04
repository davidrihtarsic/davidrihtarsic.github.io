2 Disk partitioning

V bistvu imam dve particji

1. sda1 = boot
2. sda2 = root =/

nato pa še en disk sdb mauntam v Files. Tam imam shranjene vse moje pomembnejše datoteke... mogoče bi bilo bolje, da bi imel cel /home na svojem disku... ker sedaj ne vem kako bo s ključnimi datotekami kot so: .zshenv, .xprofile...

skratka izgleda takole:

    NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
    sda      8:0    0 238.5G  0 disk 
    ├─sda1   8:1    0   512M  0 part /boot
    └─sda2   8:2    0   238G  0 part /
    sdb      8:16   0 256.2G  0 disk 
    └─sdb1   8:17   0 256.2G  0 part /home/david/Files

## Format USB device

    sudo fdisk /dev/sdc

> Welcome to fdisk (util-linux 2.38.1).
> Changes will remain in memory only, until you decide to write them.
> Be careful before using the write command.
> 
> The device contains 'vfat' signature and it will be removed by a write command. See fdisk(8) man page and --wipe option for more details.

    Command (m for help): p

> Disk /dev/sdc: 14.89 GiB, 15987638272 bytes, 31225856 sectors
> Disk model: Storage Device
> Units: sectors of 1 * 512 = 512 bytes
> Sector size (logical/physical): 512 bytes / 512 bytes
> I/O size (minimum/optimal): 512 bytes / 512 bytes
> Disklabel type: dos
> Disk identifier: 0x00000000

    Command (m for help): n

> Partition type
>    p   primary (0 primary, 0 extended, 4 free)
>    e   extended (container for logical partitions)
> Select (default p):
> 
> Using default response p.
> Partition number (1-4, default 1):
> First sector (2048-31225855, default 2048):
> Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-31225855, default 31225855):
> 
> Created a new partition 1 of type 'Linux' and of size 14.9 GiB.

    Command (m for help): p

>Disk /dev/sdc: 14.89 GiB, 15987638272 bytes, 31225856 sectors
>Disk model: Storage Device
>Units: sectors of 1 * 512 = 512 bytes
>Sector size (logical/physical): 512 bytes / 512 bytes
>I/O size (minimum/optimal): 512 bytes / 512 bytes
>Disklabel type: dos
>Disk identifier: 0x00000000
>
>Device     Boot Start      End  Sectors  Size Id Type
>/dev/sdc1        2048 31225855 31223808 14.9G 83 Linux

    Command (m for help): w

> The partition table has been altered.
> Calling ioctl() to re-read partition table.
> Syncing disks.

    Command (m for help): q

    lsblk

>NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
>sda      8:0    0 238.5G  0 disk
>├─sda1   8:1    0   512M  0 part /boot
>└─sda2   8:2    0   238G  0 part /
>sdb      8:16   0 256.2G  0 disk
>└─sdb1   8:17   0 256.2G  0 part /home/david/Files
>sdc      8:32   1  14.9G  0 disk
>└─sdc1   8:33   1  14.9G  0 part

    sudo mkfs.vfat -F 32 /dev/sdc1

> mkfs.fat 4.2 (2021-01-31)

## UREJENOST DIRECTORY-EV

### Potovanja

Uredi potovanja po posameznih potovanjih npr.: `2022_10-STE22_Porto`
in v ta dir. dodaš vse elemente, ki temu dogodku pripadajo.

>2022_NOVO_POTOVANJE
>├── 01_Voga_za_odobritev_odsotnosti
>│   └── 01_<++>—Vloga_za_odobritev_odsotnosti_Rihtaršič_<++>.pdf
>├── 02_Povpraševanje_Nakup_Letalska
>│   ├── 02_Besedilo-maila.md
>│   └── 02_Povprasevanja_za_nakup_letalskih_kart_2021.pdf
>├── 03_Predlog_za_izdajo_naročilnice
>│   └── 03_ePDF_predlog_za_izdajo_narocilnice_2020-v1.71N__nezascitena_polja_.pdf
>├── 04_Poročilo_in_priloge
>│   ├── 04_Poročilo_in_priloge.md
>│   └── 04_Poročilo_in_priloge.pdf
>└── 05_Obračun_potnega_naloga

Dilema je bila ali naj bodo dir. urejeni tako, da so vsi: vloge,
povpraševanja, naročilnice, ... skupaj, saj se lahko potem hitro
copy-paste in spremeniš za drugo situacijo... Vendar težava nastane,
ko imaš na neki poti nestandarden postopek npr.: preklic letalske
karte, odpoved poti...

