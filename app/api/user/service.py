from common.res_code import SUCCESS
from models.user.service import UserModel
from utils.tools import hash_password
from protocols.user_protocols.protocol import UserInfoProtocol

class RegisterService:

    @classmethod
    def register(cls, request_obj:UserInfoProtocol):
        user_obj = UserModel.set_json_response(request_obj)
        password = hash_password(request_obj.password.data)
        request_obj.password.data = password
        UserModel.insert_user_info(user_obj)
        return SUCCESS, {}
