# -*- coding:utf-8 -*-

"""
@file: user
@time: 2020/6/20 19:04
"""
from app.config.setting import DevelopmentConfig
from app.models.eggs import EggUser
import requests
from lin.db import db
from sqlalchemy.exc import SQLAlchemyError


def get_open_id(jscode: str):
    app_id = DevelopmentConfig.APP_ID
    app_secret = DevelopmentConfig.APP_SECRET

    resp = requests.get(DevelopmentConfig.WECHAT_LOGIN_URL,
                        json=dict(jscode=jscode, app_id=app_id, app_secret=app_secret, grant_type=""),
                        timeout=DevelopmentConfig.TIMEOUT)

    if not resp.status_code == requests.codes.ok:
        return


def create_or_get_user(open_id: str, union_id: str):
    egg_user = EggUser.query.filter_by(open_id=open_id).first()
    if egg_user:
        return egg_user
    try:
        egg_user = EggUser(open_id=open_id, union_id=union_id)
        db.session.add(egg_user)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
    else:
        return egg_user
