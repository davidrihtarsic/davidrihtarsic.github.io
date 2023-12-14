STARTX
================================================================================

Ko zaženemo startx se najprej zgodi:

.xinitrc  -


## Display manager

Če grafočni vmesnik zaženemo z nekim display managerjem se zažene

## .xsession

naloga je , da se nastavijo spremenljivke okolja in nato še GUIja

    #!/bin/sh
    . ~/.xprofile
    . ~/.xinitrc

### .xprofile

kakor razumem, naj bi tu bile vse spremenljivke...

### .xinitrc

tu pa vsi programi in na koncu še window manager.

