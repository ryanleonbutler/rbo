[![Black][black badge]][black]
[![Flake8][flake8 badge]][flake8]
[![Imports][isort badge]][isort]
[![License][license badge]][license]
[![Last Commit][commit badge]][commit]


<!-- Links -->
[commit]: https://github.com/ryanleonbutler/rbo/commit/HEAD
[python]: https://www.python.org/
[license]: https://github.com/ryanleonbutler/rbo/blob/main/License.txt
[github]: https://github.com/ryanleonbutler/rbo
[black]: https://github.com/psf/black
[flake8]: https://github.com/PyCQA/flake8
[isort]: https://pycqa.github.io/isort/

<!-- Badges -->
[commit badge]: https://img.shields.io/github/last-commit/ryanleonbutler/rbo
[license badge]: https://img.shields.io/github/license/ryanleonbutler/rbo
[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[flake8 badge]: https://img.shields.io/badge/linter-flake8-yellow
[isort badge]: https://img.shields.io/badge/%20imports-isort-%231674b1

# rbo - Deployment Manual

## Launch EC2 Instance
* [AWS Console](https://console.aws.amazon.com/)
* AMI -> Amazon Linux 2 AMI (HVM), SSD Volume Type
* Choose Instance Type
* Elastic IP to associate: xxx.xxx.xxx.xxx

## EC2 Host configuration

```bash
# SSH to webserver - Alias
myblog
```
```bash
#! /bin/bash

# Update system and install dependencies
sudo yum update -y
sudo yum install gcc openssl-devel bzip2-devel libffi-devel git -y
sudo amazon-linux-extras install nginx1

# Install latest SQLite
cd /opt
sudo wget https://www.sqlite.org/2020/sqlite-autoconf-3340000.tar.gz
sudo tar -xzf sqlite-autoconf-3340000.tar.gz
cd sqlite-autoconf-3340000
sudo ./configure
sudo make
sudo make install
cd /opt
sudo rm -rf sqlite-autoconf-3340000.tar.gz

# Install Python 3.9
sudo wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz
sudo tar xzf Python-3.9.0.tgz
cd Python-3.9.0 
LD_RUN_PATH=/usr/local/lib sudo ./configure --enable-optimizations
LD_RUN_PATH=/usr/local/lib make
LD_RUN_PATH=/usr/local/lib sudo make altinstall
cd /opt
sudo rm -rf Python-3.9.0.tgz
python3.9 -m pip install --upgrade pip

# Test Python 3.9 and latest SQLite
python3.9 -V >> /home/ec2-user/ec2_bootstrap.log 2>&1
python3.9 -c "import sqlite3; print(f'SQLite {sqlite3.sqlite_version}')" >> /home/ec2-user/ec2_bootstrap.log

# Create a directory for the project
mkdir /home/ec2-user/rbo
mkdir /home/ec2-user/rbo_backup

# Python venv and pip install requirements.txt
python3.9 -m venv /home/ec2-user/rbo/venv
/home/ec2-user/rbo/venv/bin/pip install -r /home/ec2-user/rbo/requirements.txt
```

## Setup Django
```bash
/home/ec2-user/rbo/venv/bin/python manage.py migrate
/home/ec2-user/rbo/venv/bin/python manage.py makemigrations blog
/home/ec2-user/rbo/venv/bin/python manage.py collectstatic
```

## Configure Gunicorn
```bash
# Test Gunicorn is running
cd /home/ec2-user/rbo
gunicorn --bind 0.0.0.0:8000 rbo_django.wsgi
curl -vL http://127.0.0.1:8000/blog

# Create service file
sudo nano /etc/systemd/system/gunicorn.service
```
```
# /etc/systemd/system/gunicorn.service - contents

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ec2-user
Group=nobody
WorkingDirectory=/home/ec2-user/rbo
ExecStart=/home/ec2-user/rbo/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ec2-user/rbo/rbo_django.sock rbo_django.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable gunicorn.service
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```

## Nginx Configuration
```bash
sudo nano /etc/nginx/nginx.conf
```
```bash
# Add/edit the following to the file and comment out the default config
...
user ec2-user;
...
server {
    listen 80;
    server_name origin.ryanbutler.online;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ec2-user/rbo;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ec2-user/rbo/rbo_django.sock;
    }
}
...
```

```bash
sudo nano /etc/nginx/proxy_params
```
```bash
# /etc/nginx/proxy_params - contents

proxy_set_header Host $http_host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```
```bash
sudo systemctl restart nginx
sudo nginx -t
```

## Test
```
curl -vL https://ryanbutler.online
```