/* TASKS:
1. Set the SURFACE_BRIGHTNESS_REFERENCE value based on the average
  measured values from the surface brightnes (line 68).
2. Write the program to control the robot follow the line 
  (actually above the edge between black and white area ).
QUESTIONS:
1. Which program function will get the value of tne light sensor?
2. Write program statements to move the robot properly:
  - if the robot is over the black area and
  - if the robot is over the white area.
READ MORE:
https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/581_LineFollower.html
*/

const int LEFT_MOTOR_PIN_A = 7;
const int LEFT_MOTOR_PIN_B = 6;
const int RIGHT_MOTOR_PIN_A = 5;
const int RIGHT_MOTOR_PIN_B = 4;
const int LIGHT_SENSOR_PIN = A0;
const int BULB_PIN = 3;

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
void setup()
{
  pinMode(LEFT_MOTOR_PIN_A, OUTPUT);
  pinMode(LEFT_MOTOR_PIN_B, OUTPUT);
  pinMode(RIGHT_MOTOR_PIN_A, OUTPUT);
  pinMode(RIGHT_MOTOR_PIN_B, OUTPUT);
  pinMode(BULB_PIN, OUTPUT);
  digitalWrite(BULB_PIN, HIGH);
  pinMode(LIGHT_SENSOR_PIN, INPUT);
}

const int SURFACE_BRIGHTNESS_REFERENCE = 0;

void loop()
{
  int light_sensor_value = analogRead(LIGHT_SENSOR_PIN );
  // write conditional statement here...
}
