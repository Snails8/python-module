ENV=

up:
	docker-compose up -d --build

exec:
	docker exec -it python3 python main.py