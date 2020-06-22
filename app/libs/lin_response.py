from flask import Response, jsonify
import logging
from flask_restful import Resource as _Resource
from flask import request
from collections import Mapping
from marshmallow import Schema
import traceback
from marshmallow.exceptions import ValidationError
from typing import Any
from json import JSONEncoder
from lin.exception import Success
from datetime import datetime
from app.libs.utils import strftime

logger = logging.getLogger("web")


class LinResponse(Response):
    # default_mimetype = 'application/json'   # 设置默认 response 类型，默认是 text/html

    @classmethod
    def force_type(cls, rv, environ=None):
        """
        只有当视图函数返回 WSGI callable 或者其它可调用对象时，才会调用 force_type
        具体参见 flask/app.py 中 make_response 源码部分
        :param rv: response value, a response object or wsgi application.
        :param environ: a WSGI environment object.
        :return: a response object.
        """
        if isinstance(rv, (dict, list, tuple, set)):
            rv = jsonify(rv)
        return super(LinResponse, cls).force_type(rv, environ)


class Resource(_Resource):
    """
    重写了flask_restful.Resource.dispatch方法，在这一层结合marshmallow做参数校验,
    可以参考method_decorators的方式来声明schema
    schema = FooSchema()
    或者
    schema = {
        "get" : FooSchema()
        "post": BarSchema()
        ...
    }
    """
    schema = None

    def dispatch_request(self, *args, **kwargs):
        meth = getattr(self, request.method.lower(), None)
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method

        if isinstance(self.schema, Mapping):
            schema = self.schema.get(request.method.lower())
        else:
            schema = self.schema

        if schema and isinstance(schema, Schema):
            try:
                _data = (request.method.lower() == "get" and request.args.to_dict()) \
                        or request.get_json(force=True, silent=True) or dict()

                data = schema.load(_data)
            except ValidationError as e:
                logger.debug(traceback.format_exc())
                # raise ParameterException(msg=e.normalized_messages())
        else:
            data = (request.method.lower() == "get" and request.args.to_dict()) \
                   or request.get_json(force=True, silent=True) or dict()
        request._data = data
        return super().dispatch_request(*args, **kwargs)

    def get_json_argument(self, key: str, default: Any = None):
        """
        :param key:
        :param default:
        :return:
        """
        if not request._data or not isinstance(request._data, dict):
            return default

        return request._data.get(key, default)


class DogonJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            return strftime(o)
        elif isinstance(o, Success):
            # 这块好像不太对
            return dict(msg=o.msg, error_code=o.error_code, code=o.code)
        else:
            return super().default(o)
