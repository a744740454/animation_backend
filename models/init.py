from models.user.User import UserInfo
from models.image.Image import ImageInfo
from models.author.author import AuthorInfo
from models.tag.tag import Tag
from models.user_rel_image.user_rel_image import UserRelImage
from models.tag_rel_image.tag_rel_image import TagRelImage
from models.author_rel_image.author_rel_image import AuthorRelImage

def get_metadata():
    metadata = [
        UserInfo.metadata,
        ImageInfo.metadata,
        AuthorInfo.metadata,
        Tag.metadata,
        UserRelImage.metadata,
        TagRelImage.metadata,
        AuthorRelImage.metadata
    ]
    return metadata
