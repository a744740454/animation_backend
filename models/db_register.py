from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import CONF


def create_db_url():
    username = CONF.get("mysql").get("user")
    password = CONF.get("mysql").get("password")
    db = CONF.get("mysql").get("db")
    host = CONF.get("mysql").get("host")
    port = CONF.get("mysql").get("port")
    db_url = '{}:{}@{}:{}/{}'.format(username, password, host, port, db)
    return db_url


def create_session():
    db_url = create_db_url()
    db_url = 'mysql+pymysql://' + db_url
    # 初始化数据库连接:
    engine = create_engine(db_url)
    # 创建DBSession类型:
    session = sessionmaker(bind=engine)
    return session
