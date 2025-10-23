# END OF LINE DETECTION

## Tasks:

1. Stop the robot when it reaches the end of line.
2. Detecting the end of line can be done by measuring the time that robot spend over the black and white area. E.g. if the robot is driving along the line - the time spent over black and time spent over white area will be quite the same. When line ends the robot will not detect the black area soon and the time spent over white area will increase significantly - and that is the trigger for detecting the end of line.
3. Advanced: Make a function to align (move) the robot back to the line.

## Questions:

1.  How can we store a data to the controller\'s memory?
2.  How can we measure time in programming loops?
3. What is the purpose of the prog. instr. exit(0); ?

```cpp
#include "RobotMovingFunctions.h"
const int LIGHT_SENSOR_PIN = A0;
const int SURFACE_BRIGHTNESS_REFERENCE = 400;
int time_on_black = 0;
int time_on_white = 0;

void setup()
{
  setIOpins();
  pinMode(LIGHT_SENSOR_PIN , INPUT);
}
void loop()
{
  int light_sensor_value = analogRead(LIGHT_SENSOR_PIN );
  if ( light_sensor_value < SURFACE_BRIGHTNESS_REFERENCE )
  {
    // BLACK area
    moveLeft();
    time_on_white = 0;  // reset time on white
    time_on_black++;    // meas. time on black
    delay(100);
  }
  else
  {
    // WHITE area
    moveRight();
    // Do similar meas.
    // of time on white
    delay(100); 
    // If time is signif. longer:
    //        robotStop();exit(0);
  }
}
```
: Edn of Line Detection. {#lst:360_Edn_of_Line_Detection}

> ## Summary:
> ### <++>
>
> ## Issues:
> ### <++>
>
