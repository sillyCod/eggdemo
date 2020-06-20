"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

# 安全性配置
from app.config.setting import BaseConfig


class DevelopmentSecure(BaseConfig):
    """
    开发环境安全性配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@127.0.0.1:3306/egg'

    SQLALCHEMY_ECHO = True  # 初期调试状态下需要看一下SQLAlchemy的执行

    # use os.urandom(32) to generate a random secret key
    SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'

    APP_KEY = ""
    APP_SECRET = ""


class ProductionSecure(BaseConfig):
    """
    生产环境安全性配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@127.0.0.1:3306/lin-cms'

    SQLALCHEMY_ECHO = False

    SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'
