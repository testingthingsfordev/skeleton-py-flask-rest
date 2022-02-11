COMPOSE_PROJECT=api-flask

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

deps:
	docker-compose run api poetry install

bash:
	docker-compose run api /bin/bash

test:
	docker-compose run api pytest tests

coverage:
	docker-compose run api pytest --cov=api --cov-report=xml tests/
