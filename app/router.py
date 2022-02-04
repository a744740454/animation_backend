from flask.blueprints import Blueprint
from app.api.user.controller import LoginController, RegisterController
from app.api.image.controller import ImageDetailController


router = Blueprint('api', __name__, url_prefix='/api/v1')


def route_register(app):
    router.add_url_rule("/login", endpoint='login', view_func=LoginController.as_view("login"))
    router.add_url_rule("/register", endpoint='register', view_func=RegisterController.as_view("register"))
    router.add_url_rule("/image_detail", endpoint='image_detail', view_func=ImageDetailController.as_view("image_detail"))
    app.register_blueprint(router)
