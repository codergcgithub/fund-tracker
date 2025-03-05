PYTHON_VERSION ?= 3.12
VENV_BIN := ./.venv/bin
SHELL := /bin/bash

create-venv:
	uv venv --python $(PYTHON_VERSION)
	source $(VENV_BIN)/activate
	uv pip install -r requirements-dev.txt

test: create-venv
	uv sync --extra test
	uv run pytest --tb=line ./tests

install: create-venv
	uv pip compile pyproject.toml
	#uv sync

lint: 
	ruff check --select=ALL ./app ./tests