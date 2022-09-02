from flask.blueprints import Blueprint
from app.api.user.controller import LoginController, RegisterController, UserInfoController, AvatarController,AuthorController
from app.api.image.controller import ImageDetailController, BannerController, ImageController, UserRelImageController, \
    UploadImageController,TagsController

router = Blueprint('api', __name__, url_prefix='/api/v1')


def route_register(app):
    # 用户模块
    # 头像上传
    router.add_url_rule("/upload_avatar", endpoint='upload_avatar', view_func=AvatarController.as_view("upload_avatar"))
    # todo 用户信息修改
    # 登录注册
    router.add_url_rule("/login", endpoint='login', view_func=LoginController.as_view("login"))
    router.add_url_rule("/register", endpoint='register', view_func=RegisterController.as_view("register"))
    # 获取用户信息
    router.add_url_rule("/user_info", endpoint='user_info', view_func=UserInfoController.as_view("user_info"))
    # 获取用户关联的图片信息
    router.add_url_rule("/user_rel_image", endpoint='user_rel_image',
                        view_func=UserRelImageController.as_view("user_rel_image"))

    # 获取作者信息
    router.add_url_rule("/author_info", endpoint='author_info', view_func=AuthorController.as_view("author_info"))

    # 图片模块
    # 获得轮播图列表
    router.add_url_rule("/banners", endpoint='banners', view_func=BannerController.as_view("banners"))
    # 图片详情
    router.add_url_rule("/image_detail", endpoint='image_detail',
                        view_func=ImageDetailController.as_view("image_detail"))
    # 图片上传
    router.add_url_rule("/upload_image", endpoint='upload_image',
                        view_func=UploadImageController.as_view("upload_image"))
    # 首页获取图片列表
    router.add_url_rule("/images", endpoint='images', view_func=ImageController.as_view("images"))
    # 收藏或取消收藏
    router.add_url_rule("/collect_or_cancel", endpoint='collect_or_cancel',
                        view_func=UserRelImageController.as_view("collect_or_cancel"))
    # 获取标签
    router.add_url_rule("/tags", endpoint='tags',
                        view_func=TagsController.as_view("tags"))

    app.register_blueprint(router)
