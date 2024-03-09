#!/bin/bash

# Run database migrations
python manage.py migrate

python manage.py collectstatic --no-input 

# Dump initial data after migrations
python manage.py loaddata initials/accounts_initial_data.json
python manage.py loaddata initials/flights_initial_data.json

# Start the Django development server
python manage.py runserver 0.0.0.0:8000
