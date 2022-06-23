from flask import Flask
from app.router import route_register
from middleware.middleware import middleware_register


def create_app():
    app = Flask(__name__,static_folder='static',template_folder="templates",static_url_path="/static")
    route_register(app)  # 路由注册
    middleware_register(app)  # 中间件注册
    return app
