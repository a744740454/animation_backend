from app.api.base.controller import BaseView
from app.api.user.service import RegisterService
from common.response import response
from protocols.image_protocol.protocol import ImageDetailProtocol
from models.image.service import ImageService

class ImageController(BaseView):
    methods = ["GET"]  # 允许的请求方式

    @classmethod
    def get(cls):
        return "hello"


class ImageDetailController(BaseView):
    methods = ["GET"]  # 允许的请求方式
    protocol = ImageDetailProtocol
    view_func = {
        "get":ImageService
    }


    @classmethod
    def register(cls):

        reg_protocol.validate_for_api()
        status, result = RegisterService.register(request_json)
        return response(status, result)
