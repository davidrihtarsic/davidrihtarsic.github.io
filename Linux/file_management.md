# FILE MANAGEMENT

Osnovne funkcije za organizacijo datotek so:

        touch datoteka.md
        mkdir Dir_1
        cp Dir_1/* Dir_2
        mv Dir_1/datoteka.md Dir_2
        ln -s datoteka.md link_na_datoteko.md

in za pregled datoek:

        ln -all
        tree ./
        find . -type f

## Naprednejše operacije

- skopiraj strukturo trenutnega direktorija v  nek drug direktorij
  to je koristno za DRTI, kjer imamo vsako leto enako strukturo direktorijev
  za finance.

        tree -dfi --noreport | xargs -I{} mkdir -p  ../Test2/{}

- če imamo imena datotek ali direktorijev zbrane v neki datoteki (npr.: `zbrani_dir.md`)
  lahko uporabimo naslednji ukaz:

        mkdir $(<zbrani_dir.md)

- naredi vse simbolične povezave datotek iz enega dir v drugega
  to pride prav za delo v projektni skupini, kjer imamo skupen direktorij, 
  v katerega dostopamo vsi, medtem pa slovenska ekipa dela na svojem direktoriju.

        find . -type f | xargs -I{} ln -s ~+/{} ../Test2/{}

