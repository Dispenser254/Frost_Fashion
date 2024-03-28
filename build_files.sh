#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run Django management commands
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear
