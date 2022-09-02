from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import sessionmaker, scoped_session
from config import CONF


def create_db_url():
    username = CONF.get("mysql").get("user")
    password = CONF.get("mysql").get("password", "")
    db = CONF.get("mysql").get("db")
    host = CONF.get("mysql").get("host")
    port = CONF.get("mysql").get("port")
    url = make_url('mysql+pymysql://{}:{}@{}:{}/{}'.format(username, password, host, port, db))
    db_url = url.update_query_dict({
        "charset": "utf8mb4",
        "autocommit": "true"
    })
    return db_url


def create_session():
    db_url = create_db_url()
    # 初始化数据库连接:
    engine = create_engine(
        db_url,
        pool_size=30,
        max_overflow=10,
        pool_pre_ping=True,
        pool_timeout=2,
        pool_recycle=10,
    )

    # 创建DBSession类型:
    session = sessionmaker(bind=engine)
    session = scoped_session(session)
    return session
