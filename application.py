from flask import Flask
from app.router import route_register
from middleware.middleware import middleware_register
from flask_cors import CORS


def create_app():
    app = Flask(__name__, static_folder='static', template_folder="templates", static_url_path="/static")
    app.config['MAX_CONTENT_LENGTH'] = 300 * 1024 * 1024
    CORS(app)  # 解决跨域问题
    route_register(app)  # 路由注册
    middleware_register(app)  # 中间件注册
    return app
