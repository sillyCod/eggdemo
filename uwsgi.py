"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from app.app import create_app
from flask import jsonify

app = create_app(environment='development')


@app.route("/api/v1/test")
def test():
    resp = jsonify(dict(test="test"))
    resp.set_cookie("hello", "world")
    return resp


if __name__ == '__main__':
    print(app.url_map)
    app.run(host="0.0.0.0", port=9999)
