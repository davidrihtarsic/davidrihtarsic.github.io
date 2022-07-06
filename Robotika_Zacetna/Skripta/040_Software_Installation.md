# SOFTWARE INSTALLATION

We will need softwate listed bellow:

1. [Arduino IDE](#arduino-ide) is basics "development environment"
2. [RobDuino](#RobDuino) library for easier programming
3. [Ardublockly](#ardublockly) is needed for introduction to programming
  + [Python](#python) is needed for running Ardublockly
4. [VSC in PlatformIO](#vsc-platformio) proper IDE include:
  + auto-completion,
  + error marking (e.g. forgotten \";\"),
  + auto-detect USB port, 
  + function information

## Arduino IDE

1. Go to Arduino web page Arduino->Software->[Download](https://www.arduino.cc/en/Main/Software).
2. Download [Arduino IDE 1.8.9](https://www.arduino.cc/en/Main/OldSoftwareReleases#previous) choose [Windows Install](https://www.arduino.cc/download_handler.php?f=/arduino-1.8.9-windows.exe)...
2. ... click `JUST DOWNLOAD`.
3. run `arduino-1.8.9.exe` and follow the instructions.
4. ... don't forget to install also 3rd party drivers (for Chinese version of Arduino UNO controller)... 
5. if you do forget... Try this [Russian drivers](https://www.5v.ru/zip/ch341ser(v34).zip) from [page](https://www.5v.ru/ch340g.htm).

### Getting started

1. Run `Arduino IDE`
2. Connect Arduino Uno controller to USB port.\
    `Arduino Uno`
3. Open simple basic program:\
    `files` -> `examples` -> `01.basics` -> `blink`

```c++
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}
```
4. Make this settings in `Tools` menu ->
    1. `Board:` Arduino/Genuino Uno
    2. `Port:` COM3 *or similar*

7. Run :\
    `Upload` to transfere the program to Arduino UNO controller.

8. If everything is OK you will get this message:

```
Done uploading.
Sketch uses 970 bytes (3%) of program storage space. Maximum is 32256 bytes.
Global variables use 9 bytes (0%) of dynamic memory, leaving 2039 bytes for local variables. Maximum is 2048 bytes.
```
9. Optional this preferences are suggested:  
`File` -> `Preferences`:
    1. `Editor Language`: English
    2. `Editor font size`: 20
    3. `Show verbose output during`: [ ]compiling [x] upload
    4. `[x] Display linenumbers`
    5. `[x] Enable code folding`

## RobDuino

RobDuino is Arduino library which include some usefull functions for driving motors and on-board key usage...

### RobDuino Library Installation

1. Download zip file:
   * [RobDuino-master.zip](https://github.com/davidrihtarsic/RobDuino/archive/master.zip)
2. rename RobDuino-master.zip in:
   * **RobDuino.zip**
3. run Arduino IDE
4. choose:
   * `Sketch` --> `Include Library` --> `Add .ZIP Library...`
5. find
   * `.../Download/RobDuino.zip`
   * `[OK]`

## Ardublockly

[Ardublockly](https://ardublockly.embeddedlog.com/) is [graphical programming environment](https://en.wikipedia.org/wiki/Visual_programming_language) for programming Arduino controllers. A demo version of the program is also available [on-line](https://ardublockly.embeddedlog.com/demo/#).

>Note: For actual programming you will need Arduino IDE installed.

>Note: For running Ardublockly you will need to install Python program.

### Python Installation

1. You will have to install [Python 3.7](https://www.python.org/) or grater. First [Download](https://www.python.org/downloads/) the newest version of Python.

2. Run installation file and set this settings:
    1. `[x] Add Python to PATH` in
    2. choose `Clasic Instalation`

### Ardublockly Installation

3. From [github.com/.../ardublockly](https://github.com/carlosperate/ardublockly) download **zip** file by clicking **Clone or download** and choosen [Download ZIP file](https://github.com/carlosperate/ardublockly/archive/master.zip).

4. Extract `ardublockly-master.zip` to dirrectory of your choice e.g. `C:\\Program Files(x86)`

5. That is it! Installation is complete.

#### Running Ardublockly

6. Find this file `C:\\Program Files(x86)\\ardublockly-master` and double-click on `start.py`. Python program should run and you should see:
    1. terminal window with some code running...
    2. and a new window should apear in your Internet Browser.
If this is will not happend try to run `start.py` with right mouse button and `Start program with` then choose `Python 3.7`.

### Settings

7. Click `menu` and choose `Settings`:
    1. `Compiler Location:` C:\\Program Files (x86)\\Arduino\\arduino_debug.exe
    2. `Arduino Board:` Uno
    3. `Com port:` COM3 *or appropriate one*
    4. Click `[RETURN]`.

## VSC in PlatformIO

>Note: For programming Arduino controllers you will need Arduino IDE installed.

[Download](https://code.visualstudio.com/download) installation file:

1. run `VSCodeUserSetup-ia32-1.49.3.exe` installation file.
2. run VSC program and click `Extensions`
3. search for `PlatformIO IDE` and 
4. run `Install`.
5. restart VSC or click `Reload now`.

### Getting Started

Write basic program `Blink`:

1. plug in Arduino Uno.
2. open `PlatformIO - Home Page`:
  - in left icon bar find `PlatformIO`
    + `QUICK ACCESS` -> `PIO Home` -> `Open`
3. choose `+ New Project`
4. Setup:
  - `Name:` ime_projekta
  - `Board:` Arduino UNO
  - `Framework:` Arduino Framework
5. click `Finish` 
6. Find directory `src` (e.g. `source code`), where you can find main program code in file `main.cpp`
7. Copy-Paste this example:
```cpp
#include <Arduino.h>
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13,HIGH);
  delay(500);
  digitalWrite(13,LOW);
  delay(500);
}
```
8. Run `Build` and `Upload`.

