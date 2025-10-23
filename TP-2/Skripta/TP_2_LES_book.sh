#! /bin/bash

cat [0-9]*.md > TP_2_LES.md
pandoc2notebook -f TP_2_LES.md -t book
