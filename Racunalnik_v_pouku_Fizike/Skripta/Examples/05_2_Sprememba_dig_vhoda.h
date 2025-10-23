void waitForInputChange(int INPUT_PIN){
    bool zacetno_stanje = digitalRead(INPUT_PIN);
    bool trenutno_stanje = zacetno_stanje;
    while (trenutno_stanje == zacetno_stanje)
        trenutno_stanje = digitalRead(INPUT_PIN);
}
