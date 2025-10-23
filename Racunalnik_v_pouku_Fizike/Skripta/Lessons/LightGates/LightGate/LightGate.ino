void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(A0, INPUT_PULLUP);
  pinMode(A1, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(2, HIGH);
  digitalWrite(3, HIGH);
  delay(100);

  // measurement ....
  while (digitalRead(A1) == 0) {}
  unsigned long t_0 = millis();
  digitalWrite(3, LOW);
  while (digitalRead(A0) == 0) {}
  unsigned long t_1 = millis();
  digitalWrite(2, LOW);
  // done...
  
  int time_diff = t_1 - t_0;            //microseconds
  float distance = 30;                  //micrometers
  float speed = distance/time_diff*100; //speed

  Serial.print(time_diff);Serial.print("\t");Serial.print(speed);Serial.println(" cm/s");
  delay(2000);
}
