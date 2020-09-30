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

