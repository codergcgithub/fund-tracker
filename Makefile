PYTHON_VERSION ?= 3.12
VENV_BIN := ./.venv/bin
SHELL := /bin/bash

create-venv:
	uv venv --python $(PYTHON_VERSION)
	source $(VENV_BIN)/activate
	uv pip install -r requirements-dev.txt
	uv add --requirements requirements.txt

test: create-venv
	uv sync --extra test
	PYTHONPATH=$(shell pwd) uv run pytest --tb=line .

install: create-venv
	uv pip compile pyproject.toml

lint: 
	ruff check --select=ALL 