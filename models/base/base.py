import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from protocols.base_protocols.protocol import BaseForm
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

    def to_json(self,objs):
        print(self.columns )

