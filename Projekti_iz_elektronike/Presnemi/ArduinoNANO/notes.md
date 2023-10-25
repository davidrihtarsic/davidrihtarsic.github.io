# programiranje ATmega16

1. napišeš program:

```
int
main(void)
{

        while (1);
}
```

2. compile

        avr-gcc -Wall -g -Os -mmcu=atmega16 -o main.bin main.c

        avr-objcopy -j .text -j .data -O ihex main.bin main.hex


/home/david/.arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17/bin/avrdude -C/home/david/.arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17/etc/avrdude.conf -c stk500v1 -b19200 -P /dev/ttyUSB0 -p m16 -U flash:w:main.hex:i

/home/david/.arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17/bin/avrdude" "-C/home/david/.arduino15/packages/arduino/tools/avrdude/6.3.0-arduino17/etc/avrdude.conf" -v  -patmega328p -carduino "-P/dev/ttyUSB0" -b57600 -D "-Uflash:w:/tmp/arduino/sketches/38065CAB08770CA40D6C5D8E1CD447E4/Blink.ino.hex:i
