# PULSEVIEW

Program za prikaz napetosti na računalniku, nudi pa tudi analizo digitalnih signalov (zelo cul!).

## sigrok-cli

je terminalen program za zajem podatkov iz različnih naprav... naj bi šlo tudi s UNI-T UT71c, vendar mi ne rata...

Naprimer:

    sudo ./sigrok-cli-NIGHTLY-x86_64.AppImage --driver=uni-t-ut71c:conn=1a86.e008 --scan

> The following devices were found:
> uni-t-ut71c - UNI-T UT71C with 1 channel: P1

... kar je ok ... nekaj prepozna, vendar...

    sudo ./sigrok-cli-NIGHTLY-x86_64.AppImage --driver=uni-t-ut71c:conn=1a86.e008 -O analog --samples 5
>

... ne prikaže nič..

v programu PulseView pa UNI-T-ja niti ni med driver-ji

