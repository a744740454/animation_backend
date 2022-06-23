from models.user.User import UserInfo
from models.image.Image import ImageInfo
from models.author.author import AuthorInfo

def get_metadata():
    metadata = [
        UserInfo.metadata,
        ImageInfo.metadata,
        AuthorInfo.metadata
    ]
    return metadata
