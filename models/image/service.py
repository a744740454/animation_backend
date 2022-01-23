from models.base.service import model_wrapper
from models.image.Image import ImageInfo


class ImageService:

    @classmethod
    @model_wrapper
    def insert_image_info(cls, image, session):
        session.add(image)
        session.commit()


    @classmethod
    def query_image_detail_by_image_id(cls):
        pass
