from flask.blueprints import Blueprint
from app.api.user.controller import LoginController, RegisterController

router = Blueprint('api', __name__)


def route_register(app):
    router.add_url_rule("/login", endpoint='login', view_func=LoginController.as_view("login"))
    router.add_url_rule("/register", endpoint='register', view_func=RegisterController.as_view("register"))
    app.register_blueprint(router)
