# 引入MinIO包。
from minio import Minio

# from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
#                          BucketAlreadyExists)

# 使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=False)


class AnimationMinio:
    def __init__(self, endpoint, access_key, secret_key):
        self.minio = Minio(endpoint, access_key, secret_key, secure=False)

    def put_file(self, bucket_name, object_name, local_file_path):
        """
        文件上传
        """
        self.minio.fput_object(bucket_name, object_name, local_file_path)

    def get_file(self, bucket_name, object_name, local_file_path):
        """
        文件上传
        """
        self.minio.fget_object(bucket_name, object_name, local_file_path)
