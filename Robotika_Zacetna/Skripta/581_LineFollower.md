# LINE FOLLOWER

## Tasks:

1. Write the program to control the robot follow the line ( actually above the edge between black and white area ). Some programming hints you can find in example:

```cpp
void robotForward();
void robotStop();
void robotLeft();
void robotRight();
void robotBackward();
void setIOpins();

void setup() {
  setIOpins();
}

void loop()
{
  int light_sensor_value = analogRead(LIGHT_SENSOR_PIN );
  if ( light_sensor_value < treshold_value ){
      // do this if robot is over the black line

  } else {
      // do this if robot is over white area
     
  }
}
```
: Simple line-follower program. {#lst:prg-line}

## Questions:

1.  What is the program function to get the `light_sensor_value`?
2.  Determine the movements of the robot if the robot is over the black
    area and if the robot is over the white area.


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

