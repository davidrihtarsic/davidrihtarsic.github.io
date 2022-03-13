# UMERITEV SENZORJA

Vnos podatkov v Arduino:

    Serial.read();

    Serial.println(Serial.read());

```cpp
while (Serial.available()){
  Serial.println(Serial.read());
}
```

1 -> 49
2 -> 50
3 -> 51

```cpp
while (Serial.available()){
  Serial.println((char)Serial.read());
}
```

...če je "C" to je konec vnosa
```cpp
while (Serial.available()){
  char inData = (char)Serial.read();
  if (inData=='C'){
    Serial.print("\t");
    Serial.println(analogRead(0));
  }else{
    Serial.print(inData);
  }
}
```



## Umeritveni program

```cpp
void setup()
{
  Serial.begin(9600);
  Serial.println("T[°C]\tADC");
}

void loop()
{
  while (Serial.available()){
    char inData = (char)Serial.read();
    if (inData=='C'){
      Serial.print("\t");
      Serial.println(analogRead(0));
    }else{
      Serial.print(inData);
    }
  }
  
  delay(10); // Delay a little bit to improve simulation performance
}
```

## Podatke kopiramo v Excel
1. podatki
2. graf
3. trendna črta
4. enačba
ALI...za polinom 2. st.:
=LINEST(A2:A8,B2:B8^{1,2},1,0)

## Izračun polinomske vrednosti

```cpp
  // y = k₀*x⁰ + k₁*x¹ + k₂*x²
  //   k     k0    k1   k2
float k[3]={-52.089, 0.5036, -3.5912E-5};

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  // potrebujemo adc vrednost! to bo naš X (v programiranju naredimo daljše ime)
  int adc_value=analogRead(0);
  // in Y to bo naša izračunana vrednost
  float temp = 0;
  // IZRAČUN ?!?
  // y = k₀*x⁰ + k₁*x¹ + k₂*x²
  // x³ ->  pow(X,3);

  // VSOTA ZAPOREDNIH ČLENOV
  //  2
  //  ∑ ( k_i * x^i )
  // i=0
  for (int i=0;i<=2;i++){
    temp += k[i] * pow(adc_value,i);
  }
  Serial.println(temp);
  delay(100);
}
```




