SHELL := /bin/bash
TEX := pdflatex -halt-on-error

filename=ski_jumper
all:
	@$(TEX) -jobname=$(filename)Student     "\def\ShowSolution{0}\def\StudentTeacherPaul{0}\input{$(filename).tex}"
	@$(TEX) -jobname=$(filename)Instructor  "\def\ShowSolution{1}\def\StudentTeacherPaul{1}\input{$(filename).tex}"

clean:
	@mv skier_mg.pdf skier_mg.pdf.bak
	@rm -vf *.synctex.gz *.aux *.log *.pdf
	@mv skier_mg.pdf.bak skier_mg.pdf
