from flask import views
from middleware.decorator import valid_token


class BaseView(views.MethodView):
    decorators = (valid_token,)
