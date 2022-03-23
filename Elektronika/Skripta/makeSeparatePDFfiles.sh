#! /bin/bash
section_counter=0
for file in [0-9]*.md
do
  sed -i "1 i \\\\\setcounter{section}{$section_counter}" $file
  pandoc2notebook -f $file -l sl
  sed -i '1d' $file
  new_section=$(head $file | grep -e "^# ")
  if [ -n "$new_section" ]
  then
    ((section_counter++))
  fi
done
