FROM python:3.6-slim

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

COPY requirements.txt /

WORKDIR /

RUN pip install -r ./requirements.txt --no-cache-dir

COPY . /app/

WORKDIR /app

CMD flask db upgrade && python manage.py seed && flask run -h 0.0.0.0 -p 5000