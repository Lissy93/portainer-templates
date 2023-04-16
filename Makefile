.PHONY: all install_requirements download combine

all: install_requirements download combine

install_requirements:
	pip install -r lib/requirements.txt

download:
	python lib/download.py

combine:
	python lib/combine.py

validate:
	python lib/validate.py
