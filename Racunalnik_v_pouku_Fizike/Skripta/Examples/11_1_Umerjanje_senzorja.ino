const int TEMPERATURE_SENSOR = A0;
void wait_for_user_to_entry_data();
void print_average_value_of(int input_pin);

void loop() {
  wait_for_user_to_entry_data();
  print_average_value_of(TEMPERATURE_SENSOR);
}

void setup() {
  Serial.begin(9600);
  Serial.println("###########################################");
  Serial.println("# INSTRUCTIONS:                           #");
  Serial.println("#   1. Insert temperature (example: 22.4) #");
  Serial.println("#   2. then press ENTER                   #");
  Serial.println("#   3. repeat steps 1. and 2. ...         #");
  Serial.println("# When you are done with calibration:     #");
  Serial.println("#   4. Copy data to spreadsheet.          #");
  Serial.println("#   5. Add some polynome to the points.   #");
  Serial.println("#   6. Insert coeficients into file:      #");
  Serial.println("#       'temperature.ino'                 #");
  Serial.println("###########################################");
  Serial.print("T[°C]");Serial.println("\tADC Value");
}

void wait_for_user_to_entry_data(){
  bool data_entry_is_complete = false;
  while (!data_entry_is_complete){
    if (Serial.available()){
      char inChar = Serial.read();
      if (inChar == '\n')
        data_entry_is_complete = true;
      else
        Serial.print(inChar);
    }
  }
}

void print_average_value_of(int input_pin){
  Serial.print("\t");
  long ADC_value = 0;
  for (int i = 0; i < 128; i++){
    ADC_value += analogRead(input_pin);
    delay(1);
  }
  float avg_ADC_val = (float)ADC_value/128;
  Serial.println(avg_ADC_val);
}
