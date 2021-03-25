#!/bin/bash

BACKUP_FILE="blog.dump"
BACKUP_DIR="/home/ec2-user/rbo_backup"
mkdir -p "$BACKUP_DIR"
chown ec2-user -R "$BACKUP_DIR"

# Backup
mysqldump -u root blog > "$BACKUP_DIR"/"$BACKUP_FILE"

# Delete backups older than 30 days
if find "$BACKUP_DIR" -name "$BACKUP_FILE" -type f -mtime -31 | grep -q .
then
        find "$BACKUP_DIR" -type f -mtime +30 -delete
fi

last_backup=$(ls -t "$BACKUP_DIR" | head -n 1)
if [ ! "$last_backup" ] || ! cmp -s "$BACKUP_DIR"/"$BACKUP_FILE" "$BACKUP_DIR"/"$last_backup"
then
        today=`date "+%Y-%m-%d_%H:%M:%S"`
        cp "$BACKUP_FILE" "$BACKUP_DIR/$today.dump"
fi