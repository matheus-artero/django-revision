#!/bin/bash

echo ">>> Collecting static files..."
python manage.py collectstatic --noinput

echo ">>> Applying database migrations..."
python manage.py migrate --noinput

echo ">>> Creating superuser..."
python manage.py createsuperuser --noinput

echo ">>> Starting server..."
python manage.py runserver 0.0.0.0:3000