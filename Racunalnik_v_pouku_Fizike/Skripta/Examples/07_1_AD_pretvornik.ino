const int POTENCIOMETER = 0;
void setup() {
    Serial.begin(9600);
}

void loop() {
    int adc_value = analogRead(POTENCIOMETER);
    Serial.println(adc_value);
    delay(100);
}
```
