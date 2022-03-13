/* TASKS:
1. Write new functions for driving the robot left and right
   with reduced power of the motors:
    - `robotLeftPWM();`
    - `robotRightPWM();`
    In one case you will might find yourself in trouble of
    controlling the power of the motor since both pins are
    not able to perform `PWM` output. In this case you can
    remember that the motor's power is 0 W also if both pins
    are in state of logical `1`.
2. Also add `analogWrite(LEFT_MOTOR_PIN_A, 0);` to function
	`robotStop()` to stop the `PWM` control of the motor.
    And do similar for the `right motor`.
3. Change the functions `robotLeft()` and `robotRight()` in
    S-R-A loop with new ones with less power on motors.
4. Add a parameter `PWM_value` to each function to set the
    `duty cicle` of the controlled output.
    - `robotLeftPWM(int PWM_value)`
    - `robotRightPWM(int PWM_value)`
QUESTIONS:
1. How can we control the average power of the motor?
2. How can we control the average power of the motor in both
    directions if we are not able to control `PWM` both
    output pins of the motor?
3. Explain the purpose of programming function
    `analogWrite(pin, pwm)`.
4. Explain the meaning of the `pin` and `pwm` parameters in
    function `analogWrite`.
READ MORE:
https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/585_PWM_motor_control.html
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

void loop()
{
  int light_sensor_value = analogRead(LIGHT_SENSOR_PIN );
  if (light_sensor_value > SURFACE_BRIGHTNESS_REFERENCE)
  {
    robotLeft();
  }
  else
  {
    robotRight();
  }
}
