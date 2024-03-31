#!/bin/sh

python manage.py migratep
gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
