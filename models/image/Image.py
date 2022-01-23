from models.base.base import Base
from sqlalchemy import Column, String, Integer, Text


class ImageInfo(Base):
    __tablename__ = 'image_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_id = Column(String(100))
    image_desc = Column(Text())
    url = Column(String(100))
    author = Column(String(30))
    author_desc = Column(Text())
