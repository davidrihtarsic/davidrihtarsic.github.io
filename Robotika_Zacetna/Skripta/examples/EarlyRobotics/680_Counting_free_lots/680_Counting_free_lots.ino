/* TASKS:
1. Count the free lots and report the value to Serial output.
READ MORE:
*/
const int GATE_MOTOR_A = 6;
const int GATE_MOTOR_B = 7;
const int REF_SW_PIN = A0;
const int REED_SW_PIN = A1;
const int POTENTIOMETER_PIN = A3;
const int HORIZONTAL = 164;
const int VERTICAL = 511;

void stopTheGate();
void moveGateUp();
void moveGateDown();
void setIOpins();

void setup(){
  setIOpins();
}

void loop()
{
  int car_is_there = !digitalRead(REED_SW_PIN);
  if (car_is_there)
  {
    moveGateUp();
    delay(1000);
    moveGateDown();
  }
  delay(100);
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
  int potenciometer_value = analogRead(POTENTIOMETER_PIN);
  while (potenciometer_value < VERTICAL)  
  {
    potenciometer_value = analogRead(POTENTIOMETER_PIN);
  }
  stopTheGate();
}
void moveGateDown()
{
  digitalWrite(GATE_MOTOR_A, LOW);
  digitalWrite(GATE_MOTOR_B, HIGH);
  int potenciometer_value = analogRead(POTENTIOMETER_PIN);
  while (potenciometer_value > HORIZONTAL)
  {
    potenciometer_value = analogRead(POTENTIOMETER_PIN);
  }
  stopTheGate();
}
void setIOpins()
{
  pinMode(GATE_MOTOR_A, OUTPUT);
  pinMode(GATE_MOTOR_B, OUTPUT);
  pinMode(REF_SW_PIN, INPUT_PULLUP);
  pinMode(REED_SW_PIN, INPUT_PULLUP);
}
