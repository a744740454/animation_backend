from flask.blueprints import Blueprint
from main import app


def route_register():
    router = Blueprint('api', __name__)
    app.register_blueprint(router)
