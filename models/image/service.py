from .Image import ImageInfo
from models.init import UserRelImage
from models import session
from utils.tools import create_id
from flask import g


class ImageModel:

    @classmethod
    def insert_image_info(
            cls,
            image_name,
            thumbnail_url,
            original_url,
            image_desc,
            author_id,
            title
    ):
        image = ImageInfo()
        image_id = create_id()
        image.id = image_id
        image.image_name = image_name
        image.thumbnail_url = thumbnail_url
        image.original_url = original_url
        image.image_desc = image_desc
        image.author_id = author_id
        image.title = title
        session.add(image)

        session.commit()
        return image_id

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
