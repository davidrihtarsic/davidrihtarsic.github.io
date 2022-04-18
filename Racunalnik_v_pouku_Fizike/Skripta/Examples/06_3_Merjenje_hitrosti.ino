const int VRATA_1 = 7;
const int VRATA_2 = 8;
void wait_for_gate_change(int input_pin);
void print_time_difference(unsigned long start_time,
                           unsigned long stop_time);
void loop() {
  wait_for_gate_change(VRATA_1);
  unsigned long start_time = micros();
  wait_for_gate_change(VRATA_2);
  unsigned long stop_time = micros();
  
  print_time_difference(start_time, stop_time);
  Serial.println("Nova maritev...");
}

void setup() {
  pinMode(VRATA_1, INPUT);
  pinMode(VRATA_2, INPUT);
  Serial.begin(9600);
  Serial.println("Start...");
}

void wait_for_gate_change(int input_pin){
  bool zacetna_vrednost  = digitalRead(input_pin);
  bool trenutna_vrednost = zacetna_vrednost;
  
  while (trenutna_vrednost == zacetna_vrednost){
    trenutna_vrednost = digitalRead(input_pin);
  }
}
void print_time_difference(unsigned long start_time,unsigned long stop_time){
  unsigned long time_diff = stop_time - start_time;
  Serial.println(time_diff);
}
