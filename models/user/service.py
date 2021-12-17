from models.base.service import model_wrapper
from models.user.User import UserInfo


class UserModelService:

    @classmethod
    @model_wrapper
    def insert_user_info(cls, user, session):
        session.add(user)
        session.commit()

    @classmethod
    def set_json_response(cls, request_json):
        user = UserInfo()
        user.name = request_json.get("username", "")
        user.password = request_json.get("password", "")
        user.email = request_json.get("email", "")
        user.telephone = request_json.get("telephone", "")
        return user
