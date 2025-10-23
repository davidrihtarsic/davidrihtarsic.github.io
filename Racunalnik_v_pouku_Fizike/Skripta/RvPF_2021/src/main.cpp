#include <Arduino.h>

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 100; i++)
  {
    int analogni_senzor = analogRead(A0);
    Serial.println(analogni_senzor);
  }
  

}

void loop() {
}