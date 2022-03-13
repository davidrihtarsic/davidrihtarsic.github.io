#! /bin/sh

grep -h -e "^>\|^#" [0-9]*.md | sed '/^#/ i \\' | sed '/### NALOGA/ i \\' > Naloge.md
pandoc2notebook -f Naloge.md -t book -l sl
