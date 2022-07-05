# DIGITAL INPUT

-   In sake to detect the obstacles we have to equip robot with the
    \"touch sensor\". This sensor is basically a switch or key, which
    toggles it\'s output between GND and +5 V voltage potentials.
-   Follow [video instructions](https://www.youtube.com/embed/eWldNxh-q2c)
    to construct bumper in front of the robot.

## Questions:

1.  Do you hear \"clicking\" sound when you push the bumper?
2.  Name the mechanical mechanism where smaller force on one end can
    cause greater force on the other end of the mechanism.

<iframe width="410" height="337" frameborder="0" src="https://www.youtube.com/embed/eWldNxh-q2c"></iframe>

## Tasks: CONNECT THE SWITCH

The key has three connecting terminals. Each of one is marked with the
number 1, 2 or 3. Connect them in right order. Connect the key terminals
in order that are specified in presentation and listed as:

1. connect to RobDuino C0 terminal.
2. connect to RobDuino voltage terminal GND.
3. connect to RobDuino voltage terminal +5V.

## Questions:

1. What is the output voltage of the sensor when the robot is (or is NOT) touching the obstacle?
2. How many different states are presented at the output of the sensor?
3. Name several more examples where digital sensor can take place.

<iframe src="https://docs.google.com/presentation/d/1Sw-3ovX36DYt9zcj6z9gESie3ZJwWLExb9KPddrw9JM/embed?authuser=0&hl=en&size=s" width="410" height="337" title="Connecting the key" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

<!--
![test](https://slides.googleapis.com/v1/presentations/1Sw-3ovX36DYt9zcj6z9gESie3ZJwWLExb9KPddrw9JM/pages/gb54165725_0_2}/thumbnail)
-->
> ## Summary:
> 
> ### Digital sensors
> 
> The output of a digital sensor can be just in two states:
> 
> -   logical \"0\" - presented in voltage as 0 V.
> -   logical \"1\" - presented in voltage as +5V.
> 
> ## Issues:
> 
> ### *Robot has no power since I connected the key as a sensor.*
> 
> Probably the key or switch is connected wrong and there is short connection between the GND and +5V voltage terminals. Unconnect the key or switch and verify if the power is back.

## Tasks: READING DIGITAL INPUT

1. Write the program shown in the presentation to test the readings of the digital sensor.
1. Then ... complete the program to turn OFF the LED when the bumper is not touching anything.
1. Next ... Change IF statements into single one IF-THEN-ELSE statement.
1. Advanced ... Solve the problem without IF statement.

## Questions:

1.  Check if the LED on the output terminal D3 is turend ON when the
    bummper is pressed.

<iframe src="https://docs.google.com/presentation/d/1NVtol-a0tmlgl00VwCACQIcAOOty3KYEMSgUFkf8-Aw/embed?authuser=0&hl=en&size=s" width="410" height="337" title="Testing Digital Input" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

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

