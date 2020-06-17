# -*- coding:utf-8 -*-

"""
@file: eggs
@time: 2020/6/17 0:16
"""
from lin.db import db
from sqlalchemy.sql import func, text


class EggUser(db.Model):
    """
    小程序用户
    """
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    open_id = db.Column(db.Integer, unique=True)
    nike_name = db.Column(db.String)

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())


class Order(db.Model):
    """
    订单
    """
    id = db.Column(db.Long, primary_key=True, auto_increment=True)
    open_id = db.Column(db.String, nullable=False, index=True)
    sku_id = db.Column(db.Integer)
    count = db.Column(db.Integer)
    address_id = db.Column(db.Long)
    payment_way = db.Column()  # 卡包或者单独购买
    price = db.Column()
    sent_time = db.Column()  # 预计送达时间
    payment_status = db.Column()

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())


class Sku(db.Model):
    id = db.Column(db.Long, primary_key=True, auto_increment=True)
    name = db.Column(db.String(64))
    image = db.Column()
    description = db.Column(db.String(1024))

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())


class MembershipCard(db.Model):
    id = db.Column()
    open_id = db.Column()
    egg_count = db.Column()
    total_count = db.Column(db.Integer, nullable=False)
    chicken_count = db.Column(db.Integer, nullable=False)
    activate_expire_time = db.Column(db.DateTime)
    is_activated = db.Column(db.Boolean, nullable=False)

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())


class Address(db.Model):

    id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("egg_user.id"))
    user_name = db.Column(db.String)
    phone = db.Column(db.String(32), nullable=False)
    province = db.Column(db.String(32), nullable=False)
    city = db.Column(db.String(32))
    district = db.Column(db.String(32), nullable=False)

    detail = db.Column(db.String(256))

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())
