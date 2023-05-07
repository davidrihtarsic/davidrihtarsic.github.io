# ImageMagic

ImageMagick® is a free, open-source software suite, used for editing and manipulating digital images. It can be used to create, edit, compose, or convert bitmap images, and supports a wide range of file formats, including JPEG, PNG, GIF, TIFF, and PDF

## magick

Read  images  into memory, perform operations on those images, and write them out to either the same or some other image file format.  The "-script" option can be used to switch from processing command line options, to reading options from a file or pipeline.

## magick-script

This command is similar to magick(1) but with an implied "-script" option.  It is useful in special "#!/usr/bin/env magick-script" scripts that search  for the magick-script(1) command anywhere along the users PATH, rather than in a hardcoded command location.

## convert

Available for Backward compatibility with ImageMagick's version 6 convert(1).  Essentially, it is just an alias to a restrictive form of the magick(1) command, which should be used instead.

Sliko raztegnemo na ustrezno ŠIRINO pixlov in ohranimo razmerje stranic:

    convert example.png -resize 200 example.png

na VIŠINO:  

    convert example.png -resize x100 example.png

Združi (merge) dve sliki. Argument `-append` združi slike navpično, `+append` vodoravno:

    convert image1.png image2.png +append result_image.png

## mogrify

Resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more. This command overwrites the  original  image  file,  whereas convert(1) writes to a different image file.

## identify

Describe the format and characteristics of one or more image files.

    indentify ime_slike.png

> ime_slike.png PNG 571x339 5760x1080+1023+508 8-bit sRGB 226198B 0.000u 0:00.000

## composite

Overlap one image over another.

## montage

Create  a  composite  image by combining several separate ones. The images are tiled on the composite image, optionally adorned with a border, frame, image name, and more.

## compare

Mathematically and visually annotate the difference between an image and its reconstruction.

## stream

Stream one or more pixel components of the image or portion of the image to your choice of storage formats. It writes the pixel components as they are read from the input image, a row at a time, making stream(1) desirable when working with large images, or when you require raw pixel components.

## display

Display an image or image sequence on any X server.

## animate

Animate an image sequence on any X server.
