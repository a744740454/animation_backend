# 引入MinIO包。
from minio import Minio
from config import CONF


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
        self.minio.fput_object("animation", object_name, local_file_path,content_type=content_type)

    def download_file(self, object_name, local_file_path):
        """
        文件上传
        """
        self.minio.fget_object("animation", object_name, local_file_path)

    def _make_buckets(self, bucket_name):
        self.minio.make_bucket(bucket_name)

    def _bucket_exists(self, bucket_name):
        return self.minio.bucket_exists(bucket_name)

    def stream_upload(self, object_name, data, length=-1):
        self.minio.put_object("animation", object_name, data, length)


if __name__ == '__main__':
    a = AnimationMinio()
    a.upload_file("image/test.jpg", "1.jpg")
