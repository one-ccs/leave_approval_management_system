#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.exceptions import HTTPException, MethodNotAllowed, NotFound
from jinja2.exceptions import TemplateNotFound
from ..views import errorhandler_blue
from ..utils import Result

@errorhandler_blue.app_errorhandler(HTTPException)
def error_1(e):
    print(e)
    return Result.failure('未知错误', code=e.code)

@errorhandler_blue.app_errorhandler(TemplateNotFound)
def error_2(e):
    return Result.error_404('模板 404')

@errorhandler_blue.app_errorhandler(ValueError)
def error_3(e):
    print(e)
    return Result.failure('值错误')

@errorhandler_blue.app_errorhandler(MethodNotAllowed)
def error_3(e):
    return Result.method_not_allowed()

@errorhandler_blue.app_errorhandler(NotFound)
def error_404(e):
    return Result.error_404()

@errorhandler_blue.app_errorhandler(500)
def error_500(e):
    return Result.failure('服务器错误', None, 500)
