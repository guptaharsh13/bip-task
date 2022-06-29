FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

CMD python3 manage.py collectstatic --noinput; python3 manage.py makemigrations; python3 manage.py migrate; python3 manage.py runserver 0.0.0.0:80