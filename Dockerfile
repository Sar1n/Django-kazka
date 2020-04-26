FROM python:3.8.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# RUN apt-get update
# RUN apt-get install systemd -y
# RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
# RUN apt-get install gnupg
# RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
# RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.2.list
# RUN apt-get update
# RUN apt-get install -y mongodb-org
# #RUN service mongod start
COPY . /code/