FROM python:3.8.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install django-heroku
RUN apt-get update && apt-get install -y netcat
COPY . /code/