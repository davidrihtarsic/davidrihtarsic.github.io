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

## NetworkManager

is a program for providing detection and configuration for systems to automatically connect to networks.
Včasih se mi zgodi, da povezava zamrzne in se ne morem povezati na internet, čeprav imam določen IP.

Navadno, ko vse dela je status od NetworkManager-ja takšen:

    systemctl status NetworkManager.service

> ● NetworkManager.service - Network Manager
>      Loaded: loaded (/usr/lib/systemd/system/NetworkManager.service; enabled; vendor preset: disabled)
>     Drop-In: /usr/lib/systemd/system/NetworkManager.service.d
>              └─NetworkManager-ovs.conf
>      Active: active (running) since Fri 2021-02-19 07:31:41 CET; 9min ago
>        Docs: man:NetworkManager(8)
>    Main PID: 411 (NetworkManager)
>       Tasks: 3 (limit: 19043)
>      Memory: 21.4M
>      CGroup: /system.slice/NetworkManager.service
>              └─411 /usr/bin/NetworkManager --no-daemon
>
> [1613716322.9445] dhcp4 (enp0s20f0u4u1): option requested_time_offset => '1'
> [1613716322.9445] dhcp4 (enp0s20f0u4u1): option requested_wpad       => '1'
> [1613716322.9445] dhcp4 (enp0s20f0u4u1): option routers              => '192.168.0.1'
> [1613716322.9445] dhcp4 (enp0s20f0u4u1): option subnet_mask          => '255.255.255.0'
> [1613716322.9445] dhcp4 (enp0s20f0u4u1): state changed unknown -> bound
> [1613716322.9468] device (enp0s20f0u4u1): state change: ip-config -> ip-check (reason 'none', sys-iface-state: 'managed')
> [1613716322.9503] device (enp0s20f0u4u1): state change: ip-check -> secondaries (reason 'none', sys-iface-state: 'managed')
> [1613716322.9508] device (enp0s20f0u4u1): state change: secondaries -> activated (reason 'none', sys-iface-state: 'managed')
> [1613716322.9576] device (enp0s20f0u4u1): Activation: successful, device activated.
> [1613716323.0618] policy: set 'Wired connection 1' (enp0s20f0u4u1) as default for IPv4 routing and DNS

Mogoče bi poskusil resetirat NetworkManager.service ? (morda prej poglej kakšen je status)

    systemctl restart NetworkManager.service

## Prioriteta povezave

NetworkManager ima tudi grafični vmesnik `nm-connection-editor`
kjer lahko nastavimo prioriteto posameznih povezav.

- `0` je najvišja povezava

Pot, ki jo povezava vzpostavi je opisana z:

    ip route get 8.8.8.8

> 8.8.8.8 via 192.168.0.1 dev enp4s0 src 192.168.0.17 uid 1000
>     cache

