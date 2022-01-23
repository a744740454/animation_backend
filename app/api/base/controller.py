from flask import views, request
from middleware.decorator import valid_token
from protocols.base_protocols.protocol import BaseForm
from common.error import ProtocolParamError, IsNotCallableObj
from common.response import response


class BaseView(views.MethodView):
    decorators = (valid_token,)
    post_protocol = None
    view_func = {
        "get": None,
        "post": None,
        "put": None,
        "delete": None
    }

    def get(self):
        print(request.args)
        get_func = self.view_func.get("get", None)
        if callable(get_func):
            status, result = get_func(request.args)
            return response(status, result)
        else:
            raise IsNotCallableObj("func is not callable")

    def post(self):
        post_protocol_obj = None
        if self.post_protocol:
            post_protocol_obj = self.post_protocol()
        if isinstance(post_protocol_obj, BaseForm):
            request_json = request.json
            post_protocol_obj.validate_for_api()
            post_func = self.view_func.get("post", None)
            if callable(post_func):
                status, result = post_func(request_json)
                return response(status, result)
            else:
                raise IsNotCallableObj("func is not callable")
        else:
            raise ProtocolParamError("please sure protocol param is true")

    def put(self):
        pass

    def delete(self):
        pass
