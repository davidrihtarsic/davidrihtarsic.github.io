#! /bin/bash

#pandoc [0-9]*.md --to latex --from markdown --number-sections -F pandoc-crossref --citeproc --template skripta --listings --pdf-engine=pdflatex -V caption-justification=centering -o Skripta.pdf


#FILEs=$1
FILEs="[0-9]*.md"
BOOK_SETTINGS='
-V documentclass=book
-V book
--toc
-M titlepage'

CAPTIONS='
-M listingTitle=Program
-M figureTitle=Slika
-M figPrefix=sl.
-M eqnPrefix=en.
-M lstPrefix=prog. '

pandoc  $FILEs --to latex -o Skripta.pdf \
    --from markdown \
    --template skripta \
    -V lang=sl \
    -M title="Računalnik v pouku Fizike - zbirka vaj" \
    -M subtitle="Skripta je namenjena študentom UL-PeF študijske smeri Fizike z vezavami. V skripti so opisani osnovni principi vzorčenja fizikalnih količin s krmilnikom Arduino NANO." \
    -M author:"dr. David Rihtaršič" \
    -M date:"$(date '+%Y-%B')" \
    --listings \
    -M listings=True \
    -M listings-no-page-break=True \
    -M codeBlockCaptions=True \
    $CAPTIONS \
    -V table-use-row-colors \
    -V urlcolor=violet \
    -V caption-justification=centering \
    --number-sections \
    -F pandoc-crossref \
    --citeproc \
    --bibliography=/home/david/Files/Work/UL-PeF/Articles/00-BibTex/bibtex.bib \
    $BOOK_SETTINGS 
