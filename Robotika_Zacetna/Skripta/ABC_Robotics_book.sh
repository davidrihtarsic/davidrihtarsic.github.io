#! /bin/bash

cat [1-9]*.md > ABC_Robotics.md
cat 0*.md >> ABC_Robotics.md
pandoc2notebook -f ABC_Robotics.md -t book
