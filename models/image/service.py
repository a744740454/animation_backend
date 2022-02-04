from models.base.service import model_wrapper
from .Image import ImageInfo
from sqlalchemy.orm.session import Session


class ImageModel:

    @classmethod
    @model_wrapper
    def insert_image_info(cls, image, session):
        session.add(image)
        session.commit()

    @classmethod
    @model_wrapper
    def query_image_detail_by_image_id(cls, image_id, session: Session):
        result = session.query(ImageInfo).filter_by(id=image_id).first()
        return result

    @classmethod
    @model_wrapper
    def query_image_info(cls, page, page_size, session: Session):
        result = session.query(ImageInfo).limit(page_size).offset((page - 1) * page_size)
        return result
