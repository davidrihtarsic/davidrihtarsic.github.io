/********************************************************************************
TASK:
1. Construct the light sensor according to video:
   https://www.youtube.com/watch?v=wEN1e6m1FGY
   and scheme:
   https://docs.google.com/presentation/d/1nVl7aVy0qCZ7b6E-bIywXlQZ7PH8LOBB2sb2VxsBKR0/embed?hl=en&size=s&slide=id.p
   Add also the light bulb which will help to lightning the
   area under the robot.
2. To test the light sensor and light bulb run the next
   program and check the reported serial data:
3. Try different resistors (1k, 10k, 100k, 1M) and find out
   at which the sensitivity of the sensor is greatest.
QUESTIONS:
1. What is the value of the sensor when the robot is over white/black surface?
    High surface brightness (in ADC):
    Low surface brightness (in ADC):
2. Calculate the average between those two values.
    Surface brightness reference (in ADC):
READ MORE:
   https://davidrihtarsic.github.io/Robotika_Zacetna/Skripta/580_LigthSensor.html
***********************************************************************************/
const int LIGHT_SENSOR_PIN = A0;
const int BULB_PIN = 3;
const int HIGH_SURFACE_BRIGHTNESS = 0;
const int LOW_SURFACE_BRIGHTNESS = 0;
const int SURFACE_BRIGHTNESS_REFERENCE = 0;
void setup() {
  pinMode(LIGHT_SENSOR_PIN , INPUT);
  pinMode(BULB_PIN, OUTPUT);
  digitalWrite(BULB_PIN, HIGH);
  Serial.begin(9600);
}

void loop() 
{
  int light_sensor_value = analogRead(LIGHT_SENSOR_PIN );
  Serial.println(light_sensor_value );
  delay(200);
}
