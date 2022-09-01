from wtforms import StringField,FieldList
from wtforms.validators import DataRequired
from protocols.base_protocols.protocol import BaseForm, BaseQueryProtocol


class ImageDetailProtocol(BaseForm):
    image_id = StringField(validators=[DataRequired(message='不允许为空')])


class BannerProtocol(BaseQueryProtocol):
    pass


class ImageInfoProtocol(BaseQueryProtocol):
    pass


class CollectProtocol(BaseForm):
    id = StringField(validators=[DataRequired(message='不允许为空')])


class UserRelImageProtocol(BaseQueryProtocol):
    pass


class UploadImageProtocol(BaseQueryProtocol):
    title = StringField()
    desc = StringField()
    author_name = StringField()
    tags = StringField()
