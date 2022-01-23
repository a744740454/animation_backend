from common.res_code import SUCCESS
from models.user.service import UserModelService
from utils.tools import hash_password


class RegisterService:

    @classmethod
    def register(cls, request_json):
        user_obj = UserModelService.set_json_response(request_json)
        user_obj.password = hash_password(user_obj.password)  # 对密码进行加密处理
        UserModelService.insert_user_info(user_obj)
        return SUCCESS, {}
