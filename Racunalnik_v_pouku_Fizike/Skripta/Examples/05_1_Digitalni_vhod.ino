const int TIPKA = A0;
const int LED = 13;

void loop(){
    bool tipka_je_pritisnjena = digitalRead(TIPKA);
    if (tipka_je_pritisnjena == 1)
        digitalWrite(LED, HIGH);
    else
        digitalWrite(LED, LOW);
}
void setup(){
    pinMode(TIPKA, INPUT);
    pinMode(LED, OUTPUT);
}
