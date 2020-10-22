# TESTING THE EQUIPMENT

## Basic testing in Arduino IDE

1. Connect the Arduino Uno to PC with proper USB cable.  
    `[Arduino Uno]` 
2. Open Arduino IDE program and open program with:  
    `Files -  Examples - 01. Basics - Blink.ino`
3. Make shure that you will set the proper settings (see [@fig:Arduino_basic_setup]). From the menu choose:  
    `Tools`-
    1.  `Board:` Arduino/Genuino Uno
    2.  `Port:` COM3

![Arduino basic setup.](./slike/Arduino_basic_setup.png){#fig:Arduino_basic_setup}

-   To upload the code you can click the icon `Upload`.  
    If the uploading was successful you will be prompted with the text
    like:  

> ```
> Done uploading.  
> Sketch uses 970 bytes (3%) of program storage space. Maximum
> is 32256 bytes. Global variables use 9 bytes (0%) of dynamic
> memory, leaving 2039 bytes for local variables. Maximum is
> 2048 bytes.
> ```

## Basic testing in Ardublockly

1. Connect the Arduino Uno to PC with proper USB cable.  
    `[Arduino Uno]` 
2. Run Ardublockly program. Which will be running as localhost and you will be using internet browser as IDE. The addres will be:  
    `http://localhost:8000/ardublockly/index.html`
3. In the left corner of the program you can find `[=] menu icon`. From where you can choose (Slide 2 and 3)  
    `[] Settings`:
    1.  `Compiler Location:` C:\\Program Files (x86)\\Arduino\\arduino\_debug.exe
    2.  `Arduino Board:` Uno
    3.  `Com port:` COM3
    4.  And press:`[ RETURN ]`
4. Finaly you can press button `PLAY` And if uploading was successful you will be prompted with the text (Slide 4):  

![Ardublockly basic setup.](./slike/Ardublockly_basic_setup.png){#fig:Ardublockly_basic_setup}

> ```
> Successfully Uploaded Sketch
> WARNING: Error loading hardware folder /home/david/Arduino/hardware/WAV8F.
> No valid hardware definitions found in folder WAV8F.
> Sketch uses 444 bytes (1%) of program storage space. Maximum is
> 32256 bytes. Global variables use 9 bytes (0%) of dynamic memory,
> leaving 2039 bytes for local variables. Maximum is 2048 bytes.
> ```

> ## Summary
> Before uploading the programming code always check that the right board and serial port are set.
>
> ## Issues
> **Ardublockly returns the Error id 55: Serial port Serial Port unavailable.**  
> Try to re-connect the Arduino board. Wait a moment, check the settings and choose the COM port again then try again.

# HELLO WORLD IN ARDUBLOCKLY

## Task:

1. Make a very simple program like setting the digital output bit D3 to logical state 1 or **HIGH**.
2. Send the program to Arduino controller.

![First program in Ardublockly.](./slike/Hello_World_Ardublockly_1.png){#fig:ardublockly_first}

## Questions:

1.  What is the voltage of the digital output pin D3?
2.  Try to compare and understand the C++ programming code in aside
    window.

> ## Summary
> Programming with programming blocks is a good starting point for beginners since humans are not good in handling to many informations at the same time.
>
> Having programming blocks aside with C code is nice and soft introduction of the code programming.
>
> ## Issues
> ...to do...
