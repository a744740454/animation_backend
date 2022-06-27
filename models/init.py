from models.user.User import UserInfo
from models.image.Image import ImageInfo
from models.author.author import AuthorInfo
from models.user_rel_image.user_rel_image import UserRelImage

def get_metadata():
    metadata = [
        UserInfo.metadata,
        ImageInfo.metadata,
        AuthorInfo.metadata,
        UserRelImage.metadata
    ]
    return metadata
