# built-in package
import jwt
import time
import hashlib
import uuid
import random

# project package
from config import CONF
from utils.redis import MyRedis

# third package
from flask import url_for


def hash_password(password):
    hl = hashlib.md5()

    # 此处必须声明encode
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    hl.update(password.encode(encoding='utf-8'))
    return hl.hexdigest()


def encode_jwt(payload: dict, user_id: str):
    payload.update({
        "user_id": user_id,
        "ex": int(time.time()) + 86400 * 15
    })
    encoding_jwt = jwt.encode(payload, CONF["jwt"]["key"], algorithm='HS256')
    r = MyRedis()
    r.set(get_token_key(user_id), "1", ex=86400 * 30)
    return encoding_jwt


def decode_jwt(token):
    payload = jwt.decode(token, CONF["jwt"]["key"], algorithms=['HS256'])
    return payload


def get_image_url(url):
    protocol = CONF["minio"]["protocol"]
    oss_endpoint = CONF["minio"]["endpoint"]

    return protocol + "://" + oss_endpoint + "/" + "animation" + "/" + url


def get_token_key(user_id):
    return "{}_token".format(user_id)


def get_static_path(user_id, mime_type):
    if mime_type == "image/jpeg":
        return "static/avatar/{}.jpg".format(user_id)
    else:
        return "static/avatar/{}.png".format(user_id)


def create_file_name():
    """
    对用户上传的文件名进行随机生成
    """
    return str(uuid.uuid4()) + ".jpg"


def create_id():
    return uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid1()) + str(random.random()))
