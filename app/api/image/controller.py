from app.api.base.controller import BaseView
from protocols.image_protocol.protocol import ImageDetailProtocol, ImageInfoProtocol, BannerProtocol,LoveProtocol
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
    methods = ["POST"]  # 允许的请求方式
    get_protocol = ImageDetailProtocol
    view_func = {
        "post": ImageService.get_image_info
    }


class BannerController(BaseView):
    methods = ["GET"]  # 允许的请求方式
    get_protocol = BannerProtocol
    view_func = {
        "get": ImageService.get_banner,
    }

class UserRelImageController(BaseView):
    decorators = (login_require,)
    methods = ["POST"]  # 允许的请求方式
    post_protocol = LoveProtocol
    view_func = {
        "post": ImageService.collect_or_cancel
    }

