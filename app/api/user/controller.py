from app.api.base.controller import BaseView
from app.api.user.service import RegisterService
from protocols.user_protocols.protocol import UserInfoProtocol


class LoginController(BaseView):
    methods = ["GET"]  # 允许的请求方式

    @classmethod
    def get(cls):
        return "hello"


class RegisterController(BaseView):
    methods = ["POST"]  # 允许的请求方式
    post_protocol = UserInfoProtocol
    view_func = {
        "post": RegisterService.register
    }
