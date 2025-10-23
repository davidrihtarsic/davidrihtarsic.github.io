# BOOTing PROCESS

## Boot problems

Diagnosing errors during the boot process involves changing the kernel parameters, and rebooting the system.
If booting the system is not possible, boot from a live image and change root to the existing system.

### Console messages

After the boot process, the screen is cleared and the login prompt appears, leaving users unable to read init output and error messages. This default behavior may be modified using methods outlined in the sections below.
Note that regardless of the chosen option, kernel messages can be displayed for inspection after booting by using

    dmesg

or all logs from the current boot with 

    journalctl -b

### Flow control

This is basic management that applies to most terminal emulators, including virtual consoles (vc):

    Press Ctrl+s to pause the output
    And Ctrl+q to resume it

This pauses not only the output, but also programs which try to print to the terminal, as they will block on the write() calls for as long as the output is paused. If your init appears frozen, make sure the system console is not paused.

To see error messages which are already displayed, see Getty#Have boot messages stay on tty1.
Debug output

Most kernel messages are hidden during boot. You can see more of these messages by adding different kernel parameters. The simplest ones are:

    debug enables debug messages for both the kernel and systemd
    ignore_loglevel forces all kernel messages to be printed

Other parameters you can add that might be useful in certain situations are:

    earlyprintk=vga,keep prints kernel messages very early in the boot process, in case the kernel would crash before output is shown. You must change vga to efi for EFI systems
    log_buf_len=16M allocates a larger (16MB) kernel message buffer, to ensure that debug output is not overwritten

There are also a number of separate debug parameters for enabling debugging in specific subsystems e.g. bootmem_debug, sched_debug. Check the kernel parameter documentation for specific information.
Note: If you cannot scroll back far enough to view the desired boot output, you should increase the size of the scrollback buffer.

## PROCESS

1. grub - izbereš lahko kateri os boš zagnal
2. Login manager - izbereš kateri uporabnik in katero Window manager se bo uporabljal
    - kateri LM uporabljaš lahko preveriš z `status display-manager.service`
    - trenutno uporabljam SDDM in ima konfiguracijsko datoteko v `/etc/sddm.conf.d/kde_settings.conf`
3. Uporabniška seja
    - SDDM izvrši `/usr/share/xsessions/chadwm.desktop` 
    - `~/.xinitrc` datoteka je namenjena prilagoditvi zagona X seje, ko uporabljaš ukaz `startx`. V njej običajno nastaviš okoljske spremenljivke, zaženeš programe, ki se izvajajo ob začetku seje, in na koncu zaženeš window manager ali namizno okolje.
    - `chadwm` konfiguriraš preko "config.h", kjer določiš barve, tipkovne bližnjice in pravila za okna (nastavitve se spremenijo ob kompilaciji). Za zagon uporabiš .xinitrc, kjer vpišeš npr. "exec chadwm".
4. Terminal in ukazne lupine
    - login lupine:
        - `/etc/.zshenv` in na to `~/.zshenv`
        - `/etc/zprofile` in `~/.zprofile`,
        - `/etc/zshrc` in `~/.zshrc`,
        - `/etc/zlogin` in `~/.zlogin`.
    - ne- log-in seje:
        - `/etc/.zshenv` in na to `~/.zshenv`
        - `/etc/zshrc` in `~/.zshrc`,
