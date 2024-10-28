FROM python

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update  && apt-get upgrade -y

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "python", "src/main.py"]