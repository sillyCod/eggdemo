# -*- coding:utf-8 -*-

"""
@file: eggs
@time: 2020/6/17 0:16
"""
from lin.db import db


class EggUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    open_id = db.Column(db.Integer, unique=True)
    nike_name = db.Column(db.String)

    utime = db.Column(db.DateTime)
    ctime = db.Column(db.DateTime)


class EggOrder(db.Model):
    id = db.Column(db.Long, primary_key=True, auto_increment=True)
    open_id = db.Column(db.String, nullable=False, index=True)
    sku_id = db.Column(db.Integer)
    count = db.Column(db.Integer)
    address_id = db.Column(db.Long)
    payment_way = db.Column()  # 卡包或者单独购买
    price = db.Column()
    sent_time = db.Column()  # 预计送达时间
    payment_status = db.Column()

    utime = db.Column(db.DateTime)
    ctime = db.Column(db.DateTime)


class Sku(db.Model):
    id = db.Column(db.Long, primary_key=True, auto_increment=True)
    name = db.Column(db.String)
    description = db.Column()

    utime = db.Column()
    ctime = db.Column()


class Membership(db.Model):
    id = db.Column()
    open_id = db.Column()
    egg_count = db.Column()
    total_count = db.Column()
    chicken_count = db.Column()
    activate_expire_time = db.Column()
    is_activated = db.Column()

    utime = db.Column()
    ctime = db.Column()


class Address(db.Model):

    id = db.Column(db.Integer)
    user_name = db.Column(db.String)
    phone = db.Column(db.String, nullable=False)
    province = db.Column(db.String)
    city = db.Column(db.String)
    district = db.Column(db.String)

    detail = db.Column()

    utime = db.Column()
    ctime = db.Column()
