#! /bin/zsh

find ../*/*md | sed "s/^/<a href =/ ; s/.md/.html><++><\/a>/" | \
                sed "/index/ s/^/<details><summary>/" | \
                sed "/index/ s/$/<\/summary>/" | \
                sed "/index/ ! s/^/\t\t<il>/" | \
                sed "/index/ ! s/$/<\/li>/" | \
                sed "/index/ s/^/<\/details>\n/" | \
                sed "1d;\$a<\/details>"
