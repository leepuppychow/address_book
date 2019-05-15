FROM python:3.6-slim

COPY requirements.txt /

WORKDIR /

RUN pip install -r ./requirements.txt --no-cache-dir

COPY . /app/

WORKDIR /app

CMD flask db upgrade && flask run -h 0.0.0.0 -p 5000