<img align="center" src="/static/markdownx/2021/01/15/blogging-part1.jpg_5492f4cf-c58f-461b-82d9-f1f913a08201.jpg" alt="blogging-part1" width="1920"/>

Welcome to this first part in multi-part series of posts, where I will be walking you through how I deployed this blog. But first, please do reach out to me on [Twitter](https://twitter.com/ryanleonbutler) or [LinkedIn](https://www.linkedin.com/in/ryanleonbutler/) with your thoughts about my blog or if you just want to talk about anything related to Python.

# Part 1

# Table of Contents
1. [Introduction](#intro)
2. [Hosting](#hosting)
3. [Django](#django)
4. [Gunicorn](#gunicorn)
5. [NGINX](#nginx)
6. [Testing](#testing)


<div id='intro' markdown='1'></div>

## 1. Introduction
In this post I will be guiding you on how to setup a host where you can deploy Django, Gunicorn and NGINX in order to serve your website or blog. Note that I will be focusing on configuring the host, installing Django, Gunicorn and NGINX in order to serve the default Django new project website. I will be diving deeper into configuring and deploying the blog app using Django in Part 2 of this series.


<div id='hosting' markdown='1'></div>

## 2. Hosting
You can choose any hosting provider, I just chose [AWS](https://aws.amazon.com/) and EC2 because of the breadth of services they have to offer as well as the maturity of their products. There is also the obvious [Free Tier](https://aws.amazon.com/free/) offering, which is great for starting out or playing around with their services for free.

* If you also want to use AWS, open a new account [here](https://portal.aws.amazon.com/billing/signup#/start).
* Open the EC2 Console and choose the appropriate [Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). I decided to use the [Ireland](https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1#LaunchInstanceWizard) Region.
* Next, choose the following [AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html): Amazon Linux 2 AMI (HVM), SSD Volume Type. Again you can technically use any Linux based AMI, but in order to follow along with this guide I recommend you choose the same AMI I used.
* Choose an appropriate [instance type](https://aws.amazon.com/ec2/instance-types/). I used a t3.micro instance which is part of the Free Tier offering.
* Associate an [Elastic IP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html). This will provide you with a static public IP, which you can use in your public DNS record for your custom domain name in order to route to your website.

### EC2 Host configuration
For the EC2 Host configuration, you can run the below commands once you have a [SSH connection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html) to your instance or you can use it as a [start-up script](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) in the EC2 launch wizard.
```
# SSH to your new instance - I configured an alias which is super handy.
# In my ~/.zshrc file

alias myblog="ssh <username>@<elastic-ip> -i ~/path/to/private_key.pem"
```
```
myblog
```
```
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

# Install Python 3.9, which is the latest Python version at the time of this post
sudo wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz
sudo tar xzf Python-3.9.0.tgz
cd Python-3.9.0 
LD_RUN_PATH=/usr/local/lib sudo ./configure --enable-optimizations
LD_RUN_PATH=/usr/local/lib make
LD_RUN_PATH=/usr/local/lib sudo make altinstall
cd /opt
sudo rm -rf Python-3.9.0.tgz

# Test Python 3.9 and latest SQLite
python3.9 -V
python3.9 -c "import sqlite3; print(f'SQLite {sqlite3.sqlite_version}')"

# Create a Python virtual environment using venv and pip install your requirements.txt or manually install each package
cd ~/myproject
python3.9 -m venv ~/myproject/venv
source venv/bin/activate
(venv) pip install -r requirements.txt
(venv) deactivate
```
```
# Contents of my requirements.txt and the versions I used at the time of this post
asgiref==3.3.1
boto3==1.16.38
botocore==1.19.38
Django==3.1.4
django-markdown==0.8.4
django-markdownx==3.0.1
gunicorn==20.0.4
jmespath==0.10.0
Markdown==3.3.3
Pillow==8.0.1
python-dateutil==2.8.1
pytz==2020.4
s3transfer==0.3.3
six==1.15.0
sqlparse==0.4.1
urllib3==1.26.2
```

<div id='django' markdown='1'></div>

## 3. [Django](https://www.djangoproject.com/)
Django is one of the most popular web frameworks for Python. It is mature, stable and approachable, therefore my first choice for developing web apps using Python.

We will start a new Django project, create a "blog" app, create a super user and the default SQLite database.
```
cd ~/myproject
source venv/bin/activate
(venv) django-admin startproject myproject .
(venv) python manage.py startapp blog
(venv) python manage.py migrate
(venv) python manage.py createsuperuser
(venv) deactivate
```

<div id='gunicorn' markdown='1'></div>

## 4. [Gunicorn](https://gunicorn.org/)
We will be using Gunicorn as a HTTP server for our Django web app.
```
# Test if Gunicorn is working correctly.
cd ~/myproject
source venv/bin/activate
(venv) gunicorn --bind 0.0.0.0:8000 myproject.wsgi
(venv) curl -vL http://127.0.0.1:8000/blog
(venv) deactivate

# Create a new service file for Gunicorn to run as a service on your host.
sudo nano /etc/systemd/system/gunicorn.service
```
```
# Contents of /etc/systemd/system/gunicorn.service.

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ec2-user
Group=nobody
WorkingDirectory=/home/ec2-user/myproject
ExecStart=/home/ec2-user/myproject/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ec2-user/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```

```
# Enable and start the service.
sudo systemctl enable gunicorn.service
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```

<div id='nginx' markdown='1'></div>

## 5. [NGINX](https://nginx.org/)
We will be using NGINX as a reverse proxy to serve requests to our Gunicorn HTTP server. 

First off, edit the default NGINX configuration file.
```
sudo nano /etc/nginx/nginx.conf
```
```
# Truncated contents of /etc/nginx/nginx.conf.
# Add/Edit the below to the config file and comment out the default server config.

...
user ec2-user;
...
server {
    listen 80;
    server_name example.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ec2-user/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ec2-user/myproject/myproject.sock;
    }
}
...
```

Next we need to configure NGINX's reverse proxy parameters.
```
sudo nano /etc/nginx/proxy_params
```
```
# Contents of /etc/nginx/proxy_params

proxy_set_header Host $http_host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

Restart NGINX and test.
```
sudo systemctl restart nginx
sudo nginx -t
```

<div id='testing' markdown='1'></div>

## 6. Testing
With both NGINX and your Gunicorn service running you should be able to test your Django website locally and publicly (if you already configured your public DNS record to resolve to your EC2 instance's elastic IP).

```
curl -vL http://127.0.0.1

HTTP/2 200
content-type: text/html; charset=utf-8
content-length: 7049
vary: Accept-Encoding
server: nginx/1.18.0
date: Thu, 24 Dec 2020 03:38:35 GMT
x-frame-options: DENY
x-content-type-options: nosniff
referrer-policy: same-origin
```

![](/static/markdownx/2020/12/24/django-default-ca8921fb-5261-4c84-9cef-c385a88e5b5f.png)

## Last words

This wraps up Part 1 of my multi-series posts where we will be deploying a blog similar to the one I have. In the next part we will be diving deeper into Django and how I managed to add markdown support for easily writing posts. Till then, keep safe.

*Best Regards*

*Ryan*