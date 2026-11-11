void setup(){
	pinMode(11, OUTPUT);
}

void loop(){
	int pot_value = analogRead(A5);
	analogWrite(11, pot_value/4);
	delay(500);
}