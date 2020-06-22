# -*- coding: utf-8 -*-
# time: 2020/6/18 下午4:43
from app.models.eggs import MembershipCard
from flask import g


def get_membership_list():
    """
    获取用户购买的卡券列表
    """
    user = g.egg_user
    open_id = user.open_id
    cards = MembershipCard.query.filter_by(open_id=open_id).all()
    return list(map(lambda m: m.dict_data, cards))
