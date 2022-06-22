import os
import yaml

project_name = 'stp_atp_api'

BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
CONFIG_PATH = os.path.join(BASE_PATH, "config")
LOG_PATH = os.path.join(BASE_PATH, "logs")

TEMPLATE_PATH = os.path.join(BASE_PATH, "templates")

EXPORT_REPORTS_DIR_NAME = "export_reports"
EXPORT_REPORTS_PATH = os.path.join(BASE_PATH, EXPORT_REPORTS_DIR_NAME)


def get_config():
    """获取配置文件"""
    AIO_SERVER_ENV = os.environ.get('ATP_env', 'dev')
    env_path_dict = {
        'dev': {
            'config_path': os.path.join(CONFIG_PATH, 'dev.yml'),
        },
        'prod': {
            'config_path': os.path.join(CONFIG_PATH, 'prod.yml'),
        },
    }

    env_obj = env_path_dict[AIO_SERVER_ENV]
    config_path = env_obj.get('config_path')
    with open(config_path, "r") as fr:
        conf_dict = yaml.load(fr.read(), Loader=yaml.SafeLoader)
    print("parse evn: {}, config: {}".format(AIO_SERVER_ENV, conf_dict))
    return conf_dict


def dirs_check():
    if not os.path.isdir(LOG_PATH):
        os.mkdir(LOG_PATH)
    if not os.path.isdir(TEMPLATE_PATH):
        os.mkdir(TEMPLATE_PATH)
    if not os.path.isdir(EXPORT_REPORTS_PATH):
        os.mkdir(EXPORT_REPORTS_PATH)


dirs_check()
