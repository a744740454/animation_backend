from common.res_code import SUCCESS
from models.image.service import ImageModel
from models.user_rel_image.service import UserRelImageModel
from utils.tools import get_image_url
from config.config import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
from middleware.decorator import login_require
from flask import g


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
    def get_image_info(cls, request_obj):
        page = request_obj.page.data or DEFAULT_PAGE
        page_size = request_obj.page_size.data or DEFAULT_PAGE_SIZE
        images = ImageModel.query_image_info(page, page_size)

        result = []
        for i in images:
            result.append(i.to_json())
        return SUCCESS, result

    @classmethod
    def collect_or_cancel(cls, request_obj):
        """
        收藏或取消收藏
        """

        image_rel_user = UserRelImageModel.query_image_rel_user(g.user_id, request_obj.id.data)

        # 如果未收藏就收藏
        if not image_rel_user:
            UserRelImageModel.add_image_rel_user(user_id=g.user_id, image_id=request_obj.id.data)
        else:
            UserRelImageModel.delete_image_rel_user(rel_id=image_rel_user.id)

        return SUCCESS, {}
