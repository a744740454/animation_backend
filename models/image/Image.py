import uuid
from models.base.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, Text, UniqueConstraint


class ImageInfo(Base, BaseModel):
    __tablename__ = 'image_info'
    # __table_args__ = (UniqueConstraint('image_name', 'author', name='_image_author_uc'),)

    image_name = Column(String(64), default=uuid.uuid4(), doc="图片名称")
    image_desc = Column(Text(), default='', doc="图片描述")
    url = Column(String(255), nullable=False, doc="url")
    author_id = Column(String(64), doc="作者id")
    support_num = Column(Integer, default=0, doc="点赞数")
