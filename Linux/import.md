# IMPORT - terminal screen capture

za zajem zasloncke slike

na drugem računalniku v mreži

>Assuming you have ImageMagick installed on the remote and local machine, the X server on the remote machine is running as the user you are connecting with, you can take a screenshot remotely and display it on your local X server like this:
>
>     ssh user@example.com "DISPLAY=:0 import -window root -" | display
>
>This is very convenient as you don't need to copy any temporary files.
