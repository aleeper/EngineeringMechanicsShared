SHELL := /bin/bash
TEX := pdflatex -halt-on-error

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))

filename=RobotStatics
#$(current_dir)

all:
	$(TEX) -jobname=$(filename)Student     "\def\ShowSolution{0}\def\StudentTeacherPaul{0}\input{$(filename).tex}"
	$(TEX) -jobname=$(filename)Instructor  "\def\ShowSolution{1}\def\StudentTeacherPaul{1}\input{$(filename).tex}"

clean:
	@rm -vf *.aux *.synctex.gz *.log *.pdf
