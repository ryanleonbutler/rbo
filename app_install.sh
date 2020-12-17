#!/bin/bash

/home/ec2-user/rbo/venv/bin/python /home/ec2-user/rbo/manage.py migrate
/home/ec2-user/rbo/venv/bin/python /home/ec2-user/rbo/manage.py makemigrations blog
/home/ec2-user/rbo/venv/bin/python /home/ec2-user/rbo/manage.py collectstatic
