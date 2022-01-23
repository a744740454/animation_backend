from wtforms import StringField
from wtforms.validators import DataRequired, length
from protocols.base_protocols.protocol import BaseForm


class UserInfoProtocol(BaseForm):
    username = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32)])
    password = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32)])
    email = StringField(validators=[length(max=32)])
    telephone = StringField(validators=[length(max=32)])

