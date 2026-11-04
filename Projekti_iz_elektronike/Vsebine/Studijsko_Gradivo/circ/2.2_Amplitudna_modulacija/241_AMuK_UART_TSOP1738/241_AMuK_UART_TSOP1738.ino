void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(1200);
}

void loop() {
  delay(100);
  Serial.print("M");
}
