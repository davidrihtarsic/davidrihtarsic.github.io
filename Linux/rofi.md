# ROFI

A  window  switcher,
application launcher,
ssh dialog,
dmenu replacement and more...

## Application launcher

    rofi -modi run,drun -show drun -line-padding 4 \
                -columns 2 -padding 50 -hide-scrollbar \
                -theme gruvbox-dark-hard \
                -show-icons -theme-str 'element-icon { size: 3ch;}' \
                -drun-icon-theme "ArchLabs-Light"

## Config file

o get a full list of options for config.rasi file run 

    rofi -dump-config

You can write the output of the command directly to your configuration file while running 

    rofi -dump-config > ~/.config/rofi/config.rasi
