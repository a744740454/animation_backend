from models.base.base import Base,BaseModel
from sqlalchemy import Column, String,Integer


class UserInfo(Base,BaseModel):
    __tablename__ = 'user_info'

    username = Column(String(64))
    email = Column(String(32))
    telephone = Column(String(16))
    password = Column(String(32))

    def from_json(self, data):
        print(self.__tablename__)
        for column in self.__table__.columns:
            setattr(self, column.name, data.get(column.name, getattr(self, column.name)))
        return self