FROM python:3.11.6-alpine
WORKDIR /app
COPY . /app

RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install pip --upgrade && \
    pip install poetry && \
    poetry config virtualenvs.in-project true

RUN poetry install

EXPOSE 3000
EXPOSE 8000

CMD ["poetry", "run", "reflex", "run"]

# docker run --rm -p 3000:3000 -p 8000:8000 test:0.1