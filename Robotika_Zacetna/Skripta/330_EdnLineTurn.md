# TURN AT THE END OF LINE

## Tasks:

1. Stop the robot when it reaches the end of line.
2. Detecting the end of line can be done by measuring the time that robot spend over the black and white area. E.g. if the robot is driving along the line - the time spent over black and time spent over white area will be quite the same. When line ends the robot will not detect the black area soon and the time spent over white area will increase significantly - and that is the trigger for detecting the end of line.
3. Advanced: Make a function to align (move) the robot back to the line.

## Questions:

1.  How can we store a data to the controller\'s memory?
2.  How can we measure time in programming loops?
3. What is the purpose of the prog. instr. exit(0); ?

```cpp
void setIOpins();
void robotForward();
void robotStop();
void robotLeft();
void robotRight();
void robotBackward();

int time_on_black = 0;
int time_on_white = 0;

void loop() {
  int lightSensorValue= analogRead(A1);
  if ( lightSensorValue < 400 ){
                       // BLACK area
    robotLeft();
    time_on_white = 0; // reset time on white
    time_on_black++;   // meas. time on black
    delay(100);
  } else {
                       // WHITE area
    robotRight();
                       // Do similar meas.
                       // of time on white
 
    delay(100);
                       // If time is signif.
                       // longer:
                       // robotStop();exit(0);
  }
}
[+] void setup() { ...
```
: End line tun. {#lst:end_ln_turn}

> ## Summary:
> ### <++>
>
> ## Issues:
> ### <++>
>
