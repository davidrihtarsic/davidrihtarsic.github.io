# PID CONTROL

text for some intro to new lecture unit

## Tasks:

1. <++>
2. <++>
```cpp
void zapornicaDol_PID(){
  zapornicaDol();
  int orientacija = analogRead(A0);

  //PI regulacija
  int P = 0;
  float I = 0;

  while (orientacija > spodnja_meja){
    orientacija = analogRead(A0);
    P = orientacija - spodnja_meja;
    I += 0.001 * P;
    int moc_motorja = P+I;
    if (moc_motorja > 255) moc_motorja = 255;
    analogWrite(6, moc_motorja);
    Serial.print("0,1023,");Serial.print(orientacija);Serial.print(",");Serial.println(spodnja_meja);
  }
  zapornicaStop();
}
```


3. <++>

## Questions:

1. <++>
2. <++>
3. <++>

> ## Summary:
> ### <++>
>
> ## Issues:
> ### <++>
>
