from app.api.base.controller import BaseView
from app.api.user.service import RegisterService, LoginService
from protocols.user_protocols.register_protocol import RegisterProtocol
from protocols.user_protocols.login_protocol import LoginProtocol


class LoginController(BaseView):
    methods = ["POST"]  # 允许的请求方式
    post_protocol = LoginProtocol

    view_func = {
        "post": LoginService.login
    }


class RegisterController(BaseView):
    methods = ["POST"]  # 允许的请求方式
    post_protocol = RegisterProtocol
    view_func = {
        "post": RegisterService.register
    }
