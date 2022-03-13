/* TASK:
1. Start with this example of driving the robot
  for 3s forward and then for 3s backward.
2. Change the 69th line delay(3000) of the
  example into for-nex loop with 10 repetition,
  but with the same overall duration.
3. Add the code for blinking the LED in the
  for-next loop during the robot is driving backward.
QUESTIONS:
1. Show some examples of programming assignment statement!
2. What is the operator for assign the value to the variable?
READ MORE:
https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/440_DataTypes.html
*/
const int LEFT_MOTOR_PIN_A = 7;
const int LEFT_MOTOR_PIN_B = 6;
const int RIGHT_MOTOR_PIN_A = 5;
const int RIGHT_MOTOR_PIN_B = 4;

void robotForward()
{
  digitalWrite(LEFT_MOTOR_PIN_A, HIGH);
  digitalWrite(LEFT_MOTOR_PIN_B, LOW);
  digitalWrite(RIGHT_MOTOR_PIN_A, HIGH);
  digitalWrite(RIGHT_MOTOR_PIN_B, LOW);
}
void robotStop()
{
  digitalWrite(LEFT_MOTOR_PIN_A, LOW);
  digitalWrite(LEFT_MOTOR_PIN_B, LOW);
  digitalWrite(RIGHT_MOTOR_PIN_A, LOW);
  digitalWrite(RIGHT_MOTOR_PIN_B, LOW);
}
void robotLeft()
{
  digitalWrite(LEFT_MOTOR_PIN_A, LOW);
  digitalWrite(LEFT_MOTOR_PIN_B, LOW);
  digitalWrite(RIGHT_MOTOR_PIN_A, HIGH);
  digitalWrite(RIGHT_MOTOR_PIN_B, LOW);
}
void robotRight()
{
  digitalWrite(LEFT_MOTOR_PIN_A, HIGH);
  digitalWrite(LEFT_MOTOR_PIN_B, LOW);
  digitalWrite(RIGHT_MOTOR_PIN_A, LOW);
  digitalWrite(RIGHT_MOTOR_PIN_B, LOW);
}
void robotBackward()
{
  digitalWrite(LEFT_MOTOR_PIN_A, LOW);
  digitalWrite(LEFT_MOTOR_PIN_B, HIGH);
  digitalWrite(RIGHT_MOTOR_PIN_A, LOW);
  digitalWrite(RIGHT_MOTOR_PIN_B, HIGH);
}
void setIOs()
{
  pinMode(LEFT_MOTOR_PIN_A, OUTPUT);
  pinMode(LEFT_MOTOR_PIN_B, OUTPUT);
  pinMode(RIGHT_MOTOR_PIN_A, OUTPUT);
  pinMode(RIGHT_MOTOR_PIN_B, OUTPUT);
}
void setup()
{
  setIOs();

  robotForward();
  delay(3000);
  robotBackward();
  delay(3000);
  robotStop();
}

void loop()
{
}
