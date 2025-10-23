#! /bin/bash

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
    -M title="ELEKTROTEHNIKA" \
    -M subtitle="Zbirka laboratorijskih vaj za študente Univerze v Ljubljani, Pedagoške Fakultete" \
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
