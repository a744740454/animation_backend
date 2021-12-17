from models.db_register import create_session


def model_wrapper(func):
    def inner(*args, **kwargs):
        """开启数据库连接"""
        session = create_session()
        with session.begin() as session:
            result = func(*args, session=session, **kwargs)
        return result

    return inner
