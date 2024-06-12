### PANDOC
Program za pretvorbo dokumentov. Največ ga uporabljam za pretvorbo iz `MARKDOWN` dokumentov v `PDF` dokumente. Na primer:  

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

    pandoc --extract-media ./myMediaFolder input.docx -o output.md

## Citiranje

- [Seznam različnih stilov citiranja](https://github.com/citation-style-language/styles)

## Directiory architectue

directory iz katerega `pandoc` bere je $XDG_DATA_HOME ki je : `/home/david/.local/share`
v tem directory-u pa imam narejeno strukturo:

```
/home/david/.local/share/pandoc/
├── csl
│   ├── apa6.csl
│   └── ieee.csl
└── templates
    ├── eisvogel.latex
    ├── izpit.latex
    ├── report.latex
    └── skripta.latex
```

ampak sem mu za izbor načina citiranja moral pokazati točno na datoteko naprimer:

        pandoc -o 00_test.pdf 2.2.3_Thinkercad_Circuits.md --bibliography=/home/david/Files/Work/UL-PeF/Articles/00-BibTex/bibtex.bib --filter=pandoc-crossref --citeproc --listings -M listings=True -M codeBlockCaptions=True --csl=/usr/share/pandoc/data/ieee.csl
