from flask.blueprints import Blueprint
from app.api.user.controller import LoginController, RegisterController
from app.api.image.controller import ImageDetailController,BannerController,ImageController,UserRelImageController


router = Blueprint('api', __name__, url_prefix='/api/v1')


def route_register(app):
    # 登录注册
    router.add_url_rule("/login", endpoint='login', view_func=LoginController.as_view("login"))
    router.add_url_rule("/register", endpoint='register', view_func=RegisterController.as_view("register"))

    # 获得轮播图列表
    router.add_url_rule("/banners", endpoint='banners', view_func=BannerController.as_view("banners"))

    # 图片详情
    router.add_url_rule("/image_detail", endpoint='image_detail', view_func=ImageDetailController.as_view("image_detail"))

    # 首页获取图片列表
    router.add_url_rule("/images", endpoint='images', view_func=ImageController.as_view("images"))

    # 收藏或取消收藏
    router.add_url_rule("/collect_or_cancel", endpoint='collect_or_cancel', view_func=UserRelImageController.as_view("collect_or_cancel"))

    app.register_blueprint(router)
