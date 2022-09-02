from app.api.base.controller import BaseView
from protocols.image_protocol.protocol import ImageDetailProtocol, ImageInfoProtocol, BannerProtocol, CollectProtocol, \
    UserRelImageProtocol,UploadImageProtocol,GetTagsProtocol
from app.api.image.service import ImageService
from middleware.decorator import login_require


class ImageController(BaseView):
    decorators = (login_require,)
    methods = ["GET"]  # 允许的请求方式
    get_protocol = ImageInfoProtocol
    view_func = {
        "get": ImageService.get_image_info,
    }


class ImageDetailController(BaseView):
    methods = ["GET"]  # 允许的请求方式
    decorators = (login_require,)
    get_protocol = ImageDetailProtocol
    view_func = {
        "get": ImageService.get_image_detail
    }


class BannerController(BaseView):
    methods = ["GET"]  # 允许的请求方式
    get_protocol = BannerProtocol
    decorators = (login_require,)
    view_func = {
        "get": ImageService.get_banner,
    }


class UserRelImageController(BaseView):
    methods = ["GET", "POST"]  # 允许的请求方式
    decorators = (login_require,)
    get_protocol = UserRelImageProtocol
    post_protocol = CollectProtocol
    view_func = {
        "get": ImageService.get_user_rel_image_info,
        "post": ImageService.collect_or_cancel
    }


class UploadImageController(BaseView):
    methods = ["POST"]  # 允许的请求方式
    decorators = (login_require,)
    post_protocol = UploadImageProtocol
    view_func = {
        "post": ImageService.upload_image,
    }


class TagsController(BaseView):
    methods = ["GET"]  # 允许的请求方式
    decorators = (login_require,)
    get_protocol = GetTagsProtocol
    view_func = {
        "get": ImageService.get_tags,
    }