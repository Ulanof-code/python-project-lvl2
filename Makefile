lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff

install:
	poetry install