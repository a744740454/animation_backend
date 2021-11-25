from common.res_code import SUCCESS
from models.user.User import UserInfo
from models.user.service import UserModelService


class RegisterService:

    @classmethod
    def register(cls):
        user = UserInfo()
        user.name = "test"
        user.password = "123"
        UserModelService.insert_user_info(user)
        return SUCCESS, {}
