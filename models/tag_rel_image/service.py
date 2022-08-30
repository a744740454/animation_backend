from .tag_rel_image import UserRelImage
from models import session


class UserRelImageModel:

    @classmethod
    def query_image_rel_user(cls, user_id, image_id):
        result = session.query(UserRelImage).filter(UserRelImage.user_id == user_id, UserRelImage.image_id == image_id).first()
        return result

    @classmethod
    def delete_image_rel_user(cls, rel_id):
        session.query(UserRelImage).filter(UserRelImage.id == rel_id).delete()
        session.commit()

    @classmethod
    def add_image_rel_user(cls, user_id, image_id):
        image_rel_user = UserRelImage()
        image_rel_user.user_id = user_id
        image_rel_user.image_id = image_id
        session.add(image_rel_user)
        session.commit()

    @classmethod
    def query_infos_by_user_id(cls, user_id):
        result = session.query(UserRelImage).filter(UserRelImage.user_id == user_id).all()
        return result