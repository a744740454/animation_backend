from models import session
from models.user.User import UserInfo
from protocols.user_protocols.register_protocol import RegisterProtocol
from sqlalchemy import or_


class UserModel:

    @classmethod
    def insert_user_info(cls, user):
        session.add(user)
        session.commit()

    @classmethod
    def query_user_by_account(cls, account):
        user = session.query(UserInfo).filter(or_(UserInfo.username == account, UserInfo.email == account)).first()
        return user

    @classmethod
    def set_json_response(cls, request_obj: RegisterProtocol):
        user = UserInfo()
        user.username = request_obj.username.data
        user.password = request_obj.password.data
        user.email = request_obj.email.data
        user.telephone = request_obj.telephone.data
        return user
