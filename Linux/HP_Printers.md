# HP - PRINTERS

Imel sem težave s HP printerjem... na PeF-u ... rešil sem tako, da sem naložil nazaj:

- HPLIP ( hplip 1:3.19.11-4 ) in 
- CUPS ( cups 2.3.0-4 )

Pred kratkim je na AUR-ju bilo objavljeno tole obvestilo:  

    2020-03-19 hplip 3.20.3-2 update requires manual intervention 
    The hplip package prior to version 3.20.3-2 was missing the compiled 
    python modules. This has been fixed in 3.20.3-2, so the upgrade will 
    need to overwrite the untracked pyc files that were created. If you get errors 
    such as these 
    hplip: /usr/share/hplip/base/__pycache__/__init__.cpython-38.pyc exists in filesystem 
    hplip: /usr/share/hplip/base/__pycache__/avahi.cpython-38.pyc exists in filesystem 
    hplip: /usr/share/hplip/base/__pycache__/codes.cpython-38.pyc exists in filesystem 
    ...many more... 
    when updating, use 
    pacman -Suy --overwrite /usr/share/hplip/\* 
    to perform the upgrade. 

... bomo sprobali in bomo videli..

## Težave...

Pred kratkim sem imel težave tudi na svojem ASUS-u (arch linux). Ko  sem dal printat nek dokument, sem v 

/var/log/cups/error_log

našel tole:

    E [01/Aug/2022:17:18:36 +0200] [Job 269] Unable to write print data: Broken pipe
    W [01/Aug/2022:17:18:36 +0200] [Job 269] Backend returned status 1 (failed)
    W [15/Aug/2022:21:26:50 +0200] Printer drivers are deprecated and will stop working in a future version of CUPS. See https://github.com/OpenPrinting/cups/issues/103
    E [15/Aug/2022:21:26:50 +0200] Missing value on line 382 of /var/cache/cups/job.cache.
    E [15/Aug/2022:21:26:50 +0200] Missing value on line 1014 of /var/cache/cups/job.cache.
    E [15/Aug/2022:21:29:05 +0200] [CGI] ippfind (PID 7348) stopped with status 2!
    E [15/Aug/2022:21:29:05 +0200] [cups-deviced] PID 7346 (driverless) stopped with status 2!
    E [15/Aug/2022:21:29:26 +0200] [CGI] ippfind (PID 8186) stopped with status 2!
    E [15/Aug/2022:21:38:38 +0200] [CGI] ippfind (PID 42173) stopped with status 2!
    E [15/Aug/2022:21:38:38 +0200] [cups-deviced] PID 42167 (driverless) stopped with status 2!
    E [15/Aug/2022:21:38:48 +0200] [CGI] ippfind (PID 42566) stopped with status 2!
    E [15/Aug/2022:21:54:46 +0200] [CGI] ippfind (PID 133825) stopped with status 2!
    E [15/Aug/2022:21:55:16 +0200] [CGI] ippfind (PID 135281) stopped with status 2!
    E [15/Aug/2022:21:57:11 +0200] [CGI] ippfind (PID 140680) stopped with status 2!

nimam pojma
inštaliral sem :

    hplip-printer-app

pa ni bilo nič bolje...
nisem prepričan ampak ko sem dal printat vsako stran na svoj list je dvakrat delalo...
ne dela pa, če dam printat na obe strani

## še sprobaj

- opazil sem, da imam avahi-deamon.service izklopljen. Čeprav, naj bi ta server bil le za prepoznavo in odkrivanje printerjev... Mislim pa, da ne za samo printanje.
