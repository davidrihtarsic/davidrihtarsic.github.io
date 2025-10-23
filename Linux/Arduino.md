# ARDUINO

## Dodajanje pravic naprave med uporabnike

Do naprave '/dev/ttyACM0' navadno ne moramo dostopati ter tako ne moremo programirati Arduino krmilnika.
Napravo lahko dodoamo tako:

    ls -l /dev/ttyACM*
  > crw-rw---- 1 root dialout 188, 0 5 apr 23.01 ttyACM0

sedaj dodamo našega uporabnika <uporabnik> da lahko upravlja s to napravo "dialout"

    sudo usermod -a -G dialout <uporabnik>

## ARDUINO WAVGAT

1. Start Arduino IDE and open "Preferences" window from "File" menu.
2. Go to "Additional Board Manager URLs" field add this url:
    https://raw.githubusercontent.com/paraplin/wavgat-board/master/package_paraplin_wavgat_index.json
    and press OK.
3. Go to "Tools" menu and select "Open Boards Manager". In the new window install wavgat platform.
4. Go to "Tools" menu and go to "board" submenu. Select your correct board in "WAVGAT boards" section.

<!--
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
    
-->

## Arduino USB povezava - Linux

1. ko priljučimo Arduino na USB, se v /dev/ pojavi file /dev/ttyUSB0 

        ls /dev/ttyU*

2. preverimo lahko tudi, z ukazom lsusb nekaj več podatkov o napravi
Naprimer najprej pregledamo vse usb naprave:

        lsusb

> Bus 002 Device 003: ID 0bda:0411 Realtek Semiconductor Corp. Hub
> Bus 002 Device 004: ID 0bda:8153 Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
> Bus 002 Device 002: ID 2109:0817 VIA Labs, Inc. USB3.0 Hub
> Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
> Bus 001 Device 005: ID 8087:0a2b Intel Corp. Bluetooth wireless interface
> Bus 001 Device 004: ID 0bda:0129 Realtek Semiconductor Corp. RTS5129 Card Reader Controller
> Bus 001 Device 003: ID 04f2:b57a Chicony Electronics Co., Ltd USB2.0 HD UVC WebCam
> Bus 001 Device 010: ID 2109:8817 VIA Labs, Inc. USB Billboard Device
> Bus 001 Device 011: ID 056a:0378 Wacom Co., Ltd CTL-6100WL [Intuos BT (M)]
> Bus 001 Device 009: ID 045e:00db Microsoft Corp. Natural Ergonomic Keyboard 4000 V1.0
> Bus 001 Device 008: ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
> Bus 001 Device 006: ID 2109:2817 VIA Labs, Inc. USB2.0 Hub
> Bus 001 Device 002: ID 046d:c52b Logitech, Inc. Unifying Receiver
> Bus 001 Device 013: ID 1a86:7523 QinHeng Electronics CH340 serial converter
> Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

... nato lahko izpišemo še nekaj več podatkov o sami napravi:

        lsusb --verbose -s 001:13

