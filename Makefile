.PHONY: all install_requirements download combine

PYTHON := $(shell which python3 2>/dev/null || which python)

all: install_requirements download combine list

install_requirements:
	$(PYTHON) -m pip install -r lib/requirements.txt

download:
	$(PYTHON) lib/download.py

combine:
	$(PYTHON) lib/combine.py

validate:
	$(PYTHON) lib/validate.py

list:
	$(PYTHON) lib/list.py
