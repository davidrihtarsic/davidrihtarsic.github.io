## INTEL GRAPHIC CARD

Če gre za **tearing** potem ustvari datoteko:

    /etc/X11/xorg.conf.d/20-intel.conf

in v njo daš naslednjo vsebino:

    Section "Device"
       Identifier  "Intel Graphics"
       Driver      "intel"
       Option      "TearFree"    "true"
    EndSection

## TEARING AFTER HIBERNATION

šel sem po teh navodilih:

[Intel tearing](https://bbs.archlinux.org/viewtopic.php?id=262198)

1. Enable GuC /HuC:

    sudo nvim /etc/default/grub
    GRUB_CMDLINE_LINUX_DEFAULT="resume=/dev/sda2 resume_offset=56727552 intel_idle.max_cstate=1 i915.enable_guc=2"
    sudo grub-mkconfig -o /boot/grub/grub.cfg

2. install:

    sudo pacman -S libva-intel-driver

3. removed /etc/X11/xorg.conf.d/20-intel.conf -> not used

Preveri če imamo GuC in HuC vklučen

    sudo  dmesg| grep 'GuC\|HuC'

> [    2.539392] [drm] GuC communication enabled
> [    2.549196] i915 0000:00:02.0: [drm] GuC firmware i915/kbl_guc_33.0.0.bin version 33.0 submission:disabled
> [    2.549198] i915 0000:00:02.0: [drm] HuC firmware i915/kbl_huc_4.0.0.bin version 4.0 authenticated:yes



