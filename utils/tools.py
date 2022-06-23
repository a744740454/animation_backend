import jwt
import hashlib
from config import CONF
from flask import url_for


def hash_password(password):
    hl = hashlib.md5()

    # 此处必须声明encode
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    hl.update(password.encode(encoding='utf-8'))
    return hl.hexdigest()


def encode_jwt(payload):
    encoding_jwt = jwt.encode(payload, CONF["jwt"]["key"], algorithm='HS256')
    return encoding_jwt


def decode_jwt(jwt):
    payload = jwt.decode(jwt, CONF["jwt"]["key"], algorithms=['HS256'])
    return payload


def get_image_url(static_file_name):
    return url_for("static", filename = static_file_name)
