# -*- coding:utf-8 -*-

"""
@file: user
@time: 2020/6/17 0:48
"""
from flask_restful import Api
from app.libs.lin_response import Resource
from flask.blueprints import Blueprint
from flask import request
from flask import make_response, jsonify

from app.ops.membership import get_membership_list
from app.ops.user import get_open_id, create_or_get_user
from app.libs.restful import gen_result_by_code
from app.ops.address import get_address_list
import app.libs.status_code as sc

user_bp = Blueprint("egg_user", __name__, url_prefix="/api/v1/user")
user_api = Api(user_bp)


@user_api.resource("/login")
class UserLogin(Resource):

    def post(self):
        jscode = self.get_json_argument("jscode")
        resp = get_open_id(jscode)
        open_id = resp.get("open_id")
        union_id = resp.get("union_id")
        if not open_id:
            return gen_result_by_code(sc.E_OPENID_FAILED)

        user = create_or_get_user(open_id, union_id)

        # response = jsonify(gen_result_by_code(sc.SUCC, data=dict(open_id=open_id), msg="成功"))
        # response.set_cookie()
        return gen_result_by_code(sc.SUCC, user.dict_data)


@user_api.resource("/user_info")
class UserResource(Resource):
    def get(self):
        pass

    def post(self):
        pass


class UserDetail(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


@user_api.resource("/address_list")
class AddressListResource(Resource):
    def get(self):
        address_list = get_address_list()
        return gen_result_by_code(sc.SUCC, address_list)


@user_api.resource("/address")
class AddressInfoResource(Resource):
    def get(self):
        data = get_address_info(address_id)
        return gen_result_by_code(sc.SUCC, data)

    def post(self):
        data = create_address_info()


@user_api.resource("/cards")
class UserMembershipCardsResource(Resource):
    def get(self):
        cards = get_membership_list()
        return gen_result_by_code(sc.SUCC, data=cards)


@user_api.resource("/card")
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
