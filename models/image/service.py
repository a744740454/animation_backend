from .Image import ImageInfo
from models import session


class ImageModel:

    @classmethod
    def insert_image_info(cls, image):
        session.add(image)
        session.commit()

    @classmethod
    def query_image_detail_by_image_id(cls, image_id):
        result = session.query(ImageInfo).filter(ImageInfo.id == image_id).first()
        return result

    @classmethod
    def query_image_info(cls, page, page_size):
        result = session.query(ImageInfo).limit(page_size).offset((page - 1) * page_size)
        return result

    @classmethod
    def query_image_by_image_ids(cls, image_ids, page, page_size):
        result = session.query(ImageInfo).filter(ImageInfo.id.in_(image_ids)).limit(page_size).offset(
            (page - 1) * page_size)
        return result

    @classmethod
    def query_image_by_author_id(cls, author_id):
        result = session.query(ImageInfo).filter(ImageInfo.author_id == author_id).all()
        return result
