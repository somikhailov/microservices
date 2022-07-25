#!/bin/bash

docker-compose exec flask-micro python manage.py recreate_db
docker-compose exec flask-micro python manage.py seed_db 