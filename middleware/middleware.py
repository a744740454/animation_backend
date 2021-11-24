from flask.blueprints import Blueprint

middleware = Blueprint('middleware', __name__)


def middleware_register(app):
    app.register_blueprint(middleware)
