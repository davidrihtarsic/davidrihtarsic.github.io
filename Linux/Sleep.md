# Sleep mode ...

ok probamo nekaj stvari... ker comp ne gre v slip ali hibernate po cca 10 min in vse laufa...

V /etc/systemd/logind.conf sem spremenil:

    HandleLidSwitch=suspend
    HandleLidSwitchExternalPower=suspend
    HandleLidSwitchDocked=suspend

OK :) to je rešilo problem ... torej prave nastavitve so:

Težava pa je ostala z Idle procesom t.j. ko računalnik miruje nekaj časa.
Ker uporabljam dwm (pojavi se tudi pri i3) in ta ne de "idle" signala, zato
systemd ne more izvest tega hooka. Comp se je ugasnil po 1 min ko sem nastavil tole:  

    IdleAction=suspend-then-hibernate
    IdleActionSec=1min

## REŠITEV

je bila to, da sem instaliral XAUTOLOCK

    yay -S xautolock

in nato v .xinitrc dodal tole: 

    xautolock -time 7 -locker "systemctl suspend" &  
