.PHONY: all tests setup flake8 lint exe sun moon
# make >debug.log 2>&1
ifeq ($(OS),Windows_NT)
PTEST = venv/Scripts/pytest.exe
PYINSTALLER = venv/Scripts/pyinstaller.exe
PYTHON = venv/Scripts/python.exe
COVERAGE = venv/Scripts/coverage.exe
else
PTEST = ./venv/bin/pytest
PYINSTALLER = ./venv/bin/pyinstaller
PYTHON = ./venv/bin/python
COVERAGE = ./venv/bin/coverage
endif

SKYDATA = skyfield/data
SKYBSP = skyfield-data
SOURCE = source
TESTS = tests

PYTEST = $(PTEST) --cov=$(SOURCE) --cov-report term:skip-covered
PIP = $(PYTHON) -m pip install
LINT = $(PYTHON) -m pylint
RUN = $(PYTHON) $(SOURCE)/main.py
SARATOV = 51.551750 45.964380

test:
	$(PTEST) --verbose -s $(TESTS)/test/$(T)

tests: flake8 pep257 lint
	$(PYTEST) --durations=5 $(TESTS)
	$(COVERAGE) html --skip-covered

flake8:
	$(PYTHON) -m flake8 --max-line-length=120 $(TESTS)
	$(PYTHON) -m flake8 --max-line-length=120 $(SOURCE)

lint:
	$(LINT) $(TESTS)/test
	$(LINT) $(SOURCE)

pep257:
	$(PYTHON) -m pep257 $(SOURCE)
	$(PYTHON) -m pep257 --match='.*\.py' $(TESTS)/test

exe:
	$(PYINSTALLER) --paths=$(SOURCE) --onefile --name planet-tracks $(SOURCE)/main.py --add-data '$(SKYBSP);$(SKYBSP)' --add-data 'venv/Lib/site-packages/$(SKYDATA);$(SKYDATA)'

sun:
	$(RUN) sun $(SARATOV)

moon:
	$(RUN) moon $(SARATOV)

setup: setup_python setup_pip

setup_pip:
	$(PIP) --upgrade pip
	$(PIP) -r requirements.txt
	$(PIP) -r $(TESTS)/requirements.txt

setup_python:
	$(PYTHON_BIN) -m venv ./venv
