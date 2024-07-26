#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import timedelta
from .utils import PathUtils


MAIN_KEY = 'f0d8f7aa144828d60106968a6067ea19dbfa0d2d2e067eda19dbfa0d2d2e235d37e5198842dca67e13a'
DB_PASS = 'LmzwTvA1p5Bds3DODi$b2bfe2b68ef2esdf9b86dd354e00d3c3c7f533ce18fe8a6f33f7c3af52396b1bb'


class AppConfig(object):
    # Upload 文件夹
    UPLOAD_FOLDER = PathUtils.abspath('./upload')
    TEMPLATE_FOLDER = f'{PathUtils.getObjectRoot("backend")}/frontend/dist'
    STATIC_FOLDER = f'{PathUtils.getObjectRoot("backend")}/frontend/dist/static'
    ALLOWED_IMAGE_EXTENSIONS = set(['jpg', 'png', 'webp', 'gif'])


class FlaskConfig(object):
    SECRET_KEY = MAIN_KEY
    # 最大请求体大小 100mb
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024


class FlaskCorsConfig(object):
    CORS_ORIGINS = '*'
    CORS_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    CORS_ALLOW_HEADERS = ['Authorization', 'Content-Type', 'X-Origin-Token']
    CORS_EXPOSE_HEADERS = []
    CORS_SUPPORTS_CREDENTIALS = False


class FlaskJWTExtendedConfig(object):
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    JWT_SECRET_KEY = MAIN_KEY
    # 访问 token 过期时间
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    # 刷新 token 过期时间
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)


class RedisConfig(object):
    HOST = '127.0.0.1'
    PORT = 6379
    DB = 0


class FlaskSQLAlchemyConfig(object):
    SQLALCHEMY_DATABASE_URI = f'mysql://root:{DB_PASS}@127.0.0.1:3306/leave_approval_management_system'
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
