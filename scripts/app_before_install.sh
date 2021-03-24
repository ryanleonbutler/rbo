#!/bin/bash

BACKUP_FILE="/var/lib/mysql/blog"
mkdir -p /home/ec2-user/rbo_backup
chown ec2-user -R /home/ec2-user/rbo_backup
BACKUP_DIR="/home/ec2-user/rbo_backup"

# Delete backups older than 30 days
if find "$BACKUP_FILE" -type f -mtime -31 | grep -q .
then
        find "$BACKUP_DIR" -type f -mtime +30 -delete
fi

last_backup=$(ls -t "$BACKUP_DIR" | head -n 1)
if [ ! "$last_backup" ] || ! cmp -s "$BACKUP_FILE" "$BACKUP_DIR/$last_backup"
then
        today=`date "+%Y-%m-%d_%H:%M:%S"`
        cp "$BACKUP_FILE" "$BACKUP_DIR/$today.sqlite3"
fi