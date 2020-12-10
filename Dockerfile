FROM python:latest

RUN apt-get update && \
  apt-get install -y python3-dev default-libmysqlclient-dev

RUN pip install mysqlclient


COPY ./birdclassifier/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY birdclassifier .

CMD python manage.py runserver && gunicorn birdclassifier.wsgi --log-file -
