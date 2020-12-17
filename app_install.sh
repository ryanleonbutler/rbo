#!/bin/bash

/home/ec2-user/rbo/venv/bin/python manage.py migrate
/home/ec2-user/rbo/venv/bin/python manage.py makemigrations blog
/home/ec2-user/rbo/venv/bin/python manage.py collectstatic
