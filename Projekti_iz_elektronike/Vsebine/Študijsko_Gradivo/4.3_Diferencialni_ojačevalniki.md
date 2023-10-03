DIFERENCIALNI OJAČEVALNIKI 
--------------------------------------------------------------------------------

Predstavljajte si prenos signala na daljše razdalje:

```
  A                      B
+---+                  +---+
| > |------------------| > |
+-+-+                  +-+-+
  |                      |
 GND                    GND'
```

Če sta potenciala $GND$ in $GND_1$ različna ($GND \neq GND_1$) zaradi kakršnega koli razloga, tedaj nepravilno odčitamo vrednost napetostnega potenciala v točki $B$  glede
na točko $A$.

To težavo lahko rešimo z diferencialnim signalom:

```
  A                      B
+---+                  +---+
| > |------------------| > |
|   |o-----------------|   |
+-+-+                  +-+-+
  |                      |
 GND                    GND'
```

kjer signal pošiljamo po enem vodniku, po drugem pa njegovo negacijo (ali protifazno vrednost). Tako je razlika obeh signalov neodvisna od potencialov $GND$ in $GND_1$. Ta
tehnika se uporablja že od leta 1920 in je do danes ena najpogostejših tehnik
za zagotavljanje zanesljive podatkovne povezave z visoko odpornostjo na 
zunanje elektromagnetne motnje (uporablja se v protokolih kot so: [Ethernet](https://wiki.networksecuritytoolkit.org/index.php/LAN_Ethernet_Network_Cable), [USB](https://en.wikipedia.org/wiki/USB_hardware), [HDMI](https://en.wikipedia.org/wiki/HDMI), [CAN](https://en.wikipedia.org/wiki/CAN_bus), [RS485](https://en.wikipedia.org/wiki/RS-485), ... )

### Osnovna izvedba diferencialnega ojačevalnika (odštevalni sistem z o.o.) 

* Elektrometrski diferencialni ojačevalnik

### Instrumentacijski ojačevalnik s tremi operacijskimi ojačevalniki

* Instrumentacijski ojačevalniki v integriranih vezjih 

