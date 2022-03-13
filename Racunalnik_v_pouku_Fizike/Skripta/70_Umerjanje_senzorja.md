# UMERJANJE (TEMPERATURNEGA) SENZORJA

- glej poglavje o delilnikih
- naredite temp. senzor, katerega odziv bo največji za temperaturno območje $T_{NTC} = [15,95]°C$.

> ### NALOGA: Dimenzioniranje senzorja
> Podrobno si poglejte [@sec:delilnik] in dimenzionirajte temperaturn sentor z NTC termistorjem za območje $T = [15,95]°C$. Izračunajte ali izmerite ključne vrednosti za dimenzioniranje senzorja:\
> $R_{NTC, T=15°C}=$___________,\
> $R_{NTC, T=95°C}=$___________,\
> $R_{REF}=$______________.


![Vezava temperatunega senzorja.](./slike/NTC_uK.png){#fig:NTC_uK.png height=7cm}

\newpage
## Umeritveni postopek

> ### NALOGA: Umerjanje temperaturnega senzorja.
> Naredite umeritveni postopek in predstavite tabelo s podatki.\
> \
>  **T[°C]**   |     **U[V]**\
> \
> \
> \
> \
> \
> \
> \
> \

```cpp
String inputString = "";         // a String to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(9600);
  printHelp();
  inputString.reserve(20);
}
void printHelp(){
  Serial.println("###########################################");
  Serial.println("# INSTRUCTIONS:                           #");
  Serial.println("#   1. Insert temperature (example: 22.4) #");
  Serial.println("#   2. then press ENTER                   #");
  Serial.println("#   3. repeat steps 1. and 2. ...         #");
  Serial.println("# When you are done with calibration:     #");
  Serial.println("#   4. Copy data to spreadsheet.          #");
  Serial.println("#   5. Add some polynome to the points.   #");
  Serial.println("#   6. Insert coeficients into file:      #");
  Serial.println("#       'temperature.ino'                 #");
  Serial.println("###########################################");
  Serial.println("T[°C] Value");
}
void loop() {
  //float ref_temp = waitForUserInput();
  //float sen_val = sensorsAvgValueOnCh(A0);
  //printNewTabelRow(ref_temp, sen_val);
  if (stringComplete) {
    Serial.print(inputString);
    Serial.print(" ");
    inputString = "";
    stringComplete = false;

    long CH1 = 0;

    int i;
    for (i = 0; i < 128; i++) {
      CH1 += analogRead(A7);
      delay(1);
    }
    float Vol_CH1 = float(CH1/128.0);          // calibration in ADC values...
    //float Vol_CH1 = CH1*5.0/1024; // calibration in Voltage...
    Serial.println(Vol_CH1);
  }
}
float waitForUserInput(){
  char inChar = '';
  while (inChar != '\n'){
    if (Serial.available()) inChar = (char)Serial.read();
    if (inChar != '\n') 
  }
}
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();  // get the new byte:
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;              // add it to the inputString:
    }
  }
}
```

<!--
Ker zgornji program ni deloval, sem na hitro sestavil naslednjega_
V simulaciji ne dela ENTER, zato je potrebno ENTER= '\n' zamenjati z neko črko 'C'
-->

## Interpolacija

> ### NALOGA: Interpolacija
> Dobljene podatke vnesite v programsko orodje za delo s tabelami in podatke izrišite v grafični obliki. Nato dodajte ustrezen trend in izpišite enačbo prenosne funkcije.
> \
> Prenosna funkcija:
> \
> \
> \

## Izpis temperature (stand-alone DAQ)

> ### NALOGA: Izpis temperature
> V programskem orodju za tabele (Microsoft Excel ali LibreOffice Calc) podatkom priredimo ustrezno krivuljo in odčitamo koeficiente... Nato napišemo program:

```cpp
//            k0        k1        k2        k3        k4      k5
float k[6] = { -74.91, 530.963E-3, -1.685E-3, 3.253E-6, -3.128E-9, 1.227E-12};

void setup() {
  pinMode(15, OUTPUT);
  digitalWrite(15, HIGH);
  pinMode(16, OUTPUT);
  digitalWrite(16, LOW);
  pinMode(14, INPUT); //A0
  // initialize the serial communication:
  Serial.begin(9600);
}

void loop() {
  // send the value of analog input 0:
  int i;
  float CH1 = 0;
  for (i = 0; i < 64; i++) {
    CH1 += analogRead(A7);
    delay(3);
  }
  float Vol_CH1 = float(CH1 / 64.0);

  float Temp_CH1 = 0;
  for (int i = 0; i <= 5; i++) {
    Temp_CH1 += k[i] * pow(Vol_CH1, i);
  }
  Serial.println(Temp_CH1);
  //delay(1000);
}
```

