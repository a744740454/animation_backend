from app.api.base.controller import BaseView
from app.api.user.service import RegisterService
from common.response import response
from flask import request
from protocols.user_protocols.protocol import UserInfoProtocol


class ImageController(BaseView):
    methods = ["GET"]  # 允许的请求方式

    @classmethod
    def get(cls):
        return "hello"


class ImageDetailController(BaseView):
    methods = ["POST"]  # 允许的请求方式
    protocol = UserInfoProtocol


    @classmethod
    def register(cls):

        reg_protocol.validate_for_api()
        status, result = RegisterService.register(request_json)
        return response(status, result)
