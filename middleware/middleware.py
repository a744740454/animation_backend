from flask.wrappers import Response
from flask.blueprints import Blueprint
from common.error import ParamValidErr
from common import response, res_code

middleware = Blueprint('middleware', __name__)


def middleware_register(app):
    app.register_blueprint(middleware)


@middleware.app_errorhandler(ParamValidErr)
def param_valid_exception(err):
    print(err.msg)
    return response.response(res_code.ERR_PARAM, err.msg)


@middleware.after_app_request
def cors_handler(response: Response):
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,XFILENAME,XFILECATEGORY,XFILESIZE"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
