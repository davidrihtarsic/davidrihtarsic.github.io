const char TRIGGER_PIN  = A0;
const char ECHO_PIN     = A1;

void setup()
{
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(9600);
}

int getPulseWidth_us()
{
  digitalWrite(TRIGGER_PIN,HIGH);
  delayMicroseconds(10); 
  digitalWrite(TRIGGER_PIN,LOW);
  return pulseIn(ECHO_PIN, HIGH);
}

float getDistance_cm()
{
  // do distance calculation here...
  return 0
}
void loop()
{
  float distance_cm = getDistance_cm();
  int duration_us = getPulseWidth_us();
  Serial.println(duration_us);
  delay(2000);
}
