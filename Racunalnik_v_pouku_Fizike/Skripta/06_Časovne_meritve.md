\setcounter{section}{5}
# Časovne meritve

Za preproste časovne meritve lahko uporabimo funkcijo `millis()`. Funkcija `millis()` vrne število milisekund od začetka zagona programa na krmilniku Arduino Uno.

```cpp
unsigned long time;

void setup() {
  Serial.begin(9600);
}
void loop() {
  Serial.print("Time: ");
  time = millis();

  Serial.println(time); //prints time since program started
  delay(1000);          // wait a second so as not to send massive amounts of data
}
```
: Beleženje časa. {#lst:time_function}

Preverite tudi:
```cpp
time = micros();
```
## Časovni interval med dvema digitalnima spremembama
V povezavi s časovnimi meritvami pogosto uporabljamo digitalne vhode. Le-te lahko najdemo na priključkih **D0..D13** in tudi na **A0..A7**. Primer enostavne vezave tipke na krmilnik prikazuje slika [@fig:SW_uK.png].

![Vezava tipke na digitalni vhod krmilnika Arduino.](./slike/SW_uK.png){#fig:SW_uK.png height=7cm}

> ### NALOGA: Merjenje časovnih intervalov  
> Napišite program za merjenje hitrosti človeškega odziva in zvežite vezje, ki ga prikazuje slika [@fig:SW_uK.png]. Po naključnem času naj zasveti lučka na krmilniku ArduinoUNO. Nato pa naj program nemudoma shrani trenutni čas v $start\_time$ in ko uporabnik pritisne tipko naj si program ponovno shrani čas v $stop\_time$. Program naj izračuna razliko časov in ga prikaže v na računalniku.\
> Napredno: Če znate program popravite tako, da ne bo omogočal goljufanja.

```cpp
const int TIPKA = 7;
void randomly_turn_LED_on();
void start_timing_user_respond();
void reset_the_game();

void loop() {
  randomly_turn_LED_on();
  start_timing_user_respond();
  reset_the_game();
}

void setup() {
  pinMode(LED_BUILTIN ,OUTPUT);
  pinMode(TIPKA       ,INPUT_PULLUP);
  Serial.begin(9600);
  Serial.println("Start...");
  randomSeed(analogRead(0)); 
}

void randomly_turn_LED_on(){
  digitalWrite(LED_BUILTIN,LOW);
  delay(random(5000,10000));
  digitalWrite(LED_BUILTIN,HIGH);
}

void start_timing_user_respond(){
  unsigned long start_time = micros();
  unsigned long stop_time = 0;

  while (digitalRead(TIPKA) == 0){
    stop_time = micros();
  }

  unsigned long time_div = stop_time - start_time;
  Serial.println(time_div);
}

void reset_the_game(){
  while (digitalRead(TIPKA) == 1){
    delay(200);
    Serial.println("spusti tipko...");
  }
  Serial.println("Start...");
}
```
: Merjenje časovnega intervala. {#lst:time_diff}

## Hitrost

> ### NALOGA: Merjenje hitrosti predmeta (svetlobna vrata)  
> Uporabite ali sestavite dvojna svetlobna vrata. Nato napišite program, ki bo izmeril razliko v času ko se svetlobni snop na enih in drugih svetlobnih vratih prekine. Izmerite razdaljo med vratoma in izračunajte hitrost.\
> Napredno: Če zante program popravite tako, da bo občutljiv na "spremembo" vhodnega signala.

```cpp
const int VRATA_1 = 7;
const int VRATA_2 = 8;
void wait_for_gate_change(int input_pin);
void print_time_difference(unsigned long start_time,
                           unsigned long stop_time);
void loop() {
  wait_for_gate_change(VRATA_1);
  unsigned long start_time = micros();
  wait_for_gate_change(VRATA_2);
  unsigned long stop_time = micros();
  
  print_time_difference(start_time, stop_time);
  Serial.println("Nova maritev...");
}

void setup() {
  pinMode(VRATA_1, INPUT);
  pinMode(VRATA_2, INPUT);
  Serial.begin(9600);
  Serial.println("Start...");
}

void wait_for_gate_change(int input_pin){
  bool zacetna_vrednost  = digitalRead(input_pin);
  bool trenutna_vrednost = zacetna_vrednost;
  
  while (trenutna_vrednost == zacetna_vrednost){
    trenutna_vrednost = digitalRead(input_pin);
  }
}
void print_time_difference(unsigned long start_time,unsigned long stop_time){
  unsigned long time_diff = stop_time - start_time;
  Serial.println(time_diff);
}
```
: Merjenje hitrosti predmeta. {#lst:speed_measure}

## Pospešek

