.PHONY: help install test lint format

help:
	@echo "Available commands:"
	@echo "  make install        Install all dependencies"
	@echo "  make test           Run all tests with pytest"

install:
	pip install -r requirements.txt
	playwright install

test:
	pytest -v -n "auto"
