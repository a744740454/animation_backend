# built-in package

# project package
from models.base.base import Base, BaseModel


# third package
from sqlalchemy import Column, String


class TagRelImage(Base, BaseModel):
    """用户收藏的图片"""
    __tablename__ = 'tag_rel_image'

    tag_id = Column(String(128), nullable=True, doc="标签id")
    image_id = Column(String(128), nullable=True, doc="插画id")
