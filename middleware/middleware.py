# built-in package

# project package
from common.error import ParamValidErr,APIError
from common import response, res_code

# third package
from flask.blueprints import Blueprint


middleware = Blueprint('middleware', __name__)


def middleware_register(app):
    app.register_blueprint(middleware)


@middleware.app_errorhandler(ParamValidErr)
def param_valid_exception(err):
    return response.response(res_code.ERR_PARAM, err.msg)


@middleware.app_errorhandler(APIError)
def param_valid_exception(err):
    return response.response(err.res_code, {})