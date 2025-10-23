# XRANDR

Imel sem problem, da se ni pokazala prava resolucija za sosednji ekran, če sem ga priključil
preko USB-C Multi-hub-a. Rešilo me je, da sem najprej:

    xrandr --auto
    xrandr

nato je bila resolucija tu:

>  ╰> xrandr  
>  Screen 0: minimum 8 x 8, current 3840 x 1080, maximum 32767 x 32767  
>  eDP1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 340mm x 190mm  
>     1920x1080     60.02*+  59.93  
>     1680x1050     59.88  
>     1400x1050     59.98  
>     1600x900      60.00    59.95    59.82  
>     1280x1024     60.02  
>     1400x900      59.96    59.88  
>     1280x960      60.00  
>     1368x768      60.00    59.88    59.85  
>     1280x800      59.81    59.91  
>     1280x720      59.86    60.00    59.74  
>     1024x768      60.00  
>     1024x576      60.00    59.90    59.82  
>     960x540       60.00    59.63    59.82  
>     800x600       60.32    56.25  
>     864x486       60.00    59.92    59.57  
>     640x480       59.94  
>     720x405       59.51    60.00    58.99  
>     640x360       59.84    59.32    60.00  
>  DP1 connected 1920x1080+1920+0 (normal left inverted right x axis y axis) 480mm x 270mm  
>     1920x1080     60.00*+  50.00    59.94  
>     1920x1080i    60.00    50.00    59.94  
>     1600x1200     60.00  
>     1680x1050     59.88  
>     1400x1050     59.95  
>     1280x1024     75.02    60.02  
>     1440x900      59.90  
>     1280x960      60.00  
>     1152x864      75.00  
>     1280x720      60.00    50.00    59.94  
>     1440x576      50.00  
>     1024x768      75.03    70.07    60.00  
>     1440x480      60.00    59.94  
>     832x624       74.55  
>     800x600       72.19    75.00    60.32    56.25  
>     720x576       50.00  
>     720x480       60.00    59.94  
>     640x480       75.00    72.81    66.67    60.00    59.94  
>     720x400       70.08  
>  HDMI1 disconnected (normal left inverted right x axis y axis)  
>  HDMI2 disconnected (normal left inverted right x axis y axis)  
>  VIRTUAL1 disconnected (normal left inverted right x axis y axis)  

## ADD MODE

Kako dodoamo novo resolucijo zaslona

    cvt 1920 1080 60

> # 1920x1080 59.96 Hz (CVT 2.07M9) hsync: 67.16 kHz; pclk: 173.00 MHz  
> Modeline "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync

Nato skopiras zadnjo vrstico izhoda in jo uporabiš v naslednjem ukazu

    xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync

in ta mode dodaš monutorju, ki mu ta mode manjka

    xrandr --addmode DP1 1920x1080_60.00

preverimo če je mode na spisku možnosti

    xrandr

> Screen 0: minimum 8 x 8, current 1920 x 1080, maximum 32767 x 32767
> eDP1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 340mm x 190mm
>    1920x1080     60.02*+  59.93
>    1680x1050     59.88
>    ...
>    640x360       59.84    59.32    60.00
> DP1 connected (normal left inverted right x axis y axis)
>    1024x768      60.00
>    800x600       60.32    56.25
>    848x480       60.00
>    640x480       59.94
>    1920x1080_60.00  59.96
> HDMI1 disconnected (normal left inverted right x axis y axis)
> HDMI2 disconnected (normal left inverted right x axis y axis)
> VIRTUAL1 disconnected (normal left inverted right x axis y axis)

in vključimo monitor s to resolucijo

    xrandr --output DP1 --mode 1920x1080_60.00 --pos 1920x0

## Problem 2: Dimenzije monitorja niso bile pravilno odčitane

Namesto dimenzij 477 mm x 268 mm so se dimenzije monitorja nastavile na 160 x 90 memory
To sem popravil tako, da sem v datoteko `/etc/X11/xorg.conf.d/90-monitor.conf` nastavil
pravilno velikost zaslona:

    Section "Monitor"
        Option    "UseEdidDpi"    "false"
        Identifier             "DP-1-8"
        DisplaySize             576 267
    EndSection

> ... no, tega problema nisem rešil... četudi imam to datoteko '/etc/X11/xorg.conf.d/90-monitor.conf'
> in se med nastavitvami ta dimenzija monitorja tudi nastavi:

    less /var/log/Xorg.0.log

> [   414.749] (II) modeset(0): Output DP-3-9 using initial mode 640x480 +3840+0
> [   414.749] (==) modeset(0): DPI set to (96, 96)
> ...
> [   414.749] (II) Loading sub module "fb"
> [   414.749] (II) LoadModule: "fb"
> [   415.056] (II) Initializing extension XFree86-DRI
> [   415.056] (II) Initializing extension DRI2
> ...
> [   415.057] (II) modeset(0): Setting screen physical size to 527 x 297
> [   415.107] (II) config/udev: Adding input device Video Bus (/dev/input/event5)

> ta nastavitev ni vidna v :

    xrandr -q

> Screen 0: minimum 320 x 200, current 4864 x 1200, maximum 16384 x 16384
> eDP-1 connected primary 1920x1200+0+0 (normal left inverted right x axis y axis) 344mm x 215mm
>    1920x1200     60.01*+  59.95
>    320x180       59.84    59.32
>    ...
> DP-3-8 connected 1920x1080+1920+0 (normal left inverted right x axis y axis) 598mm x 336mm
>    1920x1080     60.00*+  50.00    59.94
>    ...
> DP-3-9 connected 1024x768+3840+0 (normal left inverted right x axis y axis) 0mm x 0mm
>    640x480       59.94 +
>    1024x768      60.00*
>    800x600       60.32    56.25
>    848x480       60.00
