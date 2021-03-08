# HIBERNATION
Na archu mi ni delalo, ker v :
        /etc/mkinitcpio.conf
ni bilo napisano "resume" :

        HOOKS=(base udev autodetect keyboard modconf block filesystems resume fsck)

navodila: so tu:

https://www.reddit.com/r/linuxquestions/comments/7swvyb/etc/default/grub/cannot_restore_session_after_hibernation/?utm_source=reddit-android

https://wiki.arhttps://www.reddit.com/r/linuxquestions/comments/7swvyb/cannot_restore_session_after_hibernation/?utm_source=reddit-androidchlinux.org/index.php/Power_management/Suspend_and_hibernate#Hibernation

ko to urediš moraš skompajlirat GRUB in linux????.img

        sudo grub-mkconfig -o /boot/grub/grub.cfg
        sudo mkinitcpio -c /etc/mkinitcpio.conf -g /boot/initramfs-linux-lts.img

## skratka:

    lsblk

    NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
    sda      8:0    0 238.5G  0 disk 
    ├─sda1   8:1    0   512M  0 part /boot
    ├─sda2   8:2    0   218G  0 part /
    └─sda3   8:3    0    20G  0 part 
    sdb      8:16   0 256.2G  0 disk 
    ├─sdb1   8:17   0 236.2G  0 part /home
    └─sdb2   8:18   0    20G  0 part [SWAP]

da dobiš na kateri partuvuju je **SWAP** -> /dev/sdb2
nato pridobiš **UUID**

    ls -l /dev/disk/by-uuid/
    lrwxrwxrwx 1 root root 10 Jan 14 03:24 91e9d10f-75f0-4790-a13a-fc8d6f67b4d7 -> ../../sdb2

nato v datoteko:

    /etc/mkinitcpio.conf

dodaš resume

    HOOKS=(base udev autodetect modconf block  filesystems shutdown keyboard resume fsck)

in zbildaš nov linux image

    sudo mkinitcpio -c /etc/mkinitcpio.conf -g /boot/initramfs-linux-lts.img

nato popraviš še v  filju:
    
    /etc/default/grub

in dodoap UUID od SWAP particije:

    GRUB_CMDLINE_LINUX_DEFAULT="resume=UUID=91e9d10f-75f0-4790-a13a-fc8d6f67b4d7"

in zbildaš še grub:

    sudo grub-mkconfig -o /boot/grub/grub.cfg

rebootaš in HIBERNATION dela

This guide is based on the hibernate article from the Arch wiki.

edit /etc/default/grub and add resume as well as resume_offset kernel parameters
resume=UUID=abcd-efgh contains the UUID of the partition on which the swapfile resides. In most cases the swapfile resides in root, to identify the root parition's UUID run blkid or lsblk -O.
resume_offset=1234 is the offset of the swapfile from the partition start. The offset is the first entry in the physical_offset column of the output of filefrag -v /swapfile.
update grub: grub-mkconfig -o /boot/grub/grub.cfg
example: GRUB_CMDLINE_LINUX_DEFAULT="resume=UUID=75972c96-f909-4419-aba4-80c1b74bd605 resume_offset=1492992"
add the resume module hook to /etc/mkinitcpio.conf:
HOOKS="base udev resume autodetect ...
rebuild the initramfs mkinitcpio -p linux
check if everything works: systemctl hibernate

## HIBERNATION in SWAP-FILE

kje je swap file (na katerem disku) na root particiji

    >lsblk
    NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
    sda      8:0    0 238.5G  0 disk 
    ├─sda1   8:1    0   512M  0 part /boot
    └─sda2   8:2    0   238G  0 part /
    sdb      8:16   0 256.2G  0 disk 
    └─sdb1   8:17   0 256.2G  0 part /home/david/Files

in kolk je zamaknjen:

    >sudo filefrag -v /swapfile

    Filesystem type is: ef53
    File size of /swapfile is 19327352832 (4718592 blocks of 4096 bytes)
     ext:     logical_offset:        physical_offset: length:   expected: flags:
       0:        0..       0:      34816..     34816:      1:            
       1:        1..   30719:      34817..     65535:  30719:             unwritten

pomembna je prva številka '34816' (56727552..)
Nato dodaš resume v:

    > sudo nvim /etc/mkinitcpio.conf
    HOOKS=(base udev resume autodetect modconf block filesystems keyboard fsck)

in zbildaš LINUX IMAGE

    sudo mkinitcpio -c /etc/mkinitcpio.conf -g /boot/initramfs-linux.img

Nato dodaš še kernel parametre v GRUB, da jih pošle v kernel:

    > sudo nvim /etc/default/grub
    GRUB_CMDLINE_LINUX_DEFAULT="resume=/dev/sda2 resume_offset=34816"

Rebootaš in Hibernation DELA! :)

