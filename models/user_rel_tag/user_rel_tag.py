import uuid
from models.base.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, Text, UniqueConstraint


class UserRelTag(Base, BaseModel):
    """用户收藏的图片"""
    __tablename__ = 'user_rel_tag'

    user_id = Column(Integer, nullable=True, doc="用户id")
    tag_id = Column(Integer, nullable=True, doc="图片id")
