DESTDIR?=/
datadir?=$(DESTDIR)/usr/share
INSTALL=install

SOURCES=$(wildcard *.desktop.in)
TARGETS=${SOURCES:.in=}

all: $(TARGETS)

pos:
	make -C po all

install: all
	python setup.py install -O2 --root $(DESTDIR)

%.desktop: %.desktop.in pos
	intltool-merge -d po $< $@


