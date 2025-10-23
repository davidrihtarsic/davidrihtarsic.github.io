# S-R-A LOOP

S-R-A loop is repeating process where:

1. Seasoning,
2. Reasoning and
3. Acting

is involved during the procedure of controlling the robot. This is the most important part of software in robotics. Remember the `autonomous` control is `ability to perform intended tasks based on current state and sensing, without human intervention`.

## Tasks:

1. Using the S-R-A loop technique you should write the program in particular order:
    1.  Check the sensor. IF the bumper \...
    2.  \... Is pressed the robot has to stop/go back/turn.
    3.  \... Is not pressed the robot can drive forward.

    Test the [@lst:270_SRA_Loop] and **find out why the robot does not stop.** (Such mistake is quite often - can you fix it):

```cpp
#include "RobotMovingFunctions.h"
const int BUMPER_PIN = A0;
void setup()
{
  setIOpins();
  pinMode(BUMPER_PIN, INPUT);

  bool bumperIsPressed = digitalRead(BUMPER_PIN);
  if ( bumperIsPressed )
  {
    stopTheRobot();
  }
  else
  {
    moveForward();
  }
}
void loop()
{
}
```
: SRA Loop. {#lst:270_SRA_Loop}

2. Hint for fixing the [@lst:270_SRA_Loop]: _S-R-A must be a loop function!_

3. Write a program to drive the robot around the class and avoid the obstacles.

## Questions:

1. What for `S-A-R loop` stands for?
2. Mark all three basic S-A-R processes in previous code example.
3. Can the `line 7` of the [@lst:270_SRA_Loop] be written outside of `loop()` function? What would happened if so?

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

