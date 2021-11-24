from flask.blueprints import Blueprint
from app.api.user.controller import Login


def route_register(app):
    router = Blueprint('api', __name__)
    router.add_url_rule('/', endpoint='login', view_func=Login.as_view(name='login'))
    app.register_blueprint(router)
