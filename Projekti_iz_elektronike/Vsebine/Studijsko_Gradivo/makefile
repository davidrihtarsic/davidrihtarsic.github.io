pdfs:
	@for ff in $(file); do \
		num=$$(echo $$ff | sed 's/_.*$$//'); \
		section=$$(echo $$num | sed 's/\..*$$//g'); \
		subsect=$$(echo $$num | sed 's/.*\.//g'); \
		[[ $$subsect -gt 0 ]] && subsect=$$((subsect-1)) || section=$$((section-1)); \
		sed -i "1i \\\\\setcounter{section}{$$section}\\\\\setcounter{subsection}{$$subsect}" $$ff; \
		pandoc2notebook -f $$ff; \
		sed -i "1d" $$ff; \
		done;

TITLE="Projekti iz elektronike"
book:
	@echo "Compailing all chapters into book... $(TITLE)."
	@file_name=$$(echo $(TITLE) | sed 's/\ /_/g'); \
	pandoc [0-9]*.md --to latex -o $$file_name.pdf \
		--from markdown \
		--template skripta \
		-V lang=sl \
		-M title=$(TITLE) \
		-M subtitle="Skripta je namenjena študentom UL-PeF študijske smeri Fizike z vezavami. V skripti so opisani osnovni principi vzorčenja fizikalnih količin s krmilnikom Arduino NANO." \
		-M author:"dr. David Rihtaršič" \
		-M date:"$(date '+%Y-%B')" \
		--listings \
		-M listings=True \
		-M listings-no-page-break=True \
		-M codeBlockCaptions=True \
		-M listingTitle=Program \
		-M figureTitle=Slika \
		-M figPrefix=sl. \
		-M eqnPrefix=en. \
		-M lstPrefix=prog. \
		-V table-use-row-colors \
		-V urlcolor=violet \
		-V caption-justification=centering \
		--number-sections \
		-F pandoc-crossref \
		--citeproc \
		--bibliography=/home/david/Files/Work/UL-PeF/Articles/00-BibTex/bibtex.bib \
		-V documentclass=book \
		-V book \
		--toc \
		-M titlepage;

clean:
	@mv *.pdf ./pdf/

file := $(shell find ./ -type f -name "[0-9]*.md"|sed 's/\.\///g')
all: pdfs book clean
