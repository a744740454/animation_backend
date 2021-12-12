from common.res_code import SUCCESS
from models.user.User import UserInfo
from models.user.service import UserModelService
from utils.tools import hash_password


class RegisterService:

    @classmethod
    def register(cls, request_json):
        UserModelService.set_json_response(request_json)
        password = hash_password(request_json.get("password"))
        # username = request_json.get("username")
        # password = request_json.get("password")
        # user = UserInfo()
        # user.name = username
        # user.password = password
        # hash_password()
        # UserModelService.insert_user_info(user)
        return SUCCESS, {}
