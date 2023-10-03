# SEKVENČNA VEZJA

## D-flip-flop

D-flip-flop (D-ff) je pogosto uporabljen predvsem v dveh elektronskih funkcijah:

- kot nastavitneni/pomnilni register in
- kot pomikalni register.

D-ff je v obeh funkcijah uporabljen v periferni enoti USART mikrokrmilnika ATmega328. Enota
USART skrbi za serijsko komunikacijo UART, ki poteka po protokolu RS232. Blokovni prikaz oddajnega
dela USART enote prikazuje [@fig:UART_block_diagram].

![Blokovni prikaz sestava USART periferne enote krmilnika ATmega328.](./slike/UART_block_diagram.png){#fig:UART_block_diagram height=500px}

Oddajni del (Transmitter) USART enote je v splošnem sestavljen iz pomnilnega registra `UDRn` v katerega shranimo podatek, ki ga želimo poslati. Ta podatek se nato premakne v pomični register `Transmit Shift Register` (`TSR`). Nazadnje se prične faza pomikanja podatka proti serijskemu izhodu pomičnega registra. Med to fazo lahko z novim podatkom nastavimo pomični register `UDRn`. A ponovno nastavljanje registra `TSR` med samim pomikanjem `TSR` registra ni mogoče.

> ### NALOGA: Pomikalni register
> V simulacijskem programu (SimulIDE) načrtujte:
>
> - pomnilni register `UDRn` in
> - pomični register `TSR`.
>
> Oba registra naj boste zgrajena iz D-ff in naj vsebujeta 8 pomnilnih celic (8-bitni register).
> Krmiljenje napetosti prožitvenih signalov kot so `Enable` in `Clock` lahko zagotovite z napetostnimi viri (5V - on/off).

## T-flip-flop

T-flip-flop (T-ff) je pogosto uporabljen v sekvenčnih vezjih kot:

- dvojiški števnik in
- kot delitelj osnovnega urinega takta.

Kot slednja funkcija (deljitelj osnovnega takta) je tudi različica sekvenčnega vezja uporabljena v periferni enoti USART (glej [@fig:UART_block_diagram height=500px] - `Clock Generator`). Glede na to, da lahko z zaporedno vezavo T-ff delimo osnovni takt le s koeficienti: 2, 4, 8, 16 ... tudi razloži, zakaj so pri oddajanju podatkov po UART vodilu na voljo frekvence: 19200, 9600, 4800, 2400 ...

> ### NALOGA: Dvojiški števnik
> V simulacijskem programu (SimulIDE) sestavite:
>
> - 4-bitni dvojiški števnik (kaskadno vezani T-ff),
> - izhodne signale (D3, D2, D1 in D0) priključite na vhod 
> - integrirano vezje 74HC4511 (BCD -> 7 seg. LED) in izhode le teh
> - povežite na 7-segmentni LED prikazovljnik.

