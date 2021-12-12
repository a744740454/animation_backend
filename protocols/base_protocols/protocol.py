from flask import request
from wtforms import Form

from common.error import ParamValidErr


# Json 基础验证器
class BaseForm(Form):
    # 接收Json参数
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    # 对验证错误的参数抛出异常
    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ParamValidErr(msg=self.errors)
        return self