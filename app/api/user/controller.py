from flask import views


class Login(views.MethodView):
    methods = ["GET"]  # 允许的请求方式

    def get(self):
        pass
