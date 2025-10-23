\setcounter{section}{3}
\setcounter{section}{3}
# Arduino UNO

Arduino Uno je:

> The UNO is the best board to get started with electronics and coding. If this is your first experience tinkering with the platform, the UNO is the most robust board you can start playing with. The UNO is the most used and documented board of the whole Arduino family.
@ArduinoU75:online


![Arduino Uno](./slike/ArduinoUNO.jpg)

## Arduino UNO/NANO pinout

![Razporeditev priključkov na krmilniku Arduino UNO [@ArduinoUNOpinout:online].](./slike/Arduino-UNO-pinout.jpeg){#fig:Arduino-UNO-pinout.jpeg}

![Razporeditev priključkov na krmilniku Arduino NANO [@ArduinoUNOpinout:online].](./slike/nano.png){#fig:nano.png}

Kot lahko opazimo, so funkcije priključkov na sliki [@fig:Arduino-UNO-pinout.jpeg] in sliki [@fig:nano.png] enaki. To ni nenavadno, saj sta krmilnika po električni zgradbi enaka, razlikujeta se le v fizični izvedbi.

## Osnove programiranja krmilnika

> ### NALOGA: Nastavitve Arduino IDE programa  
> Pravilno priključite krminlnik Arduino na računalnik in nastavite programsko okolje Aruino IDE ter sprogramirajte krmilnik s testnim programom **BLINK.INO**. Iz nastavitev programskega okolja prepišite vaše nastavitve za:\
> 1. krmilnik:______________,\
> 2. komunikacijska vrata: _________,\
> 3. mikrokrmilnik: _____________.

**Testni program BLINK.INO**

Nastavite in delovanje krmilnika lahko preverimo s testnim programom **blink.ino**. Na krmilniku Arduino UNO je na priključek **13** priključena svetleča dioda prav za ta namen.

```cpp
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```
: Vzorčni program za krmilnik Arduino NANO. {#lst:test_prg}

> ### NALOGA: Berljivost programske kode  
> Spremenite [@lst:test_prg] tako, da bo čim bolj berljiv. Pri berljivosti programske kode lahko upoštevate neka smernic:
>
> 1. Skupek programskih ukazov združujte v funkcije, ki jih smiselno poimenujte.
>     1. Iz programske strukture naj se opazi čemu je program namenjen.
>     2. Če funkcija `void loop()` bolje opisuje namen programa, jo postavite pred `void setup()`.
>     3. Funkcije naj vračajo in sprejemajo smiselne parametre.
> 2. Uporabljajte `razlagalne spremenljivke in konstante` namesto surovih številčnih vrednosti.
>     1. Uporabljene priključke vedno poimenujte npr.: `int LED_PIN = 13;`.
>     2. Razmislite o potrebnem območju veljavnosti (angl. scope) spremenljivke.
>     3. Vmesne rezultate in vrednosti smiselno poimenujte npr.: `int vrednost_senzorja = analogRead(SENZOR_PIN);`
> 3. Uporabljajte komentarje LE tam, kjer je to ZARES potrebno.
>     1. Imena spremenljivk, konstant in funkcij naj pomagajo pri opisovanju kode, npr.: funkcija `delay(1000)` ne potrebuje nobenega komentarja.
>     2. Komentarji lahko postanejo dodatni element, ki ga bo potrebno vzdrževati...
>

