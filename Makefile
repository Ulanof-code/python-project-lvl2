lint:
	poetry run flake8 gendiff

mypy:
	poetry run mypy gendiff

mypy-install-types:
	poetry run mypy gendiff --install-types

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

install:
	poetry install

test:
	poetry run pytest -vv

build:
	poetry build

