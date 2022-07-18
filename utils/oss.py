# 引入MinIO包。
from minio import Minio
# from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
#                          BucketAlreadyExists)

# 使用endpoint、access key和secret key来初始化minioClient对象。
minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=False)

# 调用make_bucket来创建一个存储桶。
# try:
# minioClient.make_bucket("maylogs", location="us-east-1")
# except BucketAlreadyOwnedByYou as err:
#        pass
# except BucketAlreadyExists as err:
#        pass
# except ResponseError as err:
#        raise
# else:
#         try:
minioClient.fput_object('maylogs', 'pumaserver_debug.log', 'test.py')
        # except ResponseError as err:
        #        print(err)
