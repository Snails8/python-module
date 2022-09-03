ENV=

up:
	docker-compose up -d --build

run:
	docker run -v `pwd`:/tmp --rm -it /usr/local/bin/python3 /tmp/src/main.py

exec:
	docker-compose exec app bash
