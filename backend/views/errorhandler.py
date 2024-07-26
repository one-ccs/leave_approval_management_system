#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.exceptions import HTTPException, MethodNotAllowed, NotFound
from jinja2.exceptions import TemplateNotFound
from ..views import errorhandler_blue
from ..utils import Result

@errorhandler_blue.app_errorhandler(HTTPException)
def http_exception(e):
    print('未知错误:', e)
    return Result.failure('未知错误', code=e.code)

@errorhandler_blue.app_errorhandler(TemplateNotFound)
def template_not_found(e):
    print('模板未找到:', e)
    return Result.error_404('模板 404')

@errorhandler_blue.app_errorhandler(KeyError)
def key_error(e):
    print('键错误:', e)
    return Result.failure('键错误')

@errorhandler_blue.app_errorhandler(ValueError)
def value_error(e):
    print('值错误:', e)
    return Result.failure('值错误')

@errorhandler_blue.app_errorhandler(MethodNotAllowed)
def method_not_found(e):
    return Result.method_not_allowed()

@errorhandler_blue.app_errorhandler(NotFound)
def error_404(e):
    return Result.error_404()

@errorhandler_blue.app_errorhandler(500)
def error_500(e):
    return Result.failure('服务器错误', None, 500)
