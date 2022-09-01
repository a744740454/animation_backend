from models.base.base import Base, BaseModel
from sqlalchemy import Column, String


class UserInfo(Base, BaseModel):
    __tablename__ = 'user_info'

    username = Column(String(64))
    email = Column(String(32))
    telephone = Column(String(16))
    password = Column(String(32))
    avatar = Column(String(64), default="/static/avatar/default.jpg")

    def from_json(self, data):
        for column in self.__table__.columns:
            setattr(self, column.name, data.get(column.name, getattr(self, column.name)))
        return self
