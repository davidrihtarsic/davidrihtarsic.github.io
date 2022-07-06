# POTENTIOMETER AS ANGLE SENSOR

## Tasks:

1. Add the potentiometer to the shaft of barrier gate. You can follow the instrucions in the [video](https://www.youtube.com/embed/kzLtVWtxVsQ).

![Adding potenciometer as an angle sensor.](https://img.youtube.com/vi/kzLtVWtxVsQ/maxresdefault.jpg){#fig:pot_sen}

<iframe width="410" height="337" frameborder="0" src="https://www.youtube.com/embed/kzLtVWtxVsQ"></iframe>

<iframe src="https://docs.google.com/presentation/d/1GgbUhsWBIflvZN1qMDrkh2tXRMLtYGoxHCdt5s_COVg/embed?authuser=0&hl=en&size=s" width="410" height="337" title="potenciometer" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

2. Test the potentiometer values with next program:

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(A3));
  delay(100);
}
```

3. Change the functions for lifting and lowering the barrier gate to use potenciometer readings instead of switch and time controlled movement.

```cpp
[+] void setup() {   
[+] void loop() {
[+] void manualGateControll(){
[+] void stopTheGate(){
[-] void moveGateUp() {
        int gate_orientation = analogRead(POTENTIOMETER_PIN);
        while (gate_orientation < 750){
            digitalWrite(MOTOR_PIN_1, HIGH);
            digitalWrite(MOTOR_PIN_2, LOW);
            gate_orientation = analogRead(POTENTIOMETER_PIN);
        }
        stopTheGate(); 
    }
[+] void moveGateDown() {
```
4. Advanced: Calculate the angle of barrier gate from the analog readings of potenciometer.

## Questions:

1.  What is the value of the angle sensor when the barrier gate is in the upper orientation\...
2.  \... and in lower orientation.

> ## Summary:
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

