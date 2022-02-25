build:
	docker-compose build

down:
	docker-compose down

up: build migrate
	docker-compose up -d

migrate:
	docker-compose run api python manage.py migrate

deps:
	docker-compose run api poetry install

bash:
	docker-compose run api /bin/sh

test:
	docker-compose run api python -m unittest

coverage: build migrate
	docker-compose run api /bin/ash -c "coverage run --source='api' --omit='api/tests/*' -m unittest"
	docker-compose run api coverage report
	docker-compose run api coverage xml
	docker-compose run api coverage html
