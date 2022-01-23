from common.res_code import SUCCESS
from models.user.service import UserModelService
from utils.tools import hash_password


class RegisterService:

    @classmethod
    def register(cls, request_json):
        user_obj = UserModelService.set_json_response(request_json)
        password = hash_password(request_json.get("password"))
        request_json["password"] = password
        UserModelService.insert_user_info(user_obj)
        return SUCCESS, {}
