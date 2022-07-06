# ANALOG INPUT

## Tasks:

1. Unmount robot's bumper and all connections to the switch.
2. Equip the robot with distance sensor according to [video](https://www.youtube.com/embed/ELYsyuhbQfY) and scheme (see [@fig:distance_sen]).

![Mounting possition of analog distance sensor.](https://img.youtube.com/vi/ELYsyuhbQfY/maxresdefault.jpg){#fig:distance_sen}

3. Copy & Paste next program and check the output of distance sensor in Serial monitor.

```cpp
const int DIST_SEN_PIN = A0;
void setup()
{
  pinMode(DIST_SEN_PIN, INPUT);
  Serial.begin(9600);
}
void loop()
{
  int distance = analogRead(DIST_SEN_PIN);
  Serial.println(distance);
  delay(1000);
}
```
: Measuring analog voltage. {#lst:adc_measurement}

4. From the [datasheet](https://www.farnell.com/datasheets/1657845.pdf) for the distance sensor try to code the function for measuring the distance in cm. According to documentation there is almost linear trend between output voltage and $distance^{-1}$. Thus we can get good result with [@eq:calc_disd].

$$ distance^{-1}[cm] = 0.045 V_{out} $${#eq:calc_disd}

Next example can be your guide to code the function.

```cpp
float getDistance_cm()
{
  int volt_out = analogRead(DIST_SEN_PIN);
  float distance = 1/(0.045 * volt_out);
  return distance;
}
```

## Questions:

1. What kind of values do you getting from the reading of the distance sensor with the function `analogRead(A0)`?
2. Find the reasonable value where you should stop the robot.
3. Measure the voltage potencial of the sensor's output.


<iframe width="410" height="337" frameborder="0" src="https://www.youtube.com/embed/ELYsyuhbQfY"></iframe>

<iframe src="https://docs.google.com/presentation/d/1j4yvBeTajgG9wFb5mw9SUPUTLXjPWNWjOnINUEmyAx8/embed?authuser=0&hl=en&size=s" width="410" height="337" title="Conection of distance sensor" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

> ## Summary:
> 
> ### Analog to digital converter - ADC
> 
> ADC is an electronic sistem that converts analog signal (voltage) to a
> digitalized values. In our particular case the range of an analog
> voltage from 0V to 5V is converted to range of numbers from 0 to 1023.
> 
> ## Issues:
> 
> ### *<++>*
> 
> <++>  

