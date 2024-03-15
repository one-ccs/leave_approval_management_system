#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta
from .utils import Result, _Flask


# Origin 白名单
ORIGIN_WHITE = ['http://127.0.0.1:5177', 'http://localhost:5177']
# Origin Token
ORIGIN_TOKEN = 'f0d8f7aa1448260106968a6067ea19dbfa0d2d2e067ea19dbfa0d2d2e235d37e5198842dca67e13a'

MAIN_KEY = 'LmzwTvA1p5Bds3DODi$b2bfe2b68ef2esdf9b86dd354e00d3c3c7f533ce18fe8a6f33f7c3af52396b1bb'
DATABASE_OPTIONS = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': MAIN_KEY,
    'database': 'leave_approval_management_system',
}
TEMPLATE_FOLDER = '../frontend/templates'
STATIC_FOLDER = '../frontend/static'
UPLOAD_FOLDER = './frontend/static/user_upload'
ALLOWED_IMAGE_EXTENSIONS = set(['jpg', 'png', 'webp', 'gif'])

app = _Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)

# Flask
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = MAIN_KEY
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1800)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

## Flask-SQLalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DATABASE_OPTIONS["user"]}:{DATABASE_OPTIONS["password"]}@{DATABASE_OPTIONS["host"]}:{DATABASE_OPTIONS["port"]}/{DATABASE_OPTIONS["database"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)
db.rows2dict = (lambda rows, keys: [dict(zip(keys, row)) for row in rows])

login_manager = LoginManager(app)


@app.after_request
def cors(response):
    # 前端设置 XMLHttpRequest.withCredentials = true
    # 后端设置 request.headers['Access-Control-Allow-Credentials'] = 'true'
    # 设置允许携带 cookie, 否则登录后 flask.session 无法无法设置 cookie,
    # 且服务器的 Access-Control-Allow-Origin 不能设置为 '*', 需要设置白名单进行过滤
    response.headers['Access-Control-Allow-Origin'] = ''
    # 获取 'Origin' 时应使用 get 方法并设置默认值，避免出现 KeyError: 'HTTP_ORIGIN' 错误
    if request.headers.get('Origin', '') in ORIGIN_WHITE:
        response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
    if request.values.get('origin') and request.values.get('originToken') == ORIGIN_TOKEN:
        response.headers['Access-Control-Allow-Origin'] = request.values.get('origin', '')
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with, content-type'
    response.headers['Access-Control-Allow-Credentials'] = 'true'

    return response

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route('/api')
def api():
    return Result.success(True, 'ok')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
