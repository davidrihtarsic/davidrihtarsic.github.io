### PANDOC
Program za pretvorbo dokumentov. Naveč ga uporabljam za pretvorbo iz `MARKDOWN` dokumentov v `PDF` dokumente. Na primer:  

```bash
pandoc --from markdown -F pandoc-crossref -F pandoc-citeproc --template eisvogel --listings --pdf-engine=xelatex index.md -o index.pdf
```

V verziji pandoc 2.8 mi niso delale slike...  

- odstraniš grffile iz templata in je ok (menda da delajo na tem...)

**Skripta**  
Lahko bi v templatu definral različne listingse.

- ne to se je v bistvu izkazalo za slobo... spremenil se je template od eisvogel.teh in moji listingsi niso več delali...

``` vaja
VAJA: NAPETOSTNI POTENCIALI IN NAPETOST
Zanima me kako bi zgledalo tole v dokumenti, če bi podajal naloge za študente v taki obliki.
A je v tem listingsu vsaka vrstica naoisana v novi 
nrstici.
```

> ### NALOGA: naloga
> Odločil sem se, da bom imel naloge za študente razporejene kot 3. Naslov in dane v komentarje.
> Tako se mi zdi, da lahko zelo konsistentno držim obliko.

## pretvarjanje različnih dokumentov

Eno od uporabnih zadev je tudi, da enostavno Word dokument spremenim v `*.md`. Tako lahko študentsko poročilo objavim na spletu:

    pandoc
