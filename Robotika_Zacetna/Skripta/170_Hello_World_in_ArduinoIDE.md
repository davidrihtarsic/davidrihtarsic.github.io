# HELLO WORLD IN ARDUINO IDE

## Tasks:

1. Make a very simple program like setting the digital output bit D3 to logical state 1 or **HIGH**.

```cpp
void setup() {
  // put your setup code here, to run once:
  pinMode(3, OUTPUT);
  digitalWrite(3, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:

}
```
: Hello World in ArduinoIDE. {#lst:170_Hello_World_in_ArduinoIDE}

2. Send the program to controller Arduino UNO .

## Questions:

1.  Explain the purpose of next programming characters in presented example:
    1. `;`
    2. `{  }`
    3.  `pinMode(3, OUTPUT);`
    4.  `digitalWrite(3, HIGH);`
    3.  `// put your ...`
    5.  `void setup()`
    6.  `void loop()`

> ## Summary:
> 
> ### Using curly braces - \{ and \}
> 
> Using curly braces in C++ is important part of riting the programming code. Imagine that you want to merge several members of programing code to a single pile. As we would separate pencils into one pile and markers to another - to be more organized. In real life we would do by elastic bundle or rope. If you have to choose single character from the keyboard to indicate that several members are combined to the same pile - which character would you choose? Probably curly braces {} are the best choice.
> 
> ### Function Definition
```cpp
   void loop() {

   }
```
> ### Function Call
```cpp
    digitalWrite(3, HIGH);
```
> ### Function Name
> 
> Function name should be stacked together from 2 - 5 short words that uniquely describing the functionality of the function. The first word should start with lower case and all the others words following should start with upper case. Some examples should be:
```cpp
   badname(); 
   goodFunctionName(); 
```
> ## Issues:
> 
> ### *Error: expected ';' before 'something'*
> 
> Probably you forgot to put ; (semicolon) at the end of the command. Find the row starting with \"**something**\" and look the row above\...  probably missing \"**;**\".  
>
> ### *Light at the digital output D3 is not ON.*
>
> Check if the enable switch fot the digital outputs is at the right position (ENABLE).

