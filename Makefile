ENV=

up:
	docker-compose up -d --build

run:
	docker run -v `pwd`:/tmp --rm -it /usr/local/bin/python3 /tmp/src/main.py

exec:
	docker-compose exec app bash

host:
	docker run -v $PWD/opt:/root/opt -w /root/opt -it --rm -p 7777:8888 docker-python_python3 jupyter-lab --ip 0.0.0.0 --allow-root -b localhost