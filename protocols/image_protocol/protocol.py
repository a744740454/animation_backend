# built-in package

# project package
from protocols.base_protocols.protocol import BaseForm, BaseQueryProtocol


# third package
from wtforms import StringField
from wtforms.validators import DataRequired


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


class UploadImageProtocol(BaseForm):
    title = StringField()
    desc = StringField()
    author_name = StringField()
    tags = StringField()


class GetTagsProtocol(BaseQueryProtocol):
    pass