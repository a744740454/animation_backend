from models.base.base import Base
from sqlalchemy import Column, String,Integer


class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    email = Column(String(20))
    telephone = Column(String(20))
    password = Column(String(30))
