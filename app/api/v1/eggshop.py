# -*- coding:utf-8 -*-

"""
@file: eggshop
@time: 2020/6/17 0:48
"""
from app.libs.lin_response import Resource
from flask.blueprints import Blueprint
from flask_restful import Api
from app.libs.restful import gen_result_by_code
from app.libs.decorators import user_login_required

from app.ops.order import consume_membership

shop_bp = Blueprint("shop", __name__, url_prefix="/api/v1/shop")
shop_api = Api(shop_bp)


@shop_api.resource("/consume")
class ConsumeResource(Resource):

    method_decorators = [user_login_required, ]

    def post(self):
        status = consume_membership()
        return gen_result_by_code(status)
