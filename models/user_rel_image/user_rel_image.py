# built-in package

# project package
from models.base.base import Base, BaseModel

# third package
from sqlalchemy import Column, String


class UserRelImage(Base, BaseModel):
    """用户收藏的图片"""
    __tablename__ = 'user_rel_image'

    user_id = Column(String(128), nullable=True, doc="用户id")
    image_id = Column(String(128), nullable=True, doc="图片id")
