PYTHON := python3
PIP := $(PYTHON) -m pip

.DEFAULT_GOAL = help

install:
	@echo "Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install --editable .

install-dev:
	@echo "Installing dev dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install --editable '.[dev]'
	pre-commit install

lint:
	@echo "Running linting tool..."
	flake8 src/app.py --verbose

format:
	@echo "running auto-format..."
	black src/app.py --verbose

type-check:
	@echo "Running type-checking tool..."
	mypy src/app.py

unit-test:
	@echo "Running unit tests..."
	pytest -vv --cov --cov-report=term-missing

help:
	@echo "Commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make install-dev   - Install development dependencies"
	@echo "  make lint          - Veerify code style (flake8)"
	@echo "  make format        - Format code to PEP (black)"
	@echo "  make type-check    - Verify variable types (mypy)"
	@echo "  make unit-test     - Run unit tests (pytest)"
