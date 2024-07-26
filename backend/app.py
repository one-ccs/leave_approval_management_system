#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, redirect, render_template
from .config import MAIN_KEY, AppConfig
from .utils import _Flask, Result


app = _Flask(__name__, template_folder=AppConfig.TEMPLATE_FOLDER, static_folder=AppConfig.STATIC_FOLDER)
allow_origin_list = set([
    'http://127.0.0.1:5001',
])


@app.after_request
def cors(response):
    """允许所有域访问，并在检测到不在白名单的域访问时，返回不允许的提示"""
    origin = request.headers.get('Origin', None)

    # 忽略 options、/api、/api/file/* 请求
    if request.method == 'OPTIONS' or request.path == '/api' or '/api/file/' in request.path:
        return response

    # 在白名单
    if origin in allow_origin_list or origin == None:
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

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def SFA(path):
    return render_template('/index.html')
