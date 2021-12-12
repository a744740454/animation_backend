from flask.blueprints import Blueprint
from common.error import ParamValidErr
from common import response, res_code

middleware = Blueprint('middleware', __name__)


def middleware_register(app):
    app.register_blueprint(middleware)


@middleware.app_errorhandler(ParamValidErr)
def param_valid_exception(err):
    return response.response(res_code.ERR_PARAM, err.msg)
