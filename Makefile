lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

install:
	poetry install

test:
	poetry run pytest -vv

run:
	poetry run python3 -m gendiff.cli tests/fixtures/file1.json tests/fixtures/file2.json

run-plain:
	poetry run python3 -m gendiff.cli --format plain tests/fixtures/file1.json tests/fixtures/file2.json