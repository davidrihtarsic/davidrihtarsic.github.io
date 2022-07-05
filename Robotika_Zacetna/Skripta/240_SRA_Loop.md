# S-R-A LOOP

S-R-A loop is repeating process where:

1. Seasoning,
2. Reasoning and
3. Acting

is involved during the procedure of controlling the robot. This is the most important part of software in robotics. Remember the `autonomous` control is `ability to perform intended tasks based on current state and sensing, without human intervention`.

## Tasks:

1. Write a program to drive the robot around the class and avoid the obstacles.
2. Using the S-R-A loop technique you should write the program in particular order:
    1.  Check the sensor. IF the bumper \...
    2.  \... Is pressed the robot has to stop/go back/turn.
    3.  \... Is not pressed the robot can drive forward.

```cpp
const int BUMPER_PIN = A0;
void setIOpins();
void robotForward();
void robotStop();
void robotLeft();
void robotRight();
void robotBackward();

void loop() {
  bool bumperIsPressed = digitalRead(BUMPER_PIN);
  if ( bumperIsPressed ){
    robotStop();
  }else{
    robotForward();
  }
}
[+]void setup() { ...
```
: Detecting the obstacle. {#lst:obstacle_detect}

## Questions:

1. What for `S-A-R loop` stands for?
2. Mark all three basic S-A-R processes in previous code example.
3. Can `line 4` of the previous code example be written outside of `loop()` function?

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

