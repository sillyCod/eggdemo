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
    open_id = db.Column(db.String(64), unique=True, nullable=False)
    union_id = db.Column(db.String(64), nullable=False)
    nike_name = db.Column(db.String(64))

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())


class Order(db.Model):
    """
    订单
    """
    id = db.Column(db.Long, primary_key=True, auto_increment=True)
    open_id = db.Column(db.String, nullable=False, index=True)
    sku_id = db.Column(db.Integer(db.ForeignKey("sku.id")))
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
    description = db.Column(db.String(1024), comment="商品描述")
    on_sale = db.Column(db.Boolean, nullable=False, default=True, comment="是否在售")

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())

    @property
    def dict_data(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "description": self.description
        }


class MembershipCard(db.Model):
    """
    线上自购自动激活，买了送人可以再商量怎么玩
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("egg_user.id"))
    # open_id = db.Column(db.String(32), comment=)
    egg_count = db.Column(db.Integer, nullable=False, comment="剩余鸡蛋数量")
    total_count = db.Column(db.Integer, nullable=False)
    chicken_count = db.Column(db.Integer, nullable=False)
    activate_expire_time = db.Column(db.DateTime)
    is_activated = db.Column(db.Boolean, nullable=False)

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())

    @property
    def dict_data(self):
        return {
            "open_id": self.open_id,
            "egg_count": self.egg_count,
            "total_count": self.total_count,

        }


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("egg_user.id"), comment="用户id")
    user_name = db.Column(db.String(64), nullable=False, comment="收货人姓名")
    phone = db.Column(db.String(32), nullable=False, comment="收货人电话")
    province = db.Column(db.String(32), nullable=False, comment="省份")
    city = db.Column(db.String(32), nullable=False, comment="城市")
    district = db.Column(db.String(32), nullable=False, comment="区县")

    detail = db.Column(db.String(256))

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())

    @property
    def dict_data(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_name": self.user_name,
        }
