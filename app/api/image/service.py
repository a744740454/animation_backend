from common.res_code import SUCCESS
from models.image.service import ImageModel
from utils.tools import get_image_url
from config.config import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
from middleware.decorator import login_require


class ImageService:

    @classmethod
    def insert_image_info(cls, request_obj):
        pass

    @classmethod
    def get_banner(cls, request_obj):
        page = request_obj.page.data or DEFAULT_PAGE
        page_size = request_obj.page_size.data or DEFAULT_PAGE_SIZE
        images = ImageModel.query_image_info(page, page_size)
        image_urls = []
        for i in images:
            image_url = get_image_url(i.image_name)
            image_urls.append(image_url)
        return SUCCESS, {
            "image_urls": image_urls
        }

    @classmethod
    def get_image_detail(cls, request_obj):
        image_id = request_obj.id.data
        result = ImageModel.query_image_detail_by_image_id(image_id)
        return SUCCESS, {}

    @classmethod
    # @login_require
    def get_image_info(cls, request_obj):
        page = request_obj.page.data or DEFAULT_PAGE
        page_size = request_obj.page_size.data or DEFAULT_PAGE_SIZE
        images = ImageModel.query_image_info(page, page_size)

        result = []
        for i in images:
            result.append(i.to_json())
        return SUCCESS, result

