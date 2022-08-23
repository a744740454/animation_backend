from redis import Redis
from config import CONF


class MyRedis():
    def __init__(self, db=0, host=CONF["redis"]["host"], port=CONF["redis"]["port"],
                 password=CONF["redis"]["password"]):
        self.redis = Redis(host=host, port=port, password=password, db=db)

    def set(self, key, value, ex):
        self.redis.set(name=key, value=value, ex=ex)

    def get(self, key):
        return self.redis.get(key)
