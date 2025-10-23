# FFMPEG

Commanr for recording:  

    ffmpeg -r 25 -f x11grab -s 1920x1080 -i :0.0 -f alsa -i default -c:v libx264rgb -crf 0 -preset ultrafast /home/david/Files/Pictures/ScreenCasts/screen_cast_$(date +%Y%m%d-%H%M%S).mp4
    
Med snemanjem je CPU kar obremenjen 110% - 150% ,  file pa je velik 50MB/min  
Nato narediš convert:  

    ffmpeg -i input_file.mp4 -c:v libx264 -crf 35 -preset medium -vf format=yuv420p output_file.mp4

Če video nalagaš na YT ali pa ga gledaš v ne-win predvajalnikih, potem lahko tudi '-cvf format=yuv420p' izpustiš.

| -crf |  -preset | size MB/min | Kvaliteta?               |
|:----:|:--------:|:-----------:|--------------------------|
|  25  |  medium  |     3.5     | ni popačenja super je    |
|  35  |  medium  |     2.2     | ja na meji OK            |
|  35  | veryslow |     2.1     | bolje, dolgo traja conv. |

Table: Vpliv koeficientov pri konverziji. {#tbl:ffmpeg-conversin}

## STABILIZACIJA VIDEOPOSNETKA

Za stabilizacijo video posnetka najprej ustvariš datoteko s podatki o premikanju kamere:

    ffmpeg -i input.mp4 -vf vidstabdetect=shakiness=7 -f null -

v tem ukazu je `shakiness` podatek koliko se trese kamera (1 je skoraj nič, 10 je da se kamera zelo trese).

Prejšnji ukaz ustvari datoteko `transforms.trf`, ki ga v naslednjem ukazu uporabimo pri stabilizaciji videoposnetka

    ffmpeg -i input.mp4 -vf vidstabtransform=smoothing=30:zoom=5:input="transforms.trf" stabilized.mp4

pri čemer je:
- smoothing: število slik pri povprečenju premikanja kamere (npr.: 10 pomeni, da bo vzel 10 slik prej in 10 po tisti sliki za katero izračunava stabilizacijo) Priporočljivo je izbrati `FPS/2`.
- zoom: nastavi `%` povečave. S tem parametrom damo stabilizatorju nekaj prostora v katerem lahko išče primerne sličice za generiranje stabilne slike. Seveda bo video nekoliko povečan in bomo izbubili nekaj slikovnih točk.

## IMAGES

Nekaj podatkov o fotografiji (resulucija)

    file img1.png

>img1.png: PNG image data, 1200 x 800, 8-bit/color RGB, non-interlaced

Rescale image

    convert img1.png -resize 1000x800 res_img1.png (ohrani razmerje stranic)
    convert img1.png -resize 1000x800! res_img1.png (ne ohrani razmerja stranic)
    convert IR_senzor2.png -resize x540 IR_senzor3.png
    
    ls img* | xargs -I{} convert {} -resize 1200x800! con_{} (za vse fotke ki se začnejo s con_)

## STICH

4x4 matrika

    fmpeg -i con_img1.png -i con_img2.png -i con_img3.png -i con_img4.png -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]"  output.png
