# NETWORK

Če želiš pogledat kdo in kaj je priklopen na tvojo mrežo lahko uporabiš:

    sudo netstat -tupl

in tako dobiš tele podatke:

    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 localhost:ipps          0.0.0.0:*               LISTEN      4606/cupsd
    tcp6       0      0 localhost:ipps          [::]:*                  LISTEN      4606/cupsd
    udp        0      0 224.0.0.251:mdns        0.0.0.0:*                           4760/brave --type=u
    udp        0      0 224.0.0.251:mdns        0.0.0.0:*                           4681/brave
    udp        0      0 224.0.0.251:mdns        0.0.0.0:*                           4760/brave --type=u
    udp6       0      0 [::]:43631              [::]:*                              1366934/us
    udp6       0      0 [::]:38582              [::]:*                              1366934/us
