#include <Arduino.h>
#include <TimerOne.h>

/*
# Vezava IR diode
+-----[USB]-----+
| [13]    [D12] |
| [3V3]   [D11] |
| [Aref]  [D10] |
| [A0]     [D9] |
| [A1]     [D8] |
| [A2]     [D7] |
| [A3]     [D6] |
| [A4]     [D5] |
| [A5]     [D4] |
| [A6]     [D3] |
| [A7]     [D2] o--[220]---+--|>|--+
| [5V0]   [GND] |           IR LED |
| [RST]   [RST] |                  |
| [GND]    [D0] |                  |
| [Vin]    [D1] o------------------+
+---------------+

*/
bool state;
int FM_pin = 2;

void nosilnaFrekvenca(){
  state = !state;
  digitalWrite(FM_pin, state);
}
void setup() {
  Serial.begin(2400);
  Timer1.initialize(17); //13-> 38kHz , 17 -> 30kHz
  Timer1.attachInterrupt(nosilnaFrekvenca);
  pinMode(FM_pin, OUTPUT);
}

void loop() {
  delay(1000);
  Serial.print("A");
}
