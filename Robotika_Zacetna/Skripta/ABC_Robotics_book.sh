#! /bin/bash

cat [0-9]*.md > ABC_Robotics.md
#cat 0*.md >> ABC_Robotics.md
pandoc2notebook -f ABC_Robotics.md -t book
