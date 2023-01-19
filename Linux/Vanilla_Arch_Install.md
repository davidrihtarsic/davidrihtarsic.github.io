# VANILLA ARCH INSTALL

Predno končamo z namestitvijo je verjetno dobro, da namestimo nekaj osnovnih paketov:

    sudo pacman -S --noconfirm \
        git \
        neovim \
        ranger \
        firefox \
        tree \
        man \
        xterm \
        alacritty \
        picom \
        dwm

Po ponovnem zagonu se `tty1 login:`

> login:david
> password:*****
> Last login: datum on tty1

in za tem se zažene ~/.bash_profile ali `~/.zshenv`, če imamo zsh kot shell.
na konec tega dokumenta pripnemo:

    [[ $(fgconsole)==1 ]] && startx

in zagnali bomo window manager, ki je določen v datoteki `~/.xinitrc`

## X11

X je Window System, ki poskrbi, da je možno prikazati programe v oknih, da delujeta 
tudi tipkovnica in miška... ter tudi druge naprave...

Ko zaženemo:

    startx

se izvrši skript `~/.xinitrc`, če le tega nimamo v `$HOME` direktoriju, je privzeta
datoteka v `/etc/X11/xinit/xinitrc`.

```bash
#!/bin/sh
userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap
# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi
if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi
# start some nice programs
if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# twm &
# xclock -geometry 50x50-1+1 &
# xterm -geometry 80x50+494+51 &
# xterm -geometry 80x20+494-0 &
# exec xterm -geometry 80x66+0+0 -name login

# te zgornje vrstice nadomestimo z 
exec dwm
```

Skript `~/.xinit` zažene še nekaj pomembnih datotek, kjer je shranjenih nekaj
pomembnih podatkov, ki jih X potrebuje za delovanje:

    /home/david/.config/X11/Xmodmap
    /home/david/.config/X11/Xresources
    /home/david/.config/X11/xprofile

V tem vrstem redu se zagon ArchLinuxa zgodi...
