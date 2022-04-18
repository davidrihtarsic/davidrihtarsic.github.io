const int POTENCIOMETER = 0;
void get_100_Samples();

void setup() {
  Serial.begin(9600);
  get_100_Samples();
}

void loop() {
}

void get_100_Samples(){
  for (int i = 0; i < 100; i++){
    int adc_value = analogRead(POTENCIOMETER);
    float voltage = (float)adc_value * 5 / 1023;
    Serial.println(voltage, 4);
    delay(10);
  }
}
