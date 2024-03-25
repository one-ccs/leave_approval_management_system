#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import timedelta


MAIN_KEY = 'LmzwTvA1p5Bds3DODi$b2bfe2b68ef2esdf9b86dd354e00d3c3c7f533ce18fe8a6f33f7c3af52396b1bb'


class FlaskConfig(object):
    SECRET_KEY = MAIN_KEY
    # 禁止 js 读取 Cookie
    SESSION_COOKIE_HTTPONLY = True
    # Cookie 有效期 24h
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=3600 * 24)
    # 最大请求体大小 100mb
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024


class FlaskSQLAlchemyConfig(object):
    SQLALCHEMY_DATABASE_URI = f'mysql://root:{MAIN_KEY}@127.0.0.1:3306/leave_approval_management_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class AppConfig(object):
    # Origin
    ORIGIN_WHITE = ['http://127.0.0.1:5177', 'http://localhost:5177']
    # Upload
    UPLOAD_FOLDER = './upload'
    ALLOWED_IMAGE_EXTENSIONS = set(['jpg', 'png', 'webp', 'gif'])
