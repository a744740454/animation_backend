from wtforms import StringField
from wtforms.validators import DataRequired, length
from protocols.base_protocols.protocol import BaseForm


class UserInfoProtocol(BaseForm):
    pass


class AuthorProtocol(BaseForm):
    author_id = StringField(validators=[DataRequired(message='不允许为空')])
