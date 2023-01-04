#!/bin/bash

echo "\n>>> Collecting static files..."
python manage.py collectstatic --noinput

echo "\n>>> Applying database migrations..."
python manage.py migrate --noinput

echo "\n>>> Creating superuser..."
python manage.py createsuperuser --noinput

echo "\n>>> Starting server..."
python manage.py runserver 0.0.0.0:3000