# -*- coding:utf-8 -*-

"""
@file: user
@time: 2020/6/17 0:48
"""
from flask_restful import Resource, Api
from flask.blueprints import Blueprint
from flask import request
from app.ops.user import get_open_id, create_or_get_user

user_bp = Blueprint("egg_user", __name__, url_prefix="/api/v1/user")
user_api = Api(user_bp)


@user_api.resource("/login")
class UserLogin(Resource):

    def post(self):
        data = request.get_json(silent=True, force=True)
        jscode = data.get("jscode")
        get_open_id(jscode)

        create_or_get_user(open_id)






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