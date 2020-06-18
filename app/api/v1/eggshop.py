# -*- coding:utf-8 -*-

"""
@file: eggshop
@time: 2020/6/17 0:48
"""
from app.libs.lin_response import Resource
from flask.blueprints import Blueprint
from flask_restful import Api

shop_bp = Blueprint("shop", __name__, url_prefix="/api/v1/shop")
shop_api = Api(shop_bp)


@shop_api.resource("/card")
class MembershipResource(Resource):

    schema = None
    method_decorators = None

    def get(self):
        # get_membership_cards()
        pass

    def post(self):
        # buy_card()
        pass

    def put(self):
        pass

    def delete(self):
        pass
