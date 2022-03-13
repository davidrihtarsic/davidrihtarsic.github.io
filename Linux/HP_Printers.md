## HP - PRINTERS

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
