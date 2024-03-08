#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime


def deepStrftime(obj):
    """ 深度遍历 dict 或 list 将 datetime 数值格式化 """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, datetime):
                obj[k] = v.strftime(r'%Y-%m-%d %H:%M:%S')
            deepStrftime(obj[k])
    if isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, datetime):
                obj[i] = v.strftime(r'%Y-%m-%d %H:%M:%S')
            deepStrftime(obj[i])
    return obj

def unify_response(code, data=None, message=''):
    """ 快速构造 Response 并将 data 中的日期格式化 """
    return ({'code': code, 'message': message, 'data': deepStrftime(data)}, 200)


class Result(object):

    @staticmethod
    def success(message='请求成功', data=None, code=200):
        return unify_response(code, data, message)

    @staticmethod
    def failure(message='请求失败', data=None, code=400):
        return unify_response(code, data, message)

    @staticmethod
    def unauthorized(message='请登录后操作'):
        return unify_response(401, None, message)

    @staticmethod
    def forbidden(message='您无权进行此操作'):
        return unify_response(403, None, message)

    @staticmethod
    def method_not_allowed(message='不允许的请求方法'):
        return unify_response(405, None, message)

    @staticmethod
    def error_404(message='什么都没有'):
        return unify_response(404, None, message)
