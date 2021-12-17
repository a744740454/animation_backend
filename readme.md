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