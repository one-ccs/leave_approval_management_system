#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, url_for, redirect
from .config import FlaskConfig, FlaskSQLAlchemyConfig, AppConfig
from .utils import Result, _Flask


app = _Flask(__name__)

app.url_map.strict_slashes = False
app.config.from_object(FlaskConfig)
app.config.from_object(FlaskSQLAlchemyConfig)


@app.after_request
def cors(response):
    # 前端设置 XMLHttpRequest.withCredentials = true
    # 后端设置 request.headers['Access-Control-Allow-Credentials'] = 'true'
    # 设置允许携带 cookie, 否则登录后 flask.session 无法无法设置 cookie,
    # 且服务器的 Access-Control-Allow-Origin 不能设置为 '*', 需要设置白名单进行过滤
    response.headers['Access-Control-Allow-Origin'] = ''
    # 获取 'Origin' 时应使用 get 方法并设置默认值，避免出现 KeyError: 'HTTP_ORIGIN' 错误
    if request.headers.get('Origin', '') in AppConfig.ORIGIN_WHITE:
        response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with, content-type'
    response.headers['Access-Control-Allow-Credentials'] = 'true'

    return response

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route('/api')
def api():
    return Result.success('ok', True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
