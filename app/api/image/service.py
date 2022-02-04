from common.res_code import SUCCESS
from models.image.service import ImageModel


class ImageService:

    @classmethod
    def insert_image_info(cls, request_obj):
        pass

    @classmethod
    def get_image_detail(cls, request_obj):
        image_id = request_obj.id.data
        result = ImageModel.query_image_detail_by_image_id(image_id)
        return SUCCESS, {}

    @classmethod
    def get_image_info(cls, request_obj):
        page = request_obj.page.data
        page_size = request_obj.page_size.data
        result = ImageModel.query_image_info(page, page_size)
        return SUCCESS, {}
