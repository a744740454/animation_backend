项目启动
```text
python 建议版本 3.7

安装模块
1.pip install -r requirements.txt

2.项目启动
python main.py
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