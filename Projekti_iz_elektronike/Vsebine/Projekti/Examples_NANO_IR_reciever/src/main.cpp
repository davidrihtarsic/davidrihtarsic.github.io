/*
# Vezava IR sprejemnika TSOP1738
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
| [A7]     [D2] |
| [5V0]   [GND] |
| [RST]   [RST] o----|:. GND
| [GND]    [D0] |    [ TSOP1738 ]
| [Vin]    [D1] o----[1____2___3]---+5V
+---------------+          |
                          GND
*/
#include <Arduino.h>
void setup() {
  // put your setup code here, to run once:
  //Serial.begin(2400);
  pinMode(0, INPUT);
}

void loop() {
  // vključi Arduino v PC in ga daj na RST = 0
  // tako, da bo stalno v reset in bo delovala
  // le napravica za UART -> USB
  // Mogoče niti ni potrebno naložiti programa,
  // saj so v RST načinu vsi pini as INPUT.
}
