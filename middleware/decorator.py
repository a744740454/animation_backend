from utils.tools import decode_jwt
from flask import request,g
from common.error import APIError
from common.res_code import USER_NO_LOGIN


def login_require(func):
    def inner(*args, **kwargs):
        token = request.headers.get("Authorization")

        # 校验token准确性
        if not token:
            raise APIError(USER_NO_LOGIN)

        # 对token解码，判断token准确性
        try:
            payload = decode_jwt(token)
        except Exception as e:
            raise APIError(USER_NO_LOGIN)

        # 设置user_id
        g.user_id = payload.get("user_id")
        result = func(*args, **kwargs)

        # todo 刷新token
        return result

    return inner
