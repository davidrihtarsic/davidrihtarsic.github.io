# CONTROLLING THE ROBOT

## Tasks:

1. Set the directions of used pins for controlling the motors.
2. Write a simple program that follows next sequence:
    1. move the robot forward,
    2. do it for 3000 ms,
    3. and stop the robot.

## Questions:
You probably ended up with this solution ... Right?
```cpp
void setup() {
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);

  digitalWrite(7, HIGH);
  digitalWrite(6, LOW);
  digitalWrite(5, HIGH);
  digitalWrite(4, LOW);

  delay(3000);

  digitalWrite(7, LOW);
  digitalWrite(6, LOW);
  digitalWrite(5, LOW);
  digitalWrite(4, LOW);
}

void loop() {
}
```
: Move the robot forward. {#lst:move_fwd}

1. Is your code "easy readable" and
2. Why is this important?

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

