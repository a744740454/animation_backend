import time
import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()


class BaseModel:
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(Integer, default=int(time.time()))
    modify_time = Column(Integer)

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
