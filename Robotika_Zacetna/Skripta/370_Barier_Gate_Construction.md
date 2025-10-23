# BARRIER GATE CONSTRUCTION

## Tasks:

1. Construct the barrier gate according to [video](https://www.youtube.com/embed/5_eh7ojNH68) instructions.

![Constracting a barrier gate.](https://img.youtube.com/vi/5_eh7ojNH68/maxresdefault.jpg){#fig:gate_const}

2. Connect the motor to digital outputs D7 and D6,
   - declare meaningful constants for output pins,
   - write a function `setIOpins()` for settig output pins and
   - include it in setup() function.
3. Write 3 time controlled functions for essential control
    of the barrier gate :
    - `moveGateUp();`
    - `moveGateDown();`
    - `stopTheGate();`
    and test this actions in setup() function.
4. Put this action of lifting and lowering the gate in
    For-loop and repeat it several times (e.g. 15 times).

Some sample code can be found in next example:

```cpp
const int MOTOR_PIN_1 = 7;
const int MOTOR_PIN_2 = 6;

[-] void setup() {
        pinMode(MOTOR_PIN_1, OUTPUT); //declaration of I/O pins
        pinMode(MOTOR_PIN_2, OUTPUT);    

        moveGateUp();                 // Lift the barrier.
        delay(3000);                  // Wait a bit...
        moveGateDown();               // Lower the barrier.
    }
[+] void loop() {
[+] void stopTheGate(){
[-] void moveGateUp() {
        digitalWrite(MOTOR_PIN_1, HIGH);
        digitalWrite(MOTOR_PIN_2, LOW);
        delay(1000);
        stopTheGate(); 
    }
[+] void moveGateDown() {
```

## Questions:
1. What is the time for raising and lowering the barrier?
    Compare it to your colleague's value.
2. What is the disadvantage of time controlled loop?

<iframe width="410" height="337" frameborder="0" src="https://www.youtube.com/embed/5_eh7ojNH68"></iframe>

> ## Summary
> 
> ### <++>
> 
> <++>
> 
> ## Issues:
> 
> ### *<++>*
> 
> <++>

