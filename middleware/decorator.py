import time
from utils.tools import decode_jwt, encode_jwt, get_token_key
from utils.redis import MyRedis
from flask import request, g
from common.error import APIError
from common.res_code import USER_NO_LOGIN, TOKEN_EXPIRED


def login_require(func):
    def inner(*args, **kwargs):
        """
        登录校验
        1.校验token是否存在
        2.token解码，判断token是否异常
        3.判断token是否过期
        4.如果token过期一半，需要去redis中读取，重新刷新token
        5.设置全局user_id
        """
        token = request.headers.get("Authorization")

        # 校验token准确性
        if not token:
            raise APIError(USER_NO_LOGIN)

        # 对token解码，判断token准确性
        try:
            payload = decode_jwt(token)
        except Exception as e:
            raise APIError(USER_NO_LOGIN)

        # 判断token是否过期
        ex = payload.get("ex")
        user_id = payload.get("user_id")
        if ex < int(time.time()):
            redis = MyRedis()
            flag = redis.get(get_token_key(user_id))
            if flag:
                # 延长token时间
                # 设置全局变量的token,最后在响应头中进行设置
                g.token = encode_jwt(payload, user_id)
            else:
                # token完全过期
                raise APIError(TOKEN_EXPIRED)

        # 设置user_id
        g.user_id = payload.get("user_id")

        # 走正常的视图函数
        result = func(*args, **kwargs)

        return result
    return inner
