from wtforms import StringField
from wtforms.validators import DataRequired, length
from protocols.base_protocols.protocol import BaseForm, BaseQueryProtocol


class ImageDetailProtocol(BaseForm):
    id = StringField(validators=[DataRequired(message='不允许为空')])


class BannerProtocol(BaseQueryProtocol):
    pass


class ImageInfoProtocol(BaseQueryProtocol):
    pass
