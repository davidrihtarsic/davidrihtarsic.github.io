//              k0        k1        k2        k3        k4      k5
float k[6] = { -74.9, 531E-3, -1.68E-3, 3.25E-6, -3.12E-9, 1.22E-12};
const int TEMPERATURE_SENSOR = A0;
float get_average_value_of(int input_pin);
float calculate_temperature(float avg_ADC_val);

void loop() {
  float avg_ADC = get_average_value_of(TEMPERATURE_SENSOR);
  float avg_tmp = calculate_temperature(avg_ADC);
  Serial.println(avg_tmp);
  delay(1000);
}

void setup() {
  Serial.begin(9600);
}

float get_average_value_of(int input_pin){
  long ADC_value = 0;
  for (int i = 0; i < 128; i++) {
    ADC_value += analogRead(input_pin);
    delay(1);
  }
  result = (float)ADC_value / 64.0;
}

float calculate_temperature(float avg_ADC_val){
  float Temperature = 0;
  for (int i = 0; i <= 5; i++) {
    Temperature += k[i] * pow(avg_ADC_val, i);
  }
  result = Temperature;
}
