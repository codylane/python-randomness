PROJNAME = randomness

.PHONY: clean
.PHONY: clean_python
.PHONY: coverage_report
.PHONY: coverage_html
.PHONY: init
.PHONY: test


all: clean init


clean: clean_python
	rm -f .*.lcts


clean_python:
	find . -name __pycache__ -type d | xargs rm -rf
	find . -name '*.egg-info' -type d | xargs rm -rf
	find . -name '*.pyc' -type f -delete


coverage_report:
	coverage report -m


coverage_html: test
	cd coverage && python -m http.server


init:
	PROJNAME=$(PROJNAME) ./init.sh


run:
	python src/$(PROJNAME)/__init__.py


test:
	pytest -vs
