from app.api.base.controller import BaseView
from protocols.image_protocol.protocol import ImageDetailProtocol, ImageInfoProtocol
from app.api.image.service import ImageService


class ImageController(BaseView):
    methods = ["GET"]  # 允许的请求方式

    @classmethod
    def get(cls):
        return "hello"


class ImageDetailController(BaseView):
    methods = ["GET", "POST"]  # 允许的请求方式
    post_protocol = ImageInfoProtocol
    get_protocol = ImageDetailProtocol
    view_func = {
        "get": ImageService.get_image_detail,
        "post": ImageService.get_image_info
    }
