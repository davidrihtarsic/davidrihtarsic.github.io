# NVIDIA drivers and operation

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
