FROM python:3.7-slim

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080