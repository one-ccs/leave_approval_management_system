#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask.json.provider import DefaultJSONProvider
from datetime import datetime


class MyJSONProvider(DefaultJSONProvider):
    """重载 flask (version >= 2.2) DefaultJSONProvider 的 default 方法, 使之支持自定义对象序的列化"""

    @staticmethod
    def _default(obj):
        """无法序列化的对象会自动调用该函数"""
        if isinstance(obj, datetime):
            return obj.strftime(r'%Y-%m-%d %H:%M:%S')

        if hasattr(obj, 'vars'):
            return obj.vars()

        if hasattr(obj, '__dict__'):
            return obj.__dict__

        raise TypeError(f"对象类型 '{type(obj).__name__}' 无法解析为 JSON")

    # 设置 default (实践直接定义 default 方法无效)
    default = _default


class _Flask(Flask):
    """设置 Flask 的 json_provider_class (实践使用 app.json_provider_class 设置无效)"""
    json_provider_class = MyJSONProvider
