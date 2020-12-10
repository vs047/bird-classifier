FROM python:latest

RUN apt-get update && \
  apt-get install python-mysqldb

COPY ./birdclassifier/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY birdclassifier .

CMD python manage.py runserver
