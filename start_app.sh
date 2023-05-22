#!/bin/bash
 cd django_app
 python manage.py runserver &
 cd ..
 cd frontend
 npm run serve