/* TASKS:
1. Add the potentiometer to the shaft of the barrier gate.
    You can follow the instructions in the video:
    https://www.youtube.com/watch?v=kzLtVWtxVsQ
2. Wire the potentiometer accordint to schematics:
   https://docs.google.com/presentation/d/1GgbUhsWBIflvZN1qMDrkh2tXRMLtYGoxHCdt5s_COVg/embed?hl=en&size=s&slide=id.p
3. Test the program and verify the Serial output.
QUESTIONS:

READ MORE:
https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/660_Potenciometer.html
*/
const int POT_PIN = A3;
void setup()
{
  Serial.begin(9600);
  pinMode(POT_PIN, INPUT);
}

void loop()
{
  int potentiometer_value = analogRead(POT_PIN);
  Serial.println(potentiometer_value);
  delay(100);
}
