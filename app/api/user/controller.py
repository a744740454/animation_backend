from app.api.base.controller import BaseView
from app.api.user.service import RegisterService, LoginService, UserService
from protocols.user_protocols.register_protocol import RegisterProtocol
from protocols.user_protocols.login_protocol import LoginProtocol
from protocols.user_protocols.user_protocol import UserInfoProtocol, AuthorProtocol
from middleware.decorator import login_require


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


class UserInfoController(BaseView):
    decorators = (login_require,)
    methods = ["GET"]
    post_protocol = RegisterProtocol

    view_func = {
        "get": UserService.get_user_info
    }


class AvatarController(BaseView):
    decorators = (login_require,)
    methods = ["POST"]
    view_func = {
        "post": UserService.upload_avatar
    }


class AuthorController(BaseView):
    decorators = (login_require,)
    methods = ["GET"]
    get_protocol = AuthorProtocol

    view_func = {
        "get": UserService.get_author_info
    }
