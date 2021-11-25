from app.api.base.controller import BaseView
from app.api.user.service import RegisterService
from common.response import response


class LoginController(BaseView):
    methods = ["GET"]  # 允许的请求方式

    @classmethod
    def get(cls):
        return "hello"


class RegisterController(BaseView):
    methods = ["POST"]  # 允许的请求方式

    @classmethod
    def post(cls):
        status, result = RegisterService.register()
        return response(status, result)
