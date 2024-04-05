#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import timedelta


MAIN_KEY = 'LmzwTvA1p5Bds3DODi$b2bfe2b68ef2esdf9b86dd354e00d3c3c7f533ce18fe8a6f33f7c3af52396b1bb'


class AppConfig(object):
    # Origin
    ORIGIN_WHITE = ['http://127.0.0.1:5177', 'http://localhost:5177']
    # Upload
    UPLOAD_FOLDER = './upload'
    ALLOWED_IMAGE_EXTENSIONS = set(['jpg', 'png', 'webp', 'gif'])


class FlaskConfig(object):
    SECRET_KEY = MAIN_KEY
    # 禁止 js 读取 Cookie
    SESSION_COOKIE_HTTPONLY = True
    # Cookie 有效期 24h
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=3600 * 24)
    # 最大请求体大小 100mb
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024
    # 从最近某个日期开始 必须设置 samesite='None' 和 secure=True 浏览器才会跨域发送 cookie
    SESSION_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SECURE = True


class FlaskSQLAlchemyConfig(object):
    SQLALCHEMY_DATABASE_URI = f'mysql://root:{MAIN_KEY}@127.0.0.1:3306/leave_approval_management_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class FlasggerConfig(object):
    SWAGGER = {
        'uiversion': 3,
        'openapi': '3.0.1',
        # 'doc_dir': './views/api_docs/',
    }
    CONFIG = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'api',
                "route": '/api.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        # "static_folder": "static",  # must be set by user
        "swagger_ui": True,
        "specs_route": "/api-docs/"
    }
    TEMPLATE = {
        "info": {
            'title': '请假审批管理系统 API',
            'version': '0.0.1',
            'description': '请假审批管理系统 API 文档',
            'termsOfService': '/api',
            "contact": {
                "responsibleOrganization": "ME",
                "responsibleDeveloper": "Me",
                "email": "me@me.com",
                "url": "www.me.com",
            },
            "termsOfService": "/api",
        },
        "host": "mysite.com",  # overrides localhost:500
        "basePath": "/api",  # base bash for blueprint registration
        "schemes": [
            "http",
            "https"
        ],
        "operationId": "getmyData"
    }
