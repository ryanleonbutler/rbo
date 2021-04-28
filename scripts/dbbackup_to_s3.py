#!/usr/bin/env python3

from bisect import bisect_left
from pathlib import Path

import boto3


class S3Sync:
    """Class needed for syncing local direcory to a S3 bucket"""

    def __init__(self):
        """Initialize class with boto3 client"""
        self.s3 = boto3.client("s3")

    def sync(self, source: str, dest: str) -> list[str]:
        """
        Sync source to dest, this means that all elements existing in
        source that not exists in dest will be copied to dest.

        No element will be deleted.

        :param source: Source folder.
        :param dest: Destination folder.

        :return: None
        """

        paths = self.list_source_objects(source_folder=source)
        objects = self.list_bucket_objects(dest)

        # Getting the keys and ordering to perform binary search
        # each time we want to check if any paths is already there.
        object_keys = [obj["Key"] for obj in objects]
        object_keys.sort()
        object_keys_length = len(object_keys)

        for path in paths:
            # Binary search.
            index = bisect_left(object_keys, path)
            if index == object_keys_length:
                # If path not found in object_keys, it has to be sync-ed.
                self.s3.upload_file(str(Path(source).joinpath(path)), Bucket=dest, Key=path)

    def list_bucket_objects(self, bucket: str) -> list[dict]:
        """
        List all objects for the given bucket.

        :param bucket: Bucket name.
        :return: A [dict] containing the elements in the bucket.

        Example of a single object.

        {
            'Key': 'example/example.txt',
            'LastModified': datetime.datetime(2019, 7, 4, 13, 50, 34, 893000, tzinfo=tzutc()),
            'ETag': '"b11564415be7f58435013b414a59ae5c"',
            'Size': 115280,
            'StorageClass': 'STANDARD',
            'Owner': {
                'DisplayName': 'webfile',
                'ID': '75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a'
            }
        }

        """
        try:
            contents = self.s3.list_objects(Bucket=bucket)["Contents"]
        except KeyError:
            # No Contents Key, empty bucket.
            return []
        else:
            return contents

    @staticmethod
    def list_source_objects(source_folder: str) -> list[str]:
        """
        :param source_folder:  Root folder for resources you want to list.
        :return: A [str] containing relative names of the files.

        Example:

            /tmp
                - example
                    - file_1.txt
                    - some_folder
                        - file_2.txt

            >>> sync.list_source_objects("/tmp/example")
            ['file_1.txt', 'some_folder/file_2.txt']

        """

        path = Path(source_folder)

        paths = []

        for file_path in path.rglob("*"):
            if file_path.is_dir():
                continue
            str_file_path = str(file_path)
            str_file_path = str_file_path.replace(f"{str(path)}/", "")
            paths.append(str_file_path)

        return paths


if __name__ == "__main__":
    sync = S3Sync()
    sync.sync("/home/ec2-user/rbo_backup", "rbobackup")
