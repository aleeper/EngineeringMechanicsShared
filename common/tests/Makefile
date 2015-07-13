###############################################################################
### NOTE: This Makefile is shared across all problem folders via a symlink.
### Changes to this file will affect ALL problem folders.
### The actual file location is engr105/problems/Makefile.problem.
###############################################################################

### Fun with colors.
CWHITE="\\x1B[0m"
CGREEN="\\x1B[32m"
CRED="\\x1B[31m"
CPURPLE="\\x1B[35m"

### Specify the shell environment we expect to use.
SHELL := /bin/bash

### Make the echo command obey escape sequences.
ECHO := echo -e

### Specify the latex build command.
TEX := pdflatex -halt-on-error -shell-escape -interaction=nonstopmode

### Define a command for PDF viewing that will work on both Mac and Linux.
PDF_VIEW := $$(if [ "$$(uname)" == "Darwin" ]; then echo "open -a Preview"; else echo "evince"; fi;)


###############################################################################
### Make targets.
###############################################################################

default: build

objects = \
					test_bigbold \
					test_ifthenCustom \
					test_commonFonts \
					test_textStyles \
					test_customOperators \
					test_customMathScalars \
					test_vectorsCommon \
					test_mechanics \

					#test_customFormatting
					#test_multipleChoiceEquationTypes

build: check_env $(objects)
	@rm -vf *.aux *.synctex.gz *.log

# This is needed so that wildcards can be used in the prereqs.
.SECONDEXPANSION:

test_%.tex:
	@$(ECHO) "$(CPURPLE)*******************************************************************************$(CWHITE)"
	@$(ECHO) "$(CPURPLE)Creating file test_$*.tex.$(CWHITE)"
	@$(ECHO) "$(CPURPLE)*******************************************************************************$(CWHITE)"
	/usr/bin/python create_tests.py ../packages/$*.sty

test_% : test_%.tex
	@$(ECHO) "$(CGREEN)*******************************************************************************$(CWHITE)"
	@$(ECHO) "$(CGREEN)Building: $<.$(CWHITE)"
	@$(ECHO) "$(CGREEN)*******************************************************************************$(CWHITE)"
	$(TEX) $<
	@$(ECHO) "$(CGREEN)*******************************************************************************$(CWHITE)"

clean:
	@rm -vf *.aux *.synctex.gz *.log *.tex
	@rm -vf *.pdf

check_env:
	@ if [ "${TEXINPUTS}" == "" ]; then \
	    $(ECHO) "$(CRED)Environment variable TEXINPUTS is not set!$(CWHITE)"; \
	    $(ECHO) "In this terminal, please source the setup.sh script located at the root of the repo:"; \
	    $(ECHO) "    $(CGREEN)source setup.sh$(CWHITE)"; \
	    exit 1; \
	  fi
