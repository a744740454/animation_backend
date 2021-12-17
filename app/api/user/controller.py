from app.api.base.controller import BaseView
from app.api.user.service import RegisterService
from common.response import response
from flask import request
from protocols.user_protocols.protocol import UserInfoProtocol


class LoginController(BaseView):
    methods = ["GET"]  # 允许的请求方式

    @classmethod
    def get(cls):
        return "hello"


class RegisterController(BaseView):
    methods = ["POST"]  # 允许的请求方式

    @classmethod
    def post(cls):
        request_json = request.json
        # 校验数据是否正确
        reg_protocol = UserInfoProtocol()
        reg_protocol.validate_for_api()
        status, result = RegisterService.register(request_json)
        return response(status, result)
