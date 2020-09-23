# ARDUINO

## Dodajanje pravic naprave med uporabnike

Do naprave '/dev/ttyACM0' navadno ne moramo dostopati ter tako ne moremo programirati Arduino krmilnika.
Napravo lahko dodoamo tako:

    ls -l /dev/ttyACM*
  > crw-rw---- 1 root dialout 188, 0 5 apr 23.01 ttyACM0

sedaj dodamo našega uporabnika <uporabnik> da lahko upravlja s to napravo "dialout"

    sudo usermod -a -G dialout <uporabnik>

## ARDUINO WAVGAT

1. prenesi [WAVGAT drivers]( https://github.com/ericvb/Arduino-WavGat-Drivers )
2. skopiraj ./update/* v ~/Arduino/*
3. za Linuxe popravi:
    
    `../hardware/WAV/avr/boards.txt:lardu_328p.bootloader.file=lgt8fx8p\optiboot_lgt8f328p.hex`
    `../hardware/WAV8F/boards.txt:lardu_328p.bootloader.file=lgt8fx8p\optiboot_lgt8f328p.hex`
4. ponovno zaženi Arduino IDE in izberi `Tools - Boards - WAVGAT UNO R3`

### skrita za linux
[install_wavgat_boards](install_wavgat_boards.sh)
git clone https://github.com/ericvb/Arduino-WavGat-Drivers.git
cp -rv Arduino-WavGat-Drivers/update/* ~/Arduino/ 
