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
        pass

    def post(self):
        if isinstance(self.post_protocol, BaseForm):
            request_json = request.json
            self.post_protocol.validate_for_api()
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
