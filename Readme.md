项目启动
```text
python 建议版本 3.7

安装模块
1.pip install -r requirements.txt

2.安装mysql 数据库版本5.7

3.数据库迁移
linux 
    --mkdir animation/versions
    alembic revision --autogenerate -m "first makemigrate"
    alembic upgrade head

4.项目启动
python main.py


```

项目接口书写
```text
写路由
1.app/router
    eg:router.add_url_rule("/login", endpoint='login', view_func=LoginController.as_view("login"))

写对应的controller
eg:
    class LoginController(BaseView):
        methods = ["POST"]  # 允许的请求方式
        post_protocol = LoginProtocol # post请求对应的请求协议，有四种协议get_protocol、post_protocol...每次请求过来会针对对应的协议进行数据校验
    
        view_func = {
            "post": LoginService.login # post请求对应的service层函数
        }

写协议
eg:
    class LoginProtocol(BaseForm):
        username = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32)])
        password = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32)])

写service层函数,采用类函数的方式
eg:
    @classmethod
    def login(cls, request_obj: LoginProtocol):
        account = request_obj.username.data
        user = UserModel.query_user_by_account(account)

        if not user:
            raise APIError(USER_NOT_FOUND)

        # 哈希密码
        password = hash_password(request_obj.password.data)

        # 校验密码是否正确
        if password != user.password:
            raise APIError(ERR_PASSWORD)

        # 签发token
        jwt = encode_jwt({
            "user_name": user.username
        }, user_id=user.id)
        return SUCCESS, {"jwt": jwt}


```

目录结构
```commandline
--animation_web
    --animation_web     alembic自动生成的目录，记录迁移文件
        --versions      迁移记录
        --env.py        alembic的主文件
    --app api目录
    --common            通用文件目录
    --config            配置目录
    --deployment        部署目录
    --middleware        中间件以及视图装饰器
    --models            数据库模板
    --protocols         前后端交互协议
    --templates         模板
    --utils             工具方法
    --alembic.ini       alembic配置文件
    --application.py    注册app对象
    --main.py           主文件
    --readme.md         
    --requirements.txt 
```

数据库迁移
```angular2
在animation_web文件夹下面需要有对应的versions文件夹
alembic revision --autogenerate -m "first makemigrate"
alembic upgrade head
#修改字段
op.alter_column('表名',  '字段名', sa.String(length=50), existing_type=mysql.VARCHAR(50))
```