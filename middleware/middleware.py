# built-in package

# project package
from common.error import ParamValidErr, APIError
from common import response, res_code

# third package
from flask.blueprints import Blueprint

middleware = Blueprint('middleware', __name__)


# def middleware_register(app):
#     app.register_blueprint(middleware)


@middleware.app_errorhandler(ParamValidErr)
def param_valid_exception(err):
    return response.response(res_code.ERR_PARAM, err.msg)


@middleware.app_errorhandler(APIError)
def param_valid_exception(err):
    return response.response(err.res_code, {})


@middleware.after_app_request
def param_valid_exception(resp):
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE'
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp

# @app.after_request
# def af_request(resp):
#     """
#     #请求钩子，在所有的请求发生后执行，加入headers。
#     :param resp:
#     :return:
#     """
#     print("我走了")
#     resp = make_response(resp)
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE'
#     resp.headers['Access-Control-Allow-Credentials'] = 'true'
#     resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
#     print(resp.headers)
#     return resp
