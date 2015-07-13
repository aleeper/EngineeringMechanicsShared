SHELL := /bin/bash
TEX := pdflatex -halt-on-error


file_statics=inclined_block_statics
file_dynamics=inclined_block_dynamics

preambleA="\\def\\ShowSolution{0}\\def\\StudentTeacherPaul{0}"
preambleB="\\def\\ShowSolution{1}\\def\\StudentTeacherPaul{1}"

all: dynamics statics

dynamics:
	$(TEX) -jobname=$(file_dynamics)         "$(preambleA)\input{$(file_dynamics).tex}"
	$(TEX) -jobname=$(file_dynamics)Solution "$(preambleB)\input{$(file_dynamics).tex}"

statics:
	$(TEX) -jobname=$(file_statics)         "$(preambleA)\input{$(file_statics).tex}"
	$(TEX) -jobname=$(file_statics)Solution "$(preambleB)\input{$(file_statics).tex}"

view:
	evince *.pdf &
clean:
	@rm -vf *.aux *.synctex.gz *.log *.pdf
