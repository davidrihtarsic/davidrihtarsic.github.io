/* TASKS:
1. Add the read switch to detect a car, acc. to video instructions:
    https://www.youtube.com/watch?v=3hhu11bBFXc
2. Do the wireing similar to reference switch, but to A1 controller's
    terminal.
3. Write S-R-A loop where the barrier gate will be lifted
    only if a car will be detected by the reed switch.
QUESTIONS:
1. What is S-R-A loop? Explain.
READ MORE:
https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/640_Reed_switch.html
*/
const int GATE_MOTOR_A = 6;
const int GATE_MOTOR_B = 7;
const int REF_SW_PIN = A0;
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
  digitalWrite(GATE_MOTOR_A, LOW);
  digitalWrite(GATE_MOTOR_B, HIGH);
  int gate_is_closed = !digitalRead(REF_SW_PIN);
  while ( !gate_is_closed )
  {
    gate_is_closed = !digitalRead(REF_SW_PIN);
  }
  stopTheGate();
}
void setIOpins()
{
  pinMode(GATE_MOTOR_A, OUTPUT);
  pinMode(GATE_MOTOR_B, OUTPUT);
  pinMode(REF_SW_PIN, INPUT_PULLUP);
}
void setup()
{
  setIOpins();

}

void loop()
{

}
