POTFILE=$(shell cat POTFILES.in)
SOURCES=$(addprefix ../, $(POTFILE))
POFILES=$(wildcard *.po)
MOFILES=$(patsubst %.po,%.mo,$(POFILES))
all: $(MOFILES)

ojuba-personal-lock.pot: $(SOURCES)
	intltool-update -g ojuba-personal-lock -p

%.mo: %.po
	msgfmt $*.po -o $*.mo
	mkdir -p ../locale/$*/LC_MESSAGES/ || :
	cp $*.mo ../locale/$*/LC_MESSAGES/ojuba-personal-lock.mo

%.po: ojuba-personal-lock.pot
	intltool-update -g ojuba-personal-lock -d $*

