# built-in package

# project package
from models.user.User import UserInfo
from models.image.Image import ImageInfo
from models.tag.tag import Tag
from models.user_rel_image.user_rel_image import UserRelImage
from models.tag_rel_image.tag_rel_image import TagRelImage


# third package


def get_metadata():
    metadata = [
        UserInfo.metadata,
        ImageInfo.metadata,
        Tag.metadata,
        UserRelImage.metadata,
        TagRelImage.metadata,
    ]
    return metadata
