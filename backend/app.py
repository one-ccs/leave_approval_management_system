#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, redirect
from .config import MAIN_KEY
from .utils import _Flask, Result


app = _Flask(__name__)
allow_origin_list = set([])


@app.after_request
def cors(response):
    """允许所有域访问，并在检测到不在白名单的域访问时，返回不允许的提示"""
    origin = request.headers.get('Origin', None)

    # 忽略 options、/api、/api/file/* 请求
    if request.method == 'OPTIONS' or request.path == '/api' or '/api/file/' in request.path:
        return response

    # 在白名单
    if origin in allow_origin_list:
        return response

    response.set_data(Result.with_json(Result.failure('不允许的跨域请求', None, 401.9)))

    return response

@app.route('/favicon.ico')
def favicon():
    return redirect('/api/file/favicon.ico')

@app.route('/api')
def api():
    """注册 Origin 域"""
    origin = request.headers.get('Origin', None)
    origin_token = request.headers.get('X-Origin-Token', None)

    if origin and origin_token == MAIN_KEY:
        allow_origin_list.add(origin)

        return Result.success('ok', True)
    return Result.failure('ok', False)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
