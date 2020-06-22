# -*- coding: utf-8 -*-
# time: 2020/6/22 上午11:00

from flask import request
from app.libs.restful import gen_result_by_code
import app.libs.status_code as sc
from app.models.eggs import EggUser
from flask import g


def user_login_required(func):
    def wrapper(*sub, **kwargs):
        open_id = request.cookies.get("open_id")
        if not open_id:
            return sc.E_NO_OPENID
        user = EggUser.query.get(open_id=open_id)
        if not user:
            return gen_result_by_code(sc.E_USER_NOT_EXISTS)
        g.egg_user = user
        ret = func(*sub, **kwargs)
        return ret

    return wrapper
