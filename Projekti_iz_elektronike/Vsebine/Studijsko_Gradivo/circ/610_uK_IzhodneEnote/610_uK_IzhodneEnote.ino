
void setup()
{
	delay(1000);
	pinMode(13,OUTPUT);
	digitalWrite(13, 1);
	delay(3000);
	digitalWrite(13, 0);
	delay(3000);

/*	
	Poglejmo kako so nastavljeni
	delovni registri mikrokrmilnika
	
	DDRB = 0B00100000;
	PORTB = 0B00100000;
	delay(3000);
	PORTB = 0B00000000;
*/
}

void loop()
{

}