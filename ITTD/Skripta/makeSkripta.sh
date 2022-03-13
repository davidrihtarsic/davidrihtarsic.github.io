#! /bin/bash

pandoc [0-9]*.md --to latex --from markdown --number-sections -F pandoc-crossref -F pandoc-citeproc --template skripta --listings --pdf-engine=pdflatex -V caption-justification=centering -o ITTD_2020.pdf
