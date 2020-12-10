FROM python:latest

RUN apt-get update && \
  apt-get install -y python3-dev default-libmysqlclient-dev

RUN pip install mysqlclient


COPY ./birdclassifier/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY birdclassifier .

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
