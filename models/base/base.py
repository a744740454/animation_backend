import time
import uuid
import random
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from models import session

Base = declarative_base()


def create_id():
    i = uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid1()) + str(random.random()))
    print("uuid" + str(i))
    return i


class BaseModel:
    id = Column(String(128), default=create_id(), primary_key=True)
    create_time = Column(Integer, default=int(time.time()))
    modify_time = Column(Integer)
    create_user_id = Column(String(128))

    def set_data_from_json(self, data: dict):
        # 获取类字段
        cls_param = self.__class__.__dict__

        # 反射设置属性
        for k, v in data.items():
            if k in cls_param:
                setattr(self, k, v)

    def to_json(self):
        value_json = {}
        for column in self.__table__.columns:
            value_json[column.name] = getattr(self, column.name)

        return value_json

    def save(self):
        session.commit()
