/* TASK:

QUESTIONS:

READ MORE:
https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/399_FirstRide.html
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
