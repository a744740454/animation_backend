from flask import request
from wtforms import Form, IntegerField
from common.error import ParamValidErr


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ParamValidErr(msg=self.errors)

    def to_json(self):
        return self.data

class BaseQueryProtocol(BaseForm):
    """
    查询的基础协议
    """
    page = IntegerField(default=1)
    page_size = IntegerField(default=100)
