# built-in package

# project package
from common.res_code import SUCCESS
from models.image.service import ImageModel
from models.user_rel_image.service import UserRelImageModel
from utils.tools import get_image_url, create_file_name
from config.config import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
from utils.oss import AnimationMinio

# third package
from flask import g, request


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
        image_id = request_obj.image_id.data
        image = ImageModel.query_image_detail_by_image_id(image_id)
        response = {}
        if image:
            response = image.to_json()
        print(response)
        return SUCCESS, response

    @classmethod
    def get_image_info(cls, request_obj):
        page = request_obj.page.data or DEFAULT_PAGE
        page_size = request_obj.page_size.data or DEFAULT_PAGE_SIZE
        images = ImageModel.query_image_info(page, page_size)

        # 查询获取到的图片和当前登录用户的关系
        user_rel_images = UserRelImageModel.query_infos_by_user_id(g.user_id)
        image_ids = [u.image_id for u in user_rel_images]
        result = []
        for i in images:
            result_dict = i.to_json()
            if i.id in image_ids:
                result_dict["love"] = True
            else:
                result_dict["love"] = False
            result.append(result_dict)
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

    @classmethod
    def get_user_rel_image_info(cls, request_obj):
        page = request_obj.page.data
        page_size = request_obj.page_size.data

        user_rel_image = UserRelImageModel.query_infos_by_user_id(g.user_id)
        image_ids = [u.image_id for u in user_rel_image]
        print(image_ids)
        # 查询图片信息
        images = ImageModel.query_image_by_image_ids(image_ids=image_ids, page_size=page_size, page=page)
        result = [i.to_json() for i in images]
        return SUCCESS, {
            "image": result
        }

    @classmethod
    def upload_image(cls, request_obj):
        """
        上传图片
        """
        file = request.files.get("upload_image")
        file_name = create_file_name()

        # 通过流的方式上传图片
        minio = AnimationMinio()
        minio.stream_upload(file_name, file, file.content_length)

        #·

        return SUCCESS, {}
