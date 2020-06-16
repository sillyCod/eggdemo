# -*- coding: utf-8 -*-
# time: 2019/4/22 下午4:33
from typing import Union

from flask import g
from flask import jsonify

from app.libs.status_code import status_codes


def json_response(code: int, data: Union[str, list, dict] = None, msg: str = ""):
    if code not in status_codes:
        raise KeyError("{}未声明".format(code))
    lan = g.get('lan', "zh")

    if data and not isinstance(data, (str, list, dict)):
        raise Exception("非法的json格式")
    result = dict(code=code, msg=str(msg) or status_codes[code][1][lan], data=data)
    return jsonify(result)


def error_response(code: int, msg: str = None):
    """
    出错时的响应
    :param code:
    :param msg:
    :return:
    """
    if msg is None:
        lan = g.get('lan', "zh")
        msg = status_codes[code][1][lan]
    result = dict(code=code, msg=msg)

    return jsonify(result)


def gen_result_by_code(code: int, data: Union[str, list, dict] = None, msg: str = None):
    if not msg:
        lan = g.get('lan', "zh")
        msg = status_codes[code][1][lan]
    ret = dict(code=code, msg=msg, data=data)
    return ret


if __name__ == "__main__":
    json_response(0)
