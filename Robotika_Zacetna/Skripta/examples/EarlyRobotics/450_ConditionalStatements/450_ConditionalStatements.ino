/************************************************************ TASK:
1. Construct the bumper of the robot with push-button-switch
  as is shown in this video instructions:
  https://www.youtube.com/watch?v=eWldNxh-q2c&t=11s
2. Connect the push-button-switch (PBSW) terminals with module
  RobDuino according to:
  https://docs.google.com/presentation/d/19d-8UN3UQ1HTpq4a4PhSgt14YnIC8EE5Y1nDjwUab2Y/embed?hl=en&size=s&slide=id.p
3. Test the push-button-switch function in the bumper with this example code.
4. Then... complete the program to turn OFF the LED when the bumper is not touching anything.
5. Next... Change IF statements into single one IF-THEN-ELSE statement.
QUESTIONS:
1. Check if the LED on the output terminal D3 is ON when the bumper is pressed.
2. Measure the voltage potencial at the terminal A0 when the bumper is pressed.
3. Explain when the curly braces `{}` are necessary in the if-statement.
READ MORE:
https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/450_ConditionalStatements.html
************************************************************/
const int BUMPER_PIN = A0;
const int TEST_BUMPER_LED_PIN = 3;
void setup()
{
  pinMode(BUMPER_PIN, INPUT);
  pinMode(TEST_BUMPER_LED_PIN, OUTPUT);
}

void loop()
{
  bool bumperIsPressed = digitalRead(BUMPER_PIN);
  if ( bumperIsPressed ) digitalWrite(TEST_BUMPER_LED_PIN, HIGH);
}
