# built-in package

# project package
from models.base.base import Base, BaseModel

# third package
from sqlalchemy import Column, String


class Tag(Base, BaseModel):
    __tablename__ = 'tag'
    name = Column(String(64), doc="标签名称")
