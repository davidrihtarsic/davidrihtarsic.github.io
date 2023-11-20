# NVIDIA drivers and operation

2023-11-17:
Inšteliral sem ArcoLinux z NVIDIA... Erik predlaga, da namestiš `envycontrol`.

Da izklopimo nvidia:

    sudo envycontrol -s integrated

Izkazalo se je, da namesto 0.9h je bilo potem 1.5h.

Da ponastaviš v take nastavitve kot so bile pred envycontrol

    sudo envycontrol --reset

da pa optimiziraš porabo...

    sudo envycontrol -s hybrid

imam:
- Intel HD Graphicd 630 (i915)    
- NVIDIA GF GTX 1050 Mo (GP107M)  => NV137

Nazadnje je šlo nekaj narobe in v letu 2022 nvidia ni več delala
tako sem preskusil naslednji postopek:

    sudo pacman -S nvidia nvidia-utils nvidia-settings nvidia-prime
    reboot

da preverimo katero grafično uporabljamo moramo namestiti mesa-utils in
nato lahko preverimo z ukazom:

    sudo pacman -S mesa-utils
    glxinfo| grep "OpenGL rendere"

> OpenGL renderer string: Mesa Intel(R) HD Graphics 630 (KBL GT2)

in če uporabimo nvidia grafično, program zaženemo s prime-run

    prime-run glxinfo| grep "OpenGL rendere"

in nato lahko izbiraš katero grafično kartico boš uporabljal

    yay -S optimus-manager
    optimus-manager --switch nvidia
    optimus-manager --switch integrated
    optimus-manager --switch hybrid

## težave z ffmpeg
prime-run mi ni želel zagnati ffmpeg-a našel sem namig, da je potrebno imeti naloženo knjižnico
ffmpeg-full??

..:: stare nastavitve ::..

imam:
- Intel HD Graphicd 630 (i915)    
- NVIDIA GF GTX 1050 Mo (GP107M)  => NV137

        sudo pacman -S --noconfirm --needed nvidia
        sudo pacman -S --noconfirm --needed bbswitch
        trizen -S --noconfirm --needed nvidia-xrun-git

Load bbswitch module on boot

    sudo tee /etc/modules-load.d/bbswitch.conf <<<'bbswitch'

Disable the nvidia module on boot:

    sudo tee /etc/modprobe.d/bbswitch.conf <<<'options bbswitch load_state=0 unload_state=1'

After a reboot, the nvidia card will be off. This can be seen by querying bbswitch's status:

    cat /proc/acpi/bbswitch  

To force the card to turn on/off respectively run:

    tee /proc/acpi/bbswitch <<<OFF
    tee /proc/acpi/bbswitch <<<ON

 Disable the NVIDIA modules to load.

    sudo nvim /etc/modprobe.d/blacklist.conf

...blacklist modules:

    blacklist nvidia
    blacklist nvidia-drm
    blacklist nvidia-modeset
    blacklist nvidia-uvm
    blacklist nouveau

**za silo me je rešil Chacdar**

Problem solved by Chacdar Dustov. MANY THANKS!

With installing the NVIDIA drivers for GF GTX 1050

- tearing is seen,
- computer freezes randomly (with nouveau),
- original drivers from NVIDIA leave me with black screen...

- - -

Hi,

what I have installed currently is the 

    extra/nvidia-390xx-dkms 390.132-1

driver for the nvidia card. You should also install 

    bbswitch

and

    nvidia-xrun.

For normal usage I use the Intel GPU and if I want to play some game,
I switch the tty with ctrl+alt+(number grater than 1). In the console and run

  nvidia-xrun openbox

(for example, or another desktop envidonment/window manager) and there I lounch
heavier software on the GPU.

You can read this article:
https://wiki.archlinux.org/index.php/Nvidia-xrun for how to configure
the nvidia-xrun.

I suggest that you remove the nouveau and use bbswitch to switch off
the Nvidia GPU on boot.

Could you please send me your /etc/X11/xorg.conf configuration file
(its best to leave it empty).

Regards, Chavdar

- - -

David Rihtaršič 
Hi,
THANK YOU! for showing me the road! WAW... this can not be more pleasing... 
Exactly this kind of functionality I was looking for. Since I have 90% of administrative work I can easily do with Intel GPU... the other 10% is designing in FreeCAD for what I want to use the GF GTX 1050.
The consumption of battery went down significantly (cca 12W) with NVIDIA turned off - what gives me cca 3.5-4 hours of browsing and doing stuff here and there (before that I had less 2 hours).

I am not very fast with the progress because there is a lot of documentation that I am not familiar with yet and it takes time to read...

Installing the bbswitch and nvidia-xrun was crucial. I did not manage to install extra/nvidia-390xx-dkms since I got a conflict with nvidia-utils (I dont know when I installed it), but.. it is OK, nvidia drivers it seems to work to and I left  /etc/X11/xorg.conf empty as you suggested (before I had a lot of stuff in there from nvidia-xconfig command). Tearing that I was mentioning was present with Intel GPU (and not with NVIDIA) and it was solved by  Option "TearFree" "true" (as ArchWiki suggesting).

THANK YOU !!!
Best Regards, David
