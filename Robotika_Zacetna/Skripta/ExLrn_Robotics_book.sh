#! /bin/bash

cat [0-9]*.md > Experiential_Learning_of_Robotics.md
#cat 0*.md >> ABC_Robotics.md
pandoc2notebook -f Experiential_Learning_of_Robotics.md -t book -s "GUIDANCE AND RECOMMENDATIONS"
