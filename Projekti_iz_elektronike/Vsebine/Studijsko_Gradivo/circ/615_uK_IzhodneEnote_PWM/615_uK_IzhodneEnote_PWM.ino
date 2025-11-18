
void setup()
{
  pinMode(11,OUTPUT);
  digitalWrite(11, 1);
}

void loop()
{
  digitalWrite(11, 1);
  delay(500);
  digitalWrite(11, 0);
  delay(500);
}