> Bus 001 Device 013: ID 1a86:7523 QinHeng Electronics CH340 serial converter
> Couldn't open device, some information will be missing
> Device Descriptor:
>   bLength                18
>   bDescriptorType         1
>   bcdUSB               1.10
>   bDeviceClass          255 Vendor Specific Class
>   bDeviceSubClass         0
>   bDeviceProtocol         0
>   bMaxPacketSize0         8
>   idVendor           0x1a86 QinHeng Electronics
>   idProduct          0x7523 CH340 serial converter
>   bcdDevice            2.62
>   iManufacturer           0
>   iProduct                2 USB2.0-Serial
>   iSerial                 0
>   bNumConfigurations      1
>   Configuration Descriptor:
>     bLength                 9
>     bDescriptorType         2
>     wTotalLength       0x0027
>     bNumInterfaces          1
>     bConfigurationValue     1
>     iConfiguration          0
>     bmAttributes         0x80
>       (Bus Powered)
>     MaxPower               98mA
>     Interface Descriptor:
>       bLength                 9
>       bDescriptorType         4
>       bInterfaceNumber        0
>       bAlternateSetting       0
>       bNumEndpoints           3
>       bInterfaceClass       255 Vendor Specific Class
>       bInterfaceSubClass      1
>       bInterfaceProtocol      2
>       iInterface              0
>       Endpoint Descriptor:
>         bLength                 7
>         bDescriptorType         5
>         bEndpointAddress     0x82  EP 2 IN
>         bmAttributes            2
>           Transfer Type            Bulk
>           Synch Type               None
>           Usage Type               Data
>         wMaxPacketSize     0x0020  1x 32 bytes
>         bInterval               0
>       Endpoint Descriptor:
>         bLength                 7
>         bDescriptorType         5
>         bEndpointAddress     0x02  EP 2 OUT
>         bmAttributes            2
>           Transfer Type            Bulk
>           Synch Type               None
>           Usage Type               Data
>         wMaxPacketSize     0x0020  1x 32 bytes
>         bInterval               0
>       Endpoint Descriptor:
>         bLength                 7
>         bDescriptorType         5
>         bEndpointAddress     0x81  EP 1 IN
>         bmAttributes            3
>           Transfer Type            Interrupt
>           Synch Type               None
>           Usage Type               Data
>         wMaxPacketSize     0x0008  1x 8 bytes
>         bInterval               1

## Arduino as programmer


1. Na Arduiono programmer naložimo:

ArduionoIDE -> Examples -> ArduinoISP

2. Povežemo programmer in targer vezje:

| Sigmnal | Arduino programmer | ISP Connector |
|:-------:|:------------------:|:-------------:|
|   MISO  |         D11        |       1       |
|   VCC   |         +5V        |       2       |
|   SCK   |         D13        |       3       |
|   MOSI  |         D11        |       4       |
|   ~RST  |         D10        |       5       |
|   GND   |         GND        |       6       |

3. Povezavo lahko preverimo z ukazom:

        ./avrdude -c arduino -p atmega328p -P /dev/ttyUSB0 -b 19200 -C /home/david/.arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17/etc/avrdude.conf -v

>avrdude: Version 6.3-20190619
>         Copyright (c) 2000-2005 Brian Dean, http://www.bdmicro.com/
>         Copyright (c) 2007-2014 Joerg Wunsch
>
>         System wide configuration file is "/home/david/.arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17/etc/avrdude.conf"
>         User configuration file is "/home/david/.avrduderc"
>         User configuration file does not exist or is not a regular file, skipping
>
>         Using Port                    : /dev/ttyUSB0
>         Using Programmer              : arduino
>         Overriding Baud Rate          : 19200
>         AVR Part                      : ATmega328P
>         Chip Erase delay              : 9000 us
>         PAGEL                         : PD7
>         BS2                           : PC2
>         RESET disposition             : dedicated
>         RETRY pulse                   : SCK
>         serial program mode           : yes
>         parallel program mode         : yes
>         Timeout                       : 200
>         StabDelay                     : 100
>         CmdexeDelay                   : 25
>         SyncLoops                     : 32
>         ByteDelay                     : 0
>         PollIndex                     : 3
>         PollValue                     : 0x53
>         Memory Detail                 :
>
>                                  Block Poll               Page                       Polled
>           Memory Type Mode Delay Size  Indx Paged  Size   Size #Pages MinW  MaxW   ReadBack
>           ----------- ---- ----- ----- ---- ------ ------ ---- ------ ----- ----- ---------
>           eeprom        65    20     4    0 no       1024    4      0  3600  3600 0xff 0xff
>           flash         65     6   128    0 yes     32768  128    256  4500  4500 0xff 0xff
>           lfuse          0     0     0    0 no          1    0      0  4500  4500 0x00 0x00
>           hfuse          0     0     0    0 no          1    0      0  4500  4500 0x00 0x00
>           efuse          0     0     0    0 no          1    0      0  4500  4500 0x00 0x00
>           lock           0     0     0    0 no          1    0      0  4500  4500 0x00 0x00
>           calibration    0     0     0    0 no          1    0      0     0     0 0x00 0x00
>           signature      0     0     0    0 no          3    0      0     0     0 0x00 0x00
>
>         Programmer Type : Arduino
>         Description     : Arduino
>         Hardware Version: 2
>         Firmware Version: 1.18
>         Topcard         : Unknown
>         Vtarget         : 0.0 V
>         Varef           : 0.0 V
>         Oscillator      : Off
>         SCK period      : 0.1 us
>
>avrdude: AVR device initialized and ready to accept instructions
>
>Reading | ################################################## | 100% 0.01s
>
>avrdude: Device signature = 0x1e950f (probably m328p)
>avrdude: safemode: lfuse reads as FF
>avrdude: safemode: hfuse reads as DE
>avrdude: safemode: efuse reads as FD
>
>avrdude: safemode: lfuse reads as FF
>avrdude: safemode: hfuse reads as DE
>avrdude: safemode: efuse reads as FD
>avrdude: safemode: Fuses OK (E:FD, H:DE, L:FF)
>
>avrdude done.  Thank you.

