/* TASKS:
1. Set the IO pin dirrection for POTENTIOMETER_PIN.
2. Change the functions:
    - moveGateUp();
    - moveGateDown();
    to use potenciometer readings instead
    of switch and time controlled movement.
3. Advanced: Calculate the angle of barrier gate
    from the analog readings of potenciometer.
QUESTIONS:
1. What is the value of the angle sensor:
    - when the barrier gate is in the upper orientation and
    - when the barrier is in the horizontal orientation.
READ MORE:
https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/660_Potenciometer.html
*/
const int GATE_MOTOR_A  = 6;
const int GATE_MOTOR_B  = 7;
const int REF_SW_PIN    = A0;
const int REED_SW_PIN   = A1;

void stopTheGate();
void moveGateUp();
void moveGateDown();
void setIOpins();

void setup(){
  setIOpins();
}

void loop()
{
  bool car_is_there = !digitalRead(REED_SW_PIN);
  if (car_is_there)
  {
    moveGateUp();delay(3000);
    stopTheGate();delay(1000);
    moveGateDown();
  }
}
void stopTheGate()
{
  digitalWrite(GATE_MOTOR_A, LOW);
  digitalWrite(GATE_MOTOR_B, LOW);
}
void moveGateUp()
{
  digitalWrite(GATE_MOTOR_A, HIGH);
  digitalWrite(GATE_MOTOR_B, LOW);
}
void moveGateDown()
{
  do
    digitalWrite(GATE_MOTOR_A, LOW);
    digitalWrite(GATE_MOTOR_B, HIGH);
  while ( bool gate_is_open = !digitalRead(REF_SW_PIN))
  
  stopTheGate();
}

void setIOpins()
{
  pinMode(GATE_MOTOR_A, OUTPUT);
  pinMode(GATE_MOTOR_B, OUTPUT);
  pinMode(REF_SW_PIN, INPUT_PULLUP);
  pinMode(REED_SW_PIN, INPUT_PULLUP);
}
