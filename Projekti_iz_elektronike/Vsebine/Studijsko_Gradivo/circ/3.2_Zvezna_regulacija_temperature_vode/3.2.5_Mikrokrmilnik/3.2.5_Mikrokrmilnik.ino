#include <OneWire.h>
#include <DallasTemperature.h>

const int PIN_SENZOR = 10;  // vodilo 1-Wire (z uporom 4,7 kΩ proti 5 V)
const int PIN_GRELEC = 3;   // izhod PWM

const float T_REF = 41.0;   // želena temperatura v °C
const float K_P = 25.5;     // PWM-enote na kelvin (proporcionalno območje 10 K)

OneWire oneWire(PIN_SENZOR);
DallasTemperature senzor(&oneWire);

void setup() {
  senzor.begin();
}

void loop() {
  senzor.requestTemperatures();               // meritev temperature
  float T = senzor.getTempCByIndex(0);        // temperatura v °C

  int pwm = constrain((int)(K_P * (T_REF - T)), 0, 255);  // sorazmerni zakon
  if (T == DEVICE_DISCONNECTED_C) pwm = 0;    // senzor se ni javil: grelec izklopljen

  analogWrite(PIN_GRELEC, pwm);
}
