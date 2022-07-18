from flask import views, request,jsonify
from protocols.base_protocols.protocol import BaseForm
from common.error import ProtocolParamError, IsNotCallableObj
from common.response import response


class BaseView(views.MethodView):
    post_protocol = None
    get_protocol = None
    view_func = {
        "get": None,
        "post": None,
        "put": None,
        "delete": None
    }

    def valid_param(self, protocol):
        # 如果有参数，必须要有协议体
        if not protocol:
            # 判断get请求是否有对应的协议体
            return
        else:
            if callable(protocol):
                protocol_obj = protocol()  # 实例化对象
                if not isinstance(protocol_obj, BaseForm):  # 判断对象是否是协议体的对象
                    raise ProtocolParamError("please sure protocol param is true")
            else:
                raise ProtocolParamError("please sure protocol param is true")
        protocol_obj.validate_for_api()
        return protocol_obj

    def call_obj_func(self, func, request_obj):
        if callable(func):
            status, result = func(request_obj)
            return jsonify(response(status, result))
        else:
            raise IsNotCallableObj("func is not callable")

    def get(self):
        protocol_obj = self.valid_param(self.get_protocol)
        return self.call_obj_func(self.view_func.get("get"), protocol_obj)

    def post(self):
        protocol_obj = self.valid_param(self.post_protocol)
        return self.call_obj_func(self.view_func.get("post"), protocol_obj)

    def put(self):
        pass

    def delete(self):
        pass
