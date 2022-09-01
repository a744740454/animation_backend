import uuid
from models.base.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, Text, UniqueConstraint


class TagRelImage(Base, BaseModel):
    """用户收藏的图片"""
    __tablename__ = 'tag_rel_image'

    tag_id = Column(String(128), nullable=True, doc="标签id")
    image_id = Column(String(128), nullable=True, doc="插画id")
