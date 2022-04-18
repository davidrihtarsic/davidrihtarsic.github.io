const int TIPKA = 7;
void randomly_turn_LED_on();
void start_timing_user_respond();
void reset_the_game();

void loop() {
  randomly_turn_LED_on();
  start_timing_user_respond();
  reset_the_game();
}

void setup() {
  pinMode(LED_BUILDIN ,OUTPUT);
  pinMode(TIPKA       ,INPUT);
  Serial.begin(9600);
  Serial.println("Start...");
  randomSeed(analogRead(0)); 
}

void randomly_turn_LED_on(){
  digitalWrite(LED_BUILDIN,LOW);
  delay(random(5000,10000));
  digitalWrite(LED_BUILDIN,HIGH);
}

void start_timing_user_respond(){
  unsigned long start_time = micros();
  unsigned long stop_time = 0;

  while (digitalRead(TIPKA) == 0){
    stop_time = micros();
  }

  unsigned long time_div = stop_time - start_time;
  Serial.println(time_div);
}

void reset_the_game(){
  while (digitalRead(TIPKA) == 1){
    delay(200);
    Serial.println("spusti tipko...");
  }
  Serial.println("Start...");
}
