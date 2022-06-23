import jwt
import time
import hashlib
from config import CONF
from flask import url_for
from utils.redis import MyRedis


def hash_password(password):
    hl = hashlib.md5()

    # 此处必须声明encode
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    hl.update(password.encode(encoding='utf-8'))
    return hl.hexdigest()


def encode_jwt(payload: dict, user_id: str):
    payload.update({
        "user_id":user_id,
        "ex": int(time.time()) + 86400 * 15
    })
    encoding_jwt = jwt.encode(payload, CONF["jwt"]["key"], algorithm='HS256')
    r = MyRedis()
    r.set(get_token_key(user_id), "1", ex=86400 * 30)
    return encoding_jwt


def decode_jwt(jwt):
    payload = jwt.decode(jwt, CONF["jwt"]["key"], algorithms=['HS256'])
    return payload


def get_image_url(static_file_name):
    return url_for("static", filename=static_file_name)


def get_token_key(user_id):
    return "{}_token".format(user_id)
