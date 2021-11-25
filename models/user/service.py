from models.base.service import model_wrapper


class UserModelService:

    @classmethod
    @model_wrapper
    def insert_user_info(cls, user, session):
        session.add(user)
        session.commit()

