# SWAP & HIBERNATION

Za hibernation rabiš swap file... ali swap particijo...

## SWAP FILE SETUP

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

pomembna je prva številka '34816'
Nato dodaš resume v:

    > sudo nvim /etc/mkinitcpio.conf
    HOOKS=(base udev resume autodetect modconf block filesystems keyboard fsck)

in zbildaš LINUX IMAGE

    sudo mkinitcpio -c /etc/mkinitcpio.conf -g /boot/initramfs-linux.img

Nato dodaš še kernel parametre v GRUB, da jih pošle v kernel:

    > sudo nvim /etc/default/grub
    GRUB_CMDLINE_LINUX_DEFAULT="resume=/dev/sda2 resume_offset=34816"

... in generiraš nov GRUB file:

    sudo grub-mkconfig -o /boot/grub/grub.cfg

Rebootaš in Hibernation DELA! :)

## After KERNEL UPGRATE ...

Pri upgrajdanju kernela na  5.7.8 mi hibernation ni več delal, dobil sem error, da je Swap file premajhen. Zato sem moral narediti nov swap file:

    rm /swapfile #deletes old swapfile
    dd if=/dev/zero of=/swapfile bs=1G count=18 status=progress
    chmod 600 /swapfile
    mkswap /swapfile
    swapon /swapfile # enables the swapfile right now
    echo '/swapfile none swap defaults 0 0' | tee --append /etc/fstab # configs the swapfile in startup

v /et/fsck sem imel že dodan swapfile ... , moral sem le spremeniti v /etc/default/grub "resume_offset" ker je bil na spremenjeni lokaciji (glej:filefrag -v /swapfile )
