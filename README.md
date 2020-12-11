# rbo - Deploy Manual

### Launch EC2 Instance
* EC2 Console (Ireland): https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1#LaunchInstanceWizard:
* AMI: Amazon Linux 2 AMI (HVM), SSD Volume Type
* Instance Type: t2.micro
* Elastic IP to associate: 54.229.224.188

### Host configuration

```bash
# SSH to webserver - Alias
myblog
```
```bash
#! /bin/bash

# Update system and install dependencies
sudo yum update -y
sudo yum install gcc openssl-devel bzip2-devel libffi-devel git -y

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

# Test Python 3.9 and latest SQLite
python3.9 -V >> /home/ec2-user/ec2_bootstrap.log 2>&1
python3.9 -c "import sqlite3; print(f'SQLite {sqlite3.sqlite_version}')" >> /home/ec2-user/ec2_bootstrap.log

# Generate SSH Key and add to Github
cd /home/ec2-user
ssh-keygen -t rsa -b 4096 -C "ryanleonbutler@gmail.com" -f /home/ec2-user/.ssh/id_rsa -q -N ""
eval "$(ssh-agent -s)" >> /home/ec2-user/ec2_bootstrap.log
echo -e "Host github.com\n\tIdentityFile /home/ec2-user/.ssh/id_rsa\n\tStrictHostKeyChecking no" > /home/ec2-user/.ssh/config
chmod go-w /home/ec2-user/.ssh/config
ssh-add -k ~/.ssh/id_rsa
ID_RSA_PUB=`cat /home/ec2-user/.ssh/id_rsa.pub`
GITHUB_TOKEN="9da8d40c9b3d052eef398b3724381bc43f5c0ebd"
curl -H "Authorization: token ${GITHUB_TOKEN}" --data "{\"title\":\"myblog\",\"key\":\"${ID_RSA_PUB}\"}" https://api.github.com/user/keys

# Clone `rbo` repository
cd /home/ec2-user
git clone git@github.com:ryanleonbutler/rbo.git

# Python venv and pip install requirements.txt
cd /home/ec2-user/rbo
python3.9 -m venv /home/ec2-user/rbo/venv
/home/ec2-user/rbo/venv/bin/pip install -r /home/ec2-user/rbo/requirements.txt