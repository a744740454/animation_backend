from models.base.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, Text, UniqueConstraint


class Tag(Base, BaseModel):
    __tablename__ = 'tag'
    # __table_args__ = (UniqueConstraint('image_name', 'author', name='_image_author_uc'),)

    name = Column(String(64), doc="标签名称")
