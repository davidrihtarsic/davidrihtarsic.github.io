/* TASKS:
1. Add a switch to detect the reference point of the barrier
    gate. Let the reference point be the closed position of
    the barrier. Follow the video instruction:
    https://www.youtube.com/watch?v=bmgUlj_rP3U
2. Connect the switch to the controller according to schematics.
    Note that the switch is connected to GND and pull-up resistor
    must be used.
3. Change the function `moveGateDown` to lower the barrier gate
    to reference switch position. Test the For-loop of lifting
    and lowering the gate.
QUESTIONS:
1. Why the detection of reference point is important?
READ MORE:
https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/620_ReferencePoint.html
*/

const int GATE_MOTOR_A = 6;
const int GATE_MOTOR_B = 7;
void moveGateUp()
{
  digitalWrite(GATE_MOTOR_A, HIGH);
  digitalWrite(GATE_MOTOR_B, LOW);
}

void moveGateDown()
{
  digitalWrite(GATE_MOTOR_A, LOW);
  digitalWrite(GATE_MOTOR_B, HIGH);
}

void stopTheGate()
{
  digitalWrite(GATE_MOTOR_A, LOW);
  digitalWrite(GATE_MOTOR_B, LOW);
}

void setIOpins()
{
  pinMode(GATE_MOTOR_A, OUTPUT);
  pinMode(GATE_MOTOR_B, OUTPUT);
}
void setup()
{
  setIOpins();

  for (int i = 0; i < 15; i++)
  {
    moveGateUp();delay(3000);
    stopTheGate();delay(1000);
    moveGateDown();delay(3000);
    stopTheGate();delay(1000);
  }
}

void loop()
{

}
