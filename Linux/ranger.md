### RANGER

Cool "the best" File manager. Sicer napisan v pythonu, ampak še vedno hiter. Omogoča:

- vim bindings
- goto directory key shortcuts
- lahko kličeš svoje skripte
- preklop v shell (Shift+s)
- predogled filov: slike, video, programsko kodo
- ...

# ISSUES

## MARKDOWN FILES RENDERING

MD fili niso pravilno prikazani, če uporabljamo mdv
dela mi tale prva programska vrstica:

    md)
      mdv -A "${FILE_PATH}" && exit 5
      cat "${FILE_PATH}" | mdv -c ${PV_WIDTH}  -t 960.847 -n 1-3 - && exit 0
      try mdv "$path" -t 757.2295 -c $width && { dump | trim; exit 5; } || exit 2;;
      cat "${FILE_PATH}" && exit 5
    ;;


