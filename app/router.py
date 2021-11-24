from flask.blueprints import Blueprint
from app.api.user.controller import Login

router = Blueprint('api', __name__)


def route_register(app):
    router.add_url_rule("/", endpoint='index', view_func=Login.as_view("index"))
    app.register_blueprint(router)
