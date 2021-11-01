#!/usr/bin/env python3
from bisect import bisect_left
from pathlib import Path

import boto3


class S3Sync:
    """Class needed for syncing local direcory to a S3 bucket"""

    def __init__(self):
        """Initialize class with boto3 client"""
        self.s3 = boto3.client("s3")

    def upload_object(self, source: str, bucket: str, key: str):
        self.s3.upload_file(source, Bucket=bucket, Key=key)

    def list_bucket_objects(self, bucket: str) -> list[dict]:
        """
        List all objects for the given bucket.

        :param bucket: Bucket name.
        :return: A [dict] containing the elements in the bucket.

        """
        try:
            contents = self.s3.list_objects(Bucket=bucket)["Contents"]
        except KeyError:
            # No Contents Key, empty bucket.
            return []
        else:
            return contents


if __name__ == "__main__":
    sync = S3Sync()
    sync.upload_object("/home/ec2-user/rbo_backup/blog.dump", "rbobackup", "blog.dump")
