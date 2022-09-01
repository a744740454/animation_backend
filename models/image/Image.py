from models.base.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, Text


class ImageInfo(Base, BaseModel):
    __tablename__ = 'image_info'
    # __table_args__ = (UniqueConstraint('image_name', 'author', name='_image_author_uc'),)

    image_name = Column(String(64), doc="图片名称")
    title = Column(String(64), doc="图片标题")
    image_desc = Column(Text(), default='', doc="图片描述")
    original_url = Column(String(255), nullable=False, doc="原生图片url")
    thumbnail_url = Column(String(255), nullable=False, doc="缩略图url")
    author_id = Column(String(64), doc="作者id")
    collect_num = Column(Integer, default=0, doc="收藏数")
    views = Column(Integer, default=0, doc="浏览量")
