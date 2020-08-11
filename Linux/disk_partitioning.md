# Disk partitioning

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
