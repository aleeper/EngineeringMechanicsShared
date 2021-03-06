### Fun with colors.
CWHITE="\\x1B[0m"
CGREEN="\\x1B[32m"
CRED="\\x1B[31m"
CPURPLE="\\x1B[35m"

### Specify the shell environment we expect to use.
SHELL := /bin/bash

### Make the echo command obey escape sequences.
ECHO := echo -e

DIRS=\
  BodyDynamics \
  Kinematics \
  MassAndMomentOfInertia \
  ParticleDynamics \
  ProjectileMotion \
  RotationTables \
  VectorBasics \
  VectorEquations \
  VectorGeometry \

default: build

setup:
	@for i in $(DIRS); \
	  do $(ECHO) "$(CGREEN)Setting up $$i$(CWHITE)"; \
	  (cd $$i && ln -sf ../Makefile.subfolder Makefile); \
	  done

build: check_env
	@for i in $(DIRS); \
	  do $(ECHO) "$(CGREEN)Making $$i$(CWHITE)"; \
	  (cd $$i && $(MAKE)); \
	  done

clean:
	@for i in $(DIRS); \
	  do $(ECHO) "$(CPURPLE)Cleaning $$i$(CWHITE)"; \
	  (cd $$i && $(MAKE) clean); \
	  done

check_env:
	@ if [ "${TEXINPUTS}" == "" ]; then \
	    $(ECHO) "$(CRED)Environment variable TEXINPUTS is not set!$(CWHITE)"; \
	    $(ECHO) "In this terminal, please source the setup.sh script located at the root of the repo:"; \
	    $(ECHO) "    ${CGREEN}source setup.sh${CWHITE}"; \
	    exit 1; \
	  fi

