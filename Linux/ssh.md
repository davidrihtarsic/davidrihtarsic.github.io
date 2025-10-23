# SSH

ssh to Android phone

- [ video tutorial](https://www.youtube.com/watch?v=TNZW0LvEUKM)

## Navodila za povezavo na Telefon

### Na telefonu
1. Na telefonu zalaufaš `Termux`
2. pogledaš ime userja `whoami`
> u0_a199
3. nastaviš password za userja `passwd u0_a199`
> New password: *****
> Retype new password: *****
> New password was successfully set.
2. poženeš `sshd`
3. preveriš port ssh serverja `nmap localhost`
> Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-16 21:49 CET
> Nmap scan report for localhost (127.0.0.1)
> Host is up (0.0074s latency).
> Not shown: 999 closed ports
> PORT     STATE SERVICE
> 8022/tcp open  oa-system
> 
> Nmap done: 1 IP address (1 host up) scanned in 1.40 seconds
v tem primeru je port na 8022
6. preveriš ip `ifconfig wlan0`
> wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
> inet 192.168.0.15  netmask 255.255.255.0  broadcast 192.168.0.255

### Na Laptopu

1. v terminalu poženeš: `ssh u0_a199@192.168.0.15 -p 8022`
> u0_a199@192.168.0.15's password:*****
in si na telefonu...
> ╭=[ArchPhoneDR|~]==--
> ╰>
> 

### File manager

1. odpreš Nemota...
2. v okence za dirrectory vpišeš: `sftp://u0_a199@192.168.0.15:8022`
3. vpišeš geslo
4. pod `Network` najdeš telefon

### SSHFS

Da mountaš telefon kar nekam na disk od računalnika...

1. osnovni ukaz `sshfs -p 8022 u0_a199@192.168.0.15:/data/data/com.termux/files/home /home/david/Files/Davids_Phone`
> [sudo] password for david:*****

2.  da se tudi vpis gesla zgodi automatsko: `sshfs -p 8022 -o follow_symlinks -o password_stdin u0_a199@192.168.0.15:/data/data/com.termux/files/home /home/david/Files/Davids_Phone <<<'*****'`

3. da od-mountaš `sudo umount /home/david/Files/Davids_Phone`

### Problemi

na ta način nisem mogel do nekaterih dirrectory-ev, ki so bili polinkani... rešitev je da dodaš še `-o follow_symlinks`


