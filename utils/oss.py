# built-in package
import io

# project package
from config import CONF

# third package
from minio import Minio
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


class AnimationMinio:
    def __init__(self, endpoint=CONF["minio"]["endpoint"], access_key=CONF["minio"]["access_key"],
                 secret_key=CONF["minio"]["secret_key"]):
        self.minio = Minio(endpoint, access_key, secret_key, secure=False)
        if not self._bucket_exists("animation"):
            self._make_buckets("animation")

    def upload_file(self, object_name, local_file_path):
        """
        文件上传
        """
        content_type = "image/jpeg"
        self.minio.fput_object("animation", object_name, local_file_path, content_type=content_type)

    def download_file(self, object_name, local_file_path):
        """
        文件上传
        """
        self.minio.fget_object("animation", object_name, local_file_path)

    def _make_buckets(self, bucket_name):
        self.minio.make_bucket(bucket_name)

    def _bucket_exists(self, bucket_name):
        return self.minio.bucket_exists(bucket_name)

    def stream_upload(self, object_name, data, content_type="image/jpeg"):
        data = data.read()
        file_length = len(data)
        file = io.BytesIO(data)
        self.minio.put_object("animation", object_name, file, file_length, content_type)


class TencentOss:
    def __init__(self, secret_id=CONF["tencent_oss"]["secret_id"], secret_key=CONF["tencent_oss"]["secret_key"],
                 region=CONF["tencent_oss"]["region"]):
        config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
        self.client = CosS3Client(config)
        self.bucket = CONF["tencent_oss"]["bucket"]

    def stream_upload(self, stream, key):
        self.client.put_object(
            Bucket=self.bucket,
            Body=stream,
            Key=key
        )

    def create_bucket(self):
        self.client.create_bucket(
            Bucket='animation-1304688700'
        )


if __name__ == '__main__':
    a = TencentOss()
    # a.create_bucket()
    # with open("redis.py", mode='rb+',) as f:
    #     a.upload(f.read(), "test")
    # a.upload_file("image/test.jpg", "1.jpg")
