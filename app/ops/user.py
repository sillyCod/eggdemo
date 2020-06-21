# -*- coding:utf-8 -*-

"""
@file: user
@time: 2020/6/20 19:04
"""
from app.config.setting import DevelopmentConfig
from app.models.eggs import EggUser
import requests


def get_open_id(jscode: str):
    app_id = DevelopmentConfig.APP_ID
    app_secret = DevelopmentConfig.APP_SECRET

    resp = requests.get(DevelopmentConfig.WECHAT_LOGIN_URL, json=dict(jscode=jscode,app_id=app_id, app_secret=app_secret), timeout=DevelopmentConfig.TIMEOUT)



def create_or_get_user(open_id: str):
    egg_user = EggUser.query.filter_by(open_id=open_id).first()
