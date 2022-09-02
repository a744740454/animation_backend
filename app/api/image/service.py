# built-in package

# project package
from common.res_code import SUCCESS
from models.image.service import ImageModel
from models.author.service import AuthorModel
from models.tag.service import TagModel
from models.tag_rel_image.service import TagRelImageModel
from models.user_rel_image.service import UserRelImageModel
from models.author_rel_image.service import AuthorRelImageModel
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
            image_url = get_image_url(i.original_url)
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
            image.original_url = get_image_url(image.original_url)
            image.thumbnail_url = get_image_url(image.thumbnail_url)
            response = image.to_json()

        return SUCCESS, response

    @classmethod
    def get_image_info(cls, request_obj):
        page = request_obj.page.data or DEFAULT_PAGE
        page_size = request_obj.page_size.data or DEFAULT_PAGE_SIZE
        images = ImageModel.query_image_info(page, page_size)

        # 判断图片是否被用户收藏
        user_rel_images = UserRelImageModel.query_infos_by_user_id(g.user_id)
        image_ids = [u.image_id for u in user_rel_images]
        result = []
        for i in images:
            i.original_url = get_image_url(i.original_url)
            i.thumbnail_url = get_image_url(i.thumbnail_url)
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
        """
        获取用户收藏的图片信息
        """
        page = request_obj.page.data
        page_size = request_obj.page_size.data

        user_rel_image = UserRelImageModel.query_infos_by_user_id(g.user_id)
        image_ids = [u.image_id for u in user_rel_image]
        # 查询图片信息
        images = ImageModel.query_image_by_image_ids(image_ids=image_ids, page_size=page_size, page=page)
        for i in images:
            i.original_url = get_image_url(i.original_url)
            i.thumbnail_url = get_image_url(i.thumbnail_url)
        result = [i.to_json() for i in images]
        return SUCCESS, {
            "image": result
        }

    @classmethod
    def upload_image(cls, request_obj):
        """
        上传图片
        """
        original_img = request.files.get("original_img")
        thumbnail_image = request.files.get("thumbnail_img")
        content_type = original_img.headers["Content-Type"]
        file_name = create_file_name()
        # 通过流的方式上传图片
        minio = AnimationMinio()
        minio.stream_upload("original/" + file_name, original_img,
                            content_type=content_type)
        minio.stream_upload("thumbnail/" + file_name, thumbnail_image,
                            content_type=content_type)

        # 获取作者id
        if not request_obj.author_name.data:
            author_id = g.user_id
        else:
            # ·判断作者是否存在不存在就创建一个作者
            author = AuthorModel.query_author_by_name(request_obj.author_name.data)
            if not author:
                author_id = AuthorModel.insert_author(request_obj.author_name.data)
            else:
                author_id = author.id

        tags = []
        # 1.判断标签是否存在，不存在的情况下新建
        if request_obj.tags.data:
            tags = eval(request_obj.tags.data)

        # 之前存在的tag
        old_tags = TagModel.query_tags_by_names(tags)
        old_tags_name = [t.name for t in old_tags]
        tag_ids = [t.id for t in old_tags]
        # 需要新增的tag
        new_tags_name = list(set(tags) - set(old_tags_name))

        for tag in new_tags_name:
            tag_ids.append(TagModel.insert_tag(tag))

        # 2.图片插入
        image_id = ImageModel.insert_image_info(
            image_name=file_name,
            thumbnail_url="thumbnail/" + file_name,
            original_url="original/" + file_name,
            author_id=author_id,
            image_desc=request_obj.desc.data,
            title=request_obj.title.data,
        )

        # 3.标签已经存在，建立image和标签的关联关系
        for tag_id in tag_ids:
            TagRelImageModel.add_tag_rel_image(tag_id, image_id)

        # 4. 建立作者和image的关联关系
        AuthorRelImageModel.add_author_rel_image(author_id, image_id)

        return SUCCESS, {}
