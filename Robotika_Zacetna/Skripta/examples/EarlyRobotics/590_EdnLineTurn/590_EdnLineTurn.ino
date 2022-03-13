/* TASKS:
1. Stop the robot when it reaches the end of line.
2. Detecting the end of line can be done by measuring
  the time that robot spend over the black and white
  area. E.g. if the robot is driving along the line 
  the time spent over black and time spent over white
  area will be quite the same.
  When line ends the robot will not detect the black
  area soon and the time spent over white area will
  increase significantly. That is the trigger for
  detecting the end of line.
2. Advanced: Make a function to align (move) the robot
back to the line.
QUESTIONS:
1. How can we store a data to the controller's memory?
2. How can we measure time during the execution of
a programming loop?
3. What is the purpose of the prog. instr. exit(0); ?
READ MORE:
https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/590_EdnLineTurn.html
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

const int SURFACE_BRIGHTNESS_REFERENCE = 400;
int white_counter = 0;
int black_counter = 0;
void loop()
{
  int light_sensor_value = analogRead(LIGHT_SENSOR_PIN );
  if (light_sensor_value < SURFACE_BRIGHTNESS_REFERENCE)
  {
    robotLeft();
    delay(10);
    //count black_counter;
    //reset white_counter;
  }
  else
  {
    robotRight();
    delay(10);
  }
}
