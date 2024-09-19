PR = poetry run

all: lint check-migrations test

lint:
	${PR} black .
	${PR} ruff check .
	${PR} mypy .
	${PR} isort .

check-migrations:
	poetry run dj makemigrations --check

build-dev:
	docker-compose -f docker-compose.yml up -d --build
