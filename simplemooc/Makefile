clean:
    @find . -name "*.pyc" -delete

deps:
    @pip install -r requirements.txt

test: deps clean
    @python manage.py test

run:
    @python manage.py runserver 8000

help:
    grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'