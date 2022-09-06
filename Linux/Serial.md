# Serial communication

## Minicom

minicom -D /dev/ttyS0

### incomming newline char not implemented

> set the carrige ret:
    Ctrl-A Z , UA

> to pemanent sulution:
    put in `etc/minicr.dfl`

    pu addcarreturn    Yes


## SOCAT

- povežemo dva serijska terminala med sabo

    socat -d -d pty,raw,echo=0 pty,raw,echo=0

#### pseudo terminal to stdio

    socat -dd pty,raw,echo=0,crnl exec:/bin/zsh,pty,stderr,setsid,sigint,sane

na to v drugem terminalnem oknu poženeš minicom -D /dev/pts/8
in si tako preko serijskega vmesnika povezan na računalniko (kot če bi bil preko ssh-ja)

https://fossies.org/linux/socat/EXAMPLES
