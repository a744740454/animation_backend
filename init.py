import os
from models import session
from models.image.Image import ImageInfo
from utils.tools import create_id

def init():
    # 判断animation_web下面有没有version文件夹
    animation_web_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "animation_web", "versions")
    if not os.path.exists(animation_web_path):
        os.mkdir(animation_web_path)

    # 数据库初始化
    os.system("alembic revision --autogenerate -m 'first makemigrate'")
    os.system("alembic upgrade head")

    # 数据库插入数据
    for i in range(1, 11):
        image_info = ImageInfo()
        image_info.id = create_id()
        image_info.image_name = "{}.jpg".format(i)
        image_info.original_url = "/static/{}.jpg".format(i)
        image_info.thumbnail_url = "/static/{}.jpg".format(i)
        # session.
        session.add(image_info)
    session.commit()


if __name__ == '__main__':
    init()
