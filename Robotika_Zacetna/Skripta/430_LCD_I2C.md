# LCD(I2C)

## Tasks:

1. Priključite LCD na I2C vodilo kot prikazuje 

![Povezava LCD na I2C vodilo krmilnika.](./slike/I2C_LCD.png){#fig:test_I2C_LCD}

2. Priskrbite si knjižnico `LiquidCristal-I2C` iz naslova:  
https://www.arduino.cc/reference/en/libraries/liquidcrystal-i2c/ 
3. Knjižnico dodajte v Arduino IDE okolje tako, da dodate `ZIP` datoteko v :  
`Sketch >> Include Library >> Add .ZIP Library`
3. V VSC in PlatformIO vtičniku si lahko knjižnico naložite tako, da v terminalno okno vpišete ukaz  
`pio lib install "marcoschwartz/LiquidCrystal_I2C@^1.1.4"`

4. Nato preskusite naslednji program:

```cpp
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C Lcd(0x27, 16, 2);

void setup() {   
    Lcd.init();
    
    Lcd.clear();
    Lcd.backlight();
    
    Lcd.setCursor(3,0);
    Lcd.print("Hello");
    Lcd.setCursor(6,1);
    Lcd.print("World");   
}

void loop() {
}
```

Če niste prepričani kateri i2c naslov uporablja naprava na LCD-ju le tega lahko preverite s programom `I2C scanner` (https://playground.arduino.cc/Main/I2cScanner/). Običajno I2C LCD-ji, ki jih naredijo kitajski proizvajalci uporabljajo I2C naslov `0x27` , `0x3F` ali manj pogosto `0x38`.

## Questions:

1.  \<++\>
2.  \<++\>

\[ Visual instructions. \]

> ## Summary:
> 
> ### \<++\>
> 
> \<++\>
> 
> ## Issues:
> 
> ### *\<++\>*
> 
> <++>

