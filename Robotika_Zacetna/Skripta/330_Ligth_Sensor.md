# LIGHT SENSOR

## Tasks:

1. Construct the light sensor according to [video](https://www.youtube.com/embed/wEN1e6m1FGY) and scheme. Add also the light bulb which will help to lightning the area beneath the robot.

![Mounting a light sensor.](https://img.youtube.com/vi/wEN1e6m1FGY/maxresdefault.jpg)

1. To test the light sensor and light bulb test this example code and check the reported serial data.

```cpp
const int LIGHT_SENSOR_PIN = A0;

void setup()
{
  pinMode(LIGHT_SENSOR_PIN , INPUT);
  Serial.begin(9600);
}

void loop()
{
  int light_sensor_value = analogRead(LIGHT_SENSOR_PIN );
  Serial.println(light_sensor_value );
  delay(200);
}
```
: Ligth Sensor. {#lst:330_Ligth_Sensor}

2. Try different resistors (1k, 10k, 100k, 1M) and find out at which the sensitivity of the sensor is greatest.

| Resistance | (black) Sensor value | (whithe) Sensor value | Sensor difference |
|-----------:|:--------------------:|-----------------------|-------------------|
|     1 kOhm |                      |                       |                   |
|    10 kOhm |                      |                       |                   |
|   100 kOhm |                      |                       |                   |
|     1 MOhm |                      |                       |                   |

Table: Testing the sensitivity of the light sensor. {#tbl:sensor_sensitivity}

## Questions:

1.  What is the value of the sensor when the robot is over white/black area?
    - ADC value on white:
    - ADC value on black:
2.  Calculate the average between those two values.
    - Average is:

<iframe width="410" height="337" frameborder="0" src="https://www.youtube.com/embed/wEN1e6m1FGY"></iframe>

<iframe src="https://docs.google.com/presentation/d/1nVl7aVy0qCZ7b6E-bIywXlQZ7PH8LOBB2sb2VxsBKR0/embed?authuser=0&hl=en&size=s" width="410" height="337" title="Constructing the light sensor" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

> ## Summary:
> 
> ### Sensors
> 
> Sensors are electronic devices which convert physical quantity into
> electrical quantity (usually voltage). In simplest setup, sensor can be
> constructed as voltage divider with two resistors - $R_1$ and $R_2$. One of
> the resistors is resistor with fixed resistance value (eg. $R_1=10k\Omega$).
> The second one is a bit special and it\'s resistance depends on some
> physical quantity (e.g. light, temperature, humidity\...). When
> combining those two resistors into such voltage divider the output of
> the voltage divider can be calculated as: 
> 
> $$ U_{Out} = \frac{R_1}{R_1 + R_2} U_0 $$
> 
> ## Issues:
> 
> ### *Value of the sensor is very small*  
> If the value of the sensor is less than 100 the resistance of $R_2$ (connected to GND) is to low in comparismant to the resistance of R_1 (connected to +5V).
>
> ### *Value of the sensor is large*  
> If the value of the sensor is grater than 900 the resistance of $R_2$ (connected to GND) is to hi in comparismant to the resistance of R_1 (connected to +5V).
>

