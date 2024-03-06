docker-up:
	docker compose --env-file=.env up --build -d
docker-down:
	docker compose down
docker-exec:
	docker compose exec app bash
create-su:
	@docker compose exec app ./src/manage.py create_su
lint:
	@docker compose exec app pycodestyle ./src/ --exclude=./src/**/migrations/,./src/config/ --verbose