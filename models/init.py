from models.user.User import UserInfo
from models.image.Image import ImageInfo


def get_metadata():
    metadata = [
        UserInfo.metadata,
        ImageInfo.metadata
    ]
    return metadata
