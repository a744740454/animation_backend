from common.res_code import SUCCESS, USER_NOT_FOUND, ERR_PASSWORD, USER_EXISTS
from common.error import APIError
from models.user.service import UserModel
from utils.tools import hash_password, encode_jwt, get_static_path
from protocols.user_protocols.register_protocol import RegisterProtocol
from protocols.user_protocols.login_protocol import LoginProtocol
from flask import g, request


class RegisterService:

    @classmethod
    def register(cls, request_obj: RegisterProtocol):
        """
        注册信息
        """
        # 校验用户是否已经存在
        user = UserModel.query_user_by_account(request_obj.username.data)
        if user:
            raise APIError(USER_EXISTS)

        # 将请求赋值给model对象
        user_obj = UserModel.set_json_response(request_obj)

        # 哈希密码
        password = hash_password(request_obj.password.data)

        # 插入数据库
        user_obj.password = password
        UserModel.insert_user_info(user_obj)
        return SUCCESS, {}


class LoginService:

    @classmethod
    def login(cls, request_obj: LoginProtocol):
        account = request_obj.username.data
        user = UserModel.query_user_by_account(account)

        if not user:
            raise APIError(USER_NOT_FOUND)

        # 哈希密码
        password = hash_password(request_obj.password.data)

        # 校验密码是否正确
        if password != user.password:
            raise APIError(ERR_PASSWORD)

        # 签发token
        jwt = encode_jwt({
            "user_name": user.username
        }, user_id=user.id)
        return SUCCESS, {"jwt": jwt}


class UserService:
    @classmethod
    def get_user_info(cls, request_obj):
        user = UserModel.query_user_by_id(g.user_id)
        result = user.to_json()
        result.pop("password")
        return SUCCESS, result

    @classmethod
    def upload_avatar(cls, request_obj):
        avatar = request.files.get("avatar")

        # 保存图片
        avatar_path = get_static_path(g.user_id, avatar.mimetype)
        avatar.save(avatar_path)

        # 更新头像地址
        user = UserModel.query_user_by_id(g.user_id)
        user.avatar = avatar_path
        user.save()

        return SUCCESS, {}
