#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Result(object):

    @staticmethod
    def success(message='请求成功', data=None, code=200):
        return ({'code': code, 'message': message, 'data': data}, 200)

    @staticmethod
    def failure(message='请求失败', data=None, code=400):
        return ({'code': code, 'message': message, 'data': data}, 200)

    @staticmethod
    def unauthorized(message='请登录后操作'):
        return ({'code': 401, 'message': message, 'data': None}, 200)

    @staticmethod
    def forbidden(message='您无权进行此操作'):
        return ({'code': 403, 'message': message, 'data': None}, 200)

    @staticmethod
    def error_404(message='什么都没有'):
        return ({'code': 404, 'message': message, 'data': None}, 200)

    @staticmethod
    def method_not_allowed(message='不允许的请求方法'):
        return ({'code': 405, 'message': message, 'data': None}, 200)
