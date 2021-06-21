lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

install:
	poetry install

test:
	poetry run pytest -vv

build:
	poetry build

