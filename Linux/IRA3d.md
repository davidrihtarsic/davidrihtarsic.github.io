# IRA3D

imamo IRA3d printer. Za modeliranje uporabljam FreeCAD, za slicer pa CURA

## CURA nastavitve printerja:

X(Width): 250mm
Y(Width): 250mm
Z(Width): 300mm

Build plate shape: Rectangular
Heated bed: [x]

G-code flavor: Marlin

Start G-code:

    ;####################################
    ; Basic Movement settings
    ;####################################
    M92 X79.19 Y79.19   ; XY steps/mm
    M92 Z793.65         ; Z  steps/mm
    M92 E746.00         ; Extruder st/mm
    M204 P300           ; proba kocka_20_20 Acceleration Printing 300 m/s²
    ;####################################
    ; ne vem, če tole sploh rabm?
    ;####################################
    G90 		; abs mode
    G28 		; home
    G92 E0 		; reset E koordinate
    M140 S65		; prea heat bed
    M104 S180 T0	; preaheat E1 and E2
    M104 S190 T1
    ;M109 S180 T0
    M109 S190 T1	; wait E2
    M190 S65		; wait bed
    G1 F900 X50 E3.215	; 50 mm crte v X
    G1 Z50		; odmik mize
    ;--------

End G-code:

    ;----
    G91         ; relatvne koordinate
    G1 Z50      ; odmakni mizo
    G90         ; abs koordinate
    G1 Y180     ; nazaj
    M104 S0 T0	; ugasni gretje 1
    M104 S0 T1	; ugasni gretje 2
    M106 S255	; vent. na 100%
    M190 R45	; wait bed 45C
    M140 S0	; vent off
    M106 S0	; vent off
    ;-------

## Extruder 2

Compatible material diameter: 2.0mm
Nozzle offset: 22 mm

## CURA - Printing settings

Nekaj očitnih nastavitev:
Printing temperature  : 190°C
Bed temperature       : 60°C
Printing speed        : 50mm/s

Build plate adhesion  : Brim

## G-CODE (Marlin)

First created in 2011 for RepRap and Ultimaker by Erik van der Zalm et. al., today Marlin drives most of the world's 3D printers. Reliable and precise, Marlin delivers outstanding print quality while keeping you in full control of the process.

## Horizontal expansion

Ker se filament nekoliko bolj razleze na samih robovih objekta, je potrebno to upoštevati, če želimo doseči točne mere printanja.
V CURA-i to nastavimo s parametrom

    Shell
      [x] Horizontal expansion
      [x] Initial Layer horizontal expansion

Pri printerju IRA3d je bilo to potrebno nastaviti na '0.15mm', ker so bile luknje za cca 0.3mm prevelike.

## Pomik koračnih motorjev

Printtanje kvadra dimenzij 140x5x5 mm
Naprintan: 139.2mm x 4.94mm x 5.18 mm
140mm ... 139.2mm
x ....... 
78.74 s/mm * 140mm = 11023.6 stps
Naredil je  11023.6 korakov, moral bi jih pa več
= > 79.1925 steps/mm

    M92 X79.19 Y79.19 Z800.00 E828.78

> to naj bi blo flov na 95% in višina mal manjša

    M92 X79.19 Y79.19 Z793.65 E746.00

> mislim, da bi bilo potrebno korak še malo šovečat, ker se kar precej skrči...
> mogoče na X80 Y80 Z792 E746
>



