SHELL := /bin/bash
PYTHON := python3
PROJECT_NAME := chatbot
VENV_DIR := venv

venv:
	virtualenv venv -p $(PYTHON)
	source $(VENV_DIR)/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

run: venv
	python main.py

# Linting
lint: venv
	isort .
	flake8 *.py


security: venv
	safety check
