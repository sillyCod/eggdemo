# -*- coding:utf-8 -*-

"""
@file: eggs
@time: 2020/6/17 0:16
"""
from lin.db import db
from sqlalchemy.sql import func, text
from datetime import datetime
from enum import Enum


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
    class PaymentStatus(Enum):
        success = 0  # 已支付
        failed = 1  # 支付失败
        nonpay = 2  # 未支付

    class PaymentWay(Enum):
        card = 0
        wechat = 1

    id = db.Column(db.BigInteger, primary_key=True, auto_increment=True)
    user_id = db.Column(db.Integer, db.ForeignKey("egg_user.id"))
    sku_id = db.Column(db.Integer, db.ForeignKey("sku.id"))
    count = db.Column(db.Integer)
    address_id = db.Column(db.Integer, db.ForeignKey("address.id"))
    payment_way = db.Column(db.Integer, nullable=False)  # 卡包或者单独购买
    price = db.Column(db.Integer, nullable=False)
    delivery_time = db.Column(db.DateTime)  # 预计送达时间
    payment_status = db.Column(db.Integer, nullable=False, default=PaymentStatus.nonpay.value, comment="支付状态")

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())


class Sku(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(64), nullable=False, comment="商品名称")

    image = db.Column(db.String(256), comment="商品示例图")
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
    egg_exchange = db.Column(db.Integer, nullable=False, comment="已消费鸡蛋次数")
    total_count = db.Column(db.Integer, nullable=False, comment="可消费鸡蛋总次数")
    chicken_count = db.Column(db.Integer, nullable=False, comment="可消费鸡肉次数")
    chicken_exchange = db.Column(db.Integer, nullable=False, comment="鸡肉消费次数")
    activate_expire_time = db.Column(db.DateTime)
    expired_time = db.Column(db.DateTime)
    is_activated = db.Column(db.Boolean, nullable=False)

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())

    @property
    def dict_data(self):
        return {
            "open_id": self.open_id,
            "egg_exchange": self.egg_exchange,
            "total_count": self.total_count,

        }

    @property
    def chicken_available(self):
        """
        条件判定的逻辑： 鸡蛋已消费，卡仍未过期，鸡肉未消费
        """
        return self.egg_exchange == self.total_count and datetime.now() < self.expired_time and self.chicken_count > (
                    self.chicken_exchange or 0)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("egg_user.id"), comment="用户id")
    user_name = db.Column(db.String(64), nullable=False, comment="收货人姓名")
    phone = db.Column(db.String(32), nullable=False, comment="收货人电话")
    province = db.Column(db.String(32), nullable=False, default="河北省", comment="省份")
    city = db.Column(db.String(32), nullable=False, default="秦皇岛市", comment="城市")
    district = db.Column(db.String(32), nullable=False, comment="区县")

    detail = db.Column(db.String(256), comment="详情")

    utime = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    ctime = db.Column(db.DateTime, server_default=func.now())

    @property
    def dict_data(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "phone": self.phone,
            # "province": self.province,
            "city": self.city,
            "district": self.district,
            "detail": self.detail
        }
