# ON-MODULE BUTTONS WITH PULL-UP RESISTORS

## Tasks:

1. Module RobDuino includes two \"on-board\" buttons which are connected from pin A4 and A5 to GND. This two buttons can allso be used but internal pull-up resistors must be turned on.
1. Add manual functionality to the automated barrier gate. Add the possibility to manually lift (e.g. press A4 button) and lower (A5 button) the barrier gate.

## Questions:

1.  \<++\>
2.  \<++\>

```cpp
const int MOTOR_PIN_1 = 7;
const int MOTOR_PIN_2 = 6;
const int REED_SW_PIN = A1;
const int ROBDUINO_BT_A4_PIN = A4;
const int ROBDUINO_BT_A5_PIN = A5;

[+] void setup() {   
[-] void loop() {
        bool car_is_detected = !digitalRead(REED_SW_PIN);
        if (car_is_detected){
            moveGateUp();
            delay(3000);
            moveGateDown();
        }
        manualGateControll();
    }
[-] void manualControll(){
        bool button_A4_is_pressed = !digitalRead(ROBDUINO_BT_A4_PIN);
        if (button_A4_is_pressed){
            gateUp();
        }
        // add code for the case if button_A5_is_pressed ...
    }
[+] void stopTheGate(){
[+] void moveGateUp() {
[+] void moveGateDown() {
```

> ##  Summary
> 
> ### <++>
> 
> <++>
> 
> ##  Issues
> 
> ### *<++>*
> 
> <++>  

