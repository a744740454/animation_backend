from models.user.User import UserInfo
from models.image.Image import ImageInfo
from models.author.author import AuthorInfo
from models.user_rel_image.user_rel_image import UserRelImage
from models.tag_rel_image.tag_rel_image import TagRelImage
from models.user_rel_tag.user_rel_tag import UserRelTag

def get_metadata():
    metadata = [
        UserInfo.metadata,
        ImageInfo.metadata,
        AuthorInfo.metadata,
        UserRelImage.metadata,
        TagRelImage.metadata,
        UserRelTag.metadata
    ]
    return metadata
