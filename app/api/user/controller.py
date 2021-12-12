from app.api.base.controller import BaseView
from app.api.user.service import RegisterService
from common.response import response
from flask import request

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
        status, result = RegisterService.register(request_json)
        return response(status, result)
