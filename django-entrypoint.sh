#!/bin/bash
python manage.py flush --no-input
python manage.py migrate || exit 1
python manage.py createdata
DJANGO_SUPERUSER_PASSWORD=nueva123 python manage.py createsuperuser --noinput --username=admin --email=admin@rebus.com

exec "$@"