## ISSUES

### Preverjanje krmilnikov Arduino UNO

1. Preverimo, če deluje integrirano vezje CH340 za USB->UART komunikacijo:
    1. povežeš PC in krmilnik UNO, ter preveriš,
        če je zaznana nova naprava na vratih za serijsko komunikacijo.
    2. odpreš Serial Monitor in pošlješ nek znak:
        na krmilniku UNO mora uripniti ledica za TX
    3. preverimo povratno UART komunikacijo = PC->CH340->PC:
        - onemogoči mikrokrmilnik ATmega328P = povežeš RST -> GND
        - kratko skleneš nožico 2 in 3 na CH340 (z izvijačem ali priključkom M-metra)
        - v Serijski Monitor vpišemo nekaj znakov in le-ti se morajo izpisati nazaj na PC
2. Preverimo delovanje mikrokrmilnika ATmega328P:
    1. s programatorjem ArduinoISP preverimo signature byte
    2. s programatorjem ArduinoISP poizkusimo naložiti Blink
    3. s programatorjem ArduinoISP naložimo Bootloader

### Preverjanje krmilnikov Arduino UNO

#### avrdude: stk500_recv(): programmer is not responding
Opis napake:
    Arduino Uno se ne da sprogramirati. Vrne napako :avrdude: stk500_recv(): programmer is not responding.

Check lista:
1. Če se povežeš na serijsko vodilo (USB->UART) in pošlješ iz PC -> UNO nek text, ali ledica Rx nutripa?
2. Če povežes RX in Tx na UNOTU in pošlješ nek text ali obe ledici utripata?
3. Ali s programatorjem ArduinoISP lahko prebereš SighnatureByte 1E950F - ATmega328P?
4. Ali lahko s programatorjem ArduinoISP sprogramiraš krmilnik Arduino Uno?
5. Z drugim krmilnikom UART pošlji podatek na nožico Tx... in se mora na računalniku pojaviti ta podatek?

| no | Opis testiranja                                          | 11  | 12 | 13 |
|:--:|:---------------------------------------------------------|-----|----|----|
| 1. | ATmega328P signature byte read by ArduinoISP programmer? | YES |    |    |
| 2. | Program with ArduinoISP programmer?                      | YES |    |    |
| 3. | Program bootloader with ArduinoISP programmer?           | YES |    |    |
| 4. | CH340 prepoznan?                                         | YES | NO | NO |
| 5. | PC->CH340 = TX Led blinking?                             | YES |    |    |
| 6. | PC->CH340->TX->----->RX = LED is blinking?               | YES |    |    |
| 7. | Delujoči UART.Tx->UNO.Tx->CH340->PC?                     | NO  |    |    |


