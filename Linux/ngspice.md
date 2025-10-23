# NGSPICE

Open-source spice simulator.

## MODELS FOR NGSPICE

http://ngspice.sourceforge.net/modelparams.html

Velika izbira spice modelov raznoraznih elektronskih elementov.

## NGSPICE UKAZI

### PRIPRAVA NETLIST

najprej opišemo vezje... npr:

>   gnd---n0---V1+---n1---[ r1 ]---n2---|c1|---n0---gnd

r1 1 2 1k
c1 2 0 10u
V1 0 1 DC 5V

*potek simulacije za 20ms, step 0.02ms
.tran 0.02ms 20ms
.control
run
plot v(1)
.end
.END

### NAČIN SIMULACIJE

Časovni potek

        TRAN 0.0001 0.5s 0.45s 0.0001s

DC sprememba napetostnega vira

        DC V1 0V 5V 0.01V

AC sprememba frekvence vira

        AC Dec 500 0.1Hz 1kHz 

### DEFINIRANJE VIRA

vir lahko tudi definiramo kot AC

        V1 VIN 0 SIN(0V 1V 50Hz 0 0)

sprememba napetosti v času (vpišeš točke) `____1s/----\2s__`

        V1 VIN 0 pwl (0ms 0V 1s 0V 1.01s 5v 2s 5v 2.01s 0V)

### PRIKAZ REZULTATOV

izris vhodne napetosti

        plot V(some_node)

izris toka

        plot I()
        plot (V(VIN)-V(OUT)/1k)

