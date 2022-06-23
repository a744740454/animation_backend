import uuid
from models.base.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, Text, UniqueConstraint


class AuthorInfo(Base, BaseModel):
    __tablename__ = 'author_info'
    # __table_args__ = (UniqueConstraint('image_name', 'author', name='_image_author_uc'),)

    author_name = Column(String(64), doc="作者名称")
