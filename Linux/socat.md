# SOCAT

Multipurpose relay (SOcket CAT)

Preusmeri kakršenkoli data flow na karkoli:
- tpc -> bash
- ...

Meni pride prav za preusmeritev:

- UART -> BASH

tako da lahko arduino pošlje neko komando Lunxu in se ta izvrši.

To lahko naredim z ukazom:

    socat -dd /dev/ttyUSB0,raw,echo=0,crnl exec:/bin/bash,pty,stderr,setsid,sigint,sane
