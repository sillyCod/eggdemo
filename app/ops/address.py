# -*- coding:utf-8 -*-

"""
@file: address
@time: 2020/6/21 21:53
"""
from app.models.eggs import Address
from flask import g


def get_address_list():
    user_id = g.user.id
    address_list = Address.query.filter_by(user_id=user_id).all()
    return list(map(lambda a: a.dict_data, address_list))


def get_address_info(address_id):
    address = Address.query.get(id=address_id)
    return address.dict_data
