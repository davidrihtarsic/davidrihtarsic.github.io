#! /bin/bash

cat [1-9]*.md > Projekti_iz_elektronike.md
pandoc2notebook -f Projekti_iz_elektronike.md -t book -l sl
pdftotext Projekti_iz_elektronike.pdf
