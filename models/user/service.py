from models.base.service import model_wrapper
from models.user.User import UserInfo
from protocols.user_protocols.protocol import UserInfoProtocol


class UserModel:

    @classmethod
    @model_wrapper
    def insert_user_info(cls, user, session):
        session.add(user)
        session.commit()

    @classmethod
    def set_json_response(cls, request_obj: UserInfoProtocol):
        user = UserInfo()
        user.username = request_obj.username.data
        user.password = request_obj.password.data
        user.email = request_obj.email.data
        user.telephone = request_obj.telephone.data
        return user
