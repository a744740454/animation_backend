import uuid
from models.base.base import Base
from sqlalchemy import Column, String, Integer, Text,UniqueConstraint


class ImageInfo(Base):
    __tablename__ = 'image_info'
    __table_args__ = (UniqueConstraint('image_name', 'author', name='_image_author_uc'),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_name = Column(String(100),default=uuid.uuid4())
    image_desc = Column(Text(),default='')
    url = Column(String(100),nullable=False)
    author = Column(String(30),default='佚名')
    author_desc = Column(Text(),default='')
