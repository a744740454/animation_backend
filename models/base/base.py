from sqlalchemy.ext.declarative import declarative_base
import time
from sqlalchemy import Column, Integer

Base = declarative_base()


class BaseModel:
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(Integer, default=int(time.time()))
    modify_time = Column(Integer)
