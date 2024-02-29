#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.exceptions import HTTPException
from jinja2.exceptions import TemplateNotFound
from ..views import errorhandle_blue

@errorhandle_blue.errorhandler(HTTPException)
def error_404(e):
    print('http 错误')
    return '捕获错误',201

@errorhandle_blue.errorhandler(TemplateNotFound)
def error_404(e):
    print('TemplateNotFound 错误')
    return '捕获错误',201

@errorhandle_blue.errorhandler(ValueError)
def error_404(e):
    print('值错误')
    return '捕获错误',201

@errorhandle_blue.errorhandler(404)
def error_404(e):
    print('404')
    return '捕获错误',201

@errorhandle_blue.errorhandler(500)
def error_404(e):
    print('500 错误')
    return '捕获错误',201
