.PHONY: pdf pdfs book clean all

TITLE = Projekti iz elektronike
file ?= $(wildcard [0-9]*.md)

# Make individual PDFs beside their Markdown source files.
# Example: make pdf file=1.3_Svetlobni_sprejemnik.md
pdf: pdfs

pdfs:
	@set -e; for ff in $(file); do \
		( \
			set -e; \
			base=$${ff##*/}; number=$${base%%_*}; \
			chapter=$${number%%.*}; subsection=$${number#*.}; \
			case "$$chapter:$$subsection" in *[!0-9:]*|:*) echo "Ime datoteke mora začeti z zaporedjem poglavje.podpoglavje_: $$ff" >&2; exit 1;; esac; \
			section=$$chapter; \
			if [ "$$subsection" -eq 0 ]; then \
				subsection=-1; \
				if sed -n '1p' "$$ff" | grep -Eq '^#[[:space:]]' || sed -n '2p' "$$ff" | grep -Eq '^[[:space:]]*={3,}[[:space:]]*$$'; then \
					section=$$((chapter - 1)); subsection=0; \
				fi; \
			else \
				subsection=$$((subsection - 1)); \
			fi; \
			sed -i "1i\\\\\\setcounter{section}{$$section}\\\\setcounter{subsection}{$$subsection}" "$$ff"; \
			cleanup() { sed -i '1d' "$$ff"; }; \
			trap cleanup EXIT; \
			out=$${ff%.md}.pdf; \
			pandoc "$$ff" \
				--to latex \
				--from markdown \
				--pdf-engine=xelatex \
				--template=skripta.latex \
				--output="$$out" \
				-V lang=sl \
				-M author="dr. David Rihtaršič" \
				-M date:"$$(date '+%Y-%B')" \
				--syntax-highlighting=idiomatic \
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
				-F mermaid-filter \
				--citeproc \
				--bibliography=./references.bib \
				-V documentclass=article; \
		); \
	done

book:
	@echo "Compailing all chapters into book... $(TITLE)."
	@file_name=$$(echo $(TITLE) | sed 's/\ /_/g'); \
	pandoc [0-9]*.md --to latex -o $$file_name.pdf \
		--from markdown \
		--pdf-engine=xelatex \
		--template=skripta.latex \
		-V lang=sl \
		-M title=$(TITLE) \
		-M subtitle="Študijsko gradivo za študente UL-PeF študijske smeri Tehnika z vezavami. Skripta obravnava osnove elektronskih vezij, analogne in digitalne signale, regulacijske sisteme, mikrokrmilnike ter druga uporabna elektronska vezja." \
		-M author:"dr. David Rihtaršič" \
		-M date:"$$(date '+%Y-%B')" \
		--syntax-highlighting=idiomatic \
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
		--bibliography=./references.bib \
		-V documentclass=book \
		-V book \
		--toc \
		-M titlepage

clean:
	@mv *.pdf ./pdf/

all: pdfs book
