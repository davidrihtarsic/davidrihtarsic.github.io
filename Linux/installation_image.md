# INSTALLATION IMAGE

## make bootable USB drive

1. check the name of usb drive!

        lsblk

2. copy image to USB drive

        sudo dd if=manjaro-kde-21.3.5-220721-linux515.iso of=/dev/sdc bs=1M status=progress
