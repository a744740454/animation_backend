from models.base.base import Base, BaseModel
from sqlalchemy import Column, String


class AuthorRelImage(Base, BaseModel):
    """用户收藏的图片"""
    __tablename__ = 'author_rel_image'

    author_id = Column(String(128), nullable=True, doc="作者id")
    image_id = Column(String(128), nullable=True, doc="图片id")
