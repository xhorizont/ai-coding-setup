
.PHONY: help setup lint test format check wizard

.PHONY: help setup lint test format check


PYTHON := python3
VENV ?= .venv
ACTIVATE := source $(VENV)/bin/activate

help:

        @echo "Targets: setup, lint, test, format, check, wizard"

	@echo "Targets: setup, lint, test, format, check"


$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)
	$(ACTIVATE) && pip install --upgrade pip

setup: $(VENV)/bin/activate
	$(ACTIVATE) && pip install -r requirements.txt || true
	$(ACTIVATE) && pip install pre-commit
	$(ACTIVATE) && pre-commit install

lint:
	$(ACTIVATE) && ruff check .

format:
	$(ACTIVATE) && black .

mypy:
	$(ACTIVATE) && mypy scripts adapters src

precommit:
	$(ACTIVATE) && pre-commit run --all-files

check: format lint mypy

test:

        @echo "Tests are disabled for this project."

wizard:
        $(PYTHON) scripts/repo/setup_wizard.py

	@echo "Tests are disabled for this project."

