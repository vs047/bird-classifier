FROM python:latest

RUN apt-get update && \
  apt-get install python-mysqldb

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver
