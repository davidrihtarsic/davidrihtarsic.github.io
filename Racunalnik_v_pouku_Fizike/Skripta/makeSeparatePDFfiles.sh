#! /bin/bash

for file in [0-9]*.md
do
  pandoc2notebook -l sl -f $file
done
