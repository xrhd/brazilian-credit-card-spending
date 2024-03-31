setup:
	pip install -r requirements.txt
	pre-commit install

fmt:
	ruff format

lint:
	ruff check --fix