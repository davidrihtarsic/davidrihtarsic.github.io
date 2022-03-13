#! /bin/sh


pandoc --extract-media=ElNaboj ElNaboj.docx -o ElNaboj.md
pandoc --extract-media=ElUpornost ElUpornost.docx -o ElUpornost.md
pandoc --extract-media=EnakomernoGibanje EnakomernoGibanje.docx -o EnakomernoGibanje.md
pandoc --extract-media=Gostota Gostota.docx -o Gostota.md
pandoc --extract-media=MagnetnoPolje MagnetnoPolje.docx -o MagnetnoPolje.md
pandoc --extract-media=OdbojLom OdbojLom.docx -o OdbojLom.md
pandoc --extract-media=SileGibanje SileGibanje.docx -o SileGibanje.md
pandoc --extract-media=SileSeštevanje SileSeštevanje.docx -o SileSeštevanje.md
pandoc --extract-media=Trenje Trenje.docx -o Trenje.md
