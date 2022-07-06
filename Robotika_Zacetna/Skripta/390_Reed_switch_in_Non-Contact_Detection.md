# REED SWITCH IN NON-CONTACT DETECTION

## Tasks:

1. Add a reed switch to the front of the barrier gate to detect the car.
2. Connect the reed switch to the input pin A1 an GND.

![Adding reef switch sensor.](https://img.youtube.com/vi/3hhu11bBFXc/maxresdefault.jpg){#fig:reed_sw}

3. Write program as such that the gate barrier will open if car is detected. Some hints are showv in nex example code:

```cpp
const int MOTOR_PIN_1 = 7;
const int MOTOR_PIN_2 = 6;
const int REED_SW_PIN = A1;

[-] void setup() {
        pinMode(MOTOR_PIN_1, OUTPUT); //declaration of I/O pins
        pinMode(MOTOR_PIN_2, OUTPUT);    
        pinMode(REED_SW_PIN, INPUT_PULLUP);
    }
[-] void loop() {
        bool car_is_detected = !digitalRead(REED_SW_PIN);
        if (car_is_detected){
            moveGateUp();
            delay(3000);
            moveGateDown();
        }
    }
[+] void stopTheGate(){
[+] void moveGateUp() {
[+] void moveGateDown() {
```

## Questions:

1.  What is pull-up resistor?
2.  How can we turn on the internal pull-up resistor of the microcontroller?

<iframe width="410" height="337" frameborder="0" src="https://www.youtube.com/embed/3hhu11bBFXc"></iframe>

> ## Summary:
>
> ### <++>
>
> <++>
>
>## Issues:
>
>### *<++>*
>
><++>  

