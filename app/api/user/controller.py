from app.api.base.controller import BaseView


class Login(BaseView):
    methods = ["GET"]  # 允许的请求方式

    def get(self):
        pass

