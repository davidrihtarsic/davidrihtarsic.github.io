# BASIC ROBOT CONTROL

## Task: CONTROLLING THE MOTORS

1. Connect LEFT MOTOR to digital outputs:
    -   D7 and D6
2. Connect RIGHT MOTOR to digital outputs:
    -   D5 and D4

![DC motors connection.](./slike/DC_motor_connect_2.png){#fig:DC_motor_connect}

3. Now you can write the program to control both motors in order to move the robot FORWARD for 3 second and STOP.
4. Next you can write the program which will move the robot in several different directions:
    - forward
    - backward
    - turn left
    - turn right

## Questions:

1.  How many digital outputs you have to set in order to control the
    robot for specific move?
2.  How many different moves your robot can make?

> ## Summary:
> 
> ### Controlling the robot in two degrees of freedom
> 
> To controlling the robot in two degrees of freedom we need to control
> two motors. Since we have to set two digital outputs for each motor we
> have to set four digital outputs for each individual move.
> 
> ## Issues:
> 
> ### *When I change the direction of the robot the robot does not move as expected.*
> 
> Probably you did not set all of the outputs correctly. Remember that
> some outputs may have remained set in previous output state from taken
> action in previous task.  

