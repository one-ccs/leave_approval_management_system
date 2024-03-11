#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask.json.provider import DefaultJSONProvider


class MyJSONProvider(DefaultJSONProvider):
    """重载 flask (version >= 2.2) DefaultJSONProvider 的 default 方法, 使之支持自定义对象序的列化
    需要配置 need_default, 且对象上应存在 vars 方法用于序列化
    注意: 务必在不会引起循环引用的地方调用 set_need_default 方法设置 need_default
    """
    __need_default = None

    @staticmethod
    def get_need_default():
        return MyJSONProvider.__need_default

    @staticmethod
    def set_need_default(*args):
        MyJSONProvider.__need_default = tuple(args)

    @staticmethod
    def _default(obj):
        """无法序列化的对象会自动调用该函数"""
        if isinstance(obj, MyJSONProvider.__need_default):
            return obj.vars() if obj.vars else '无法序列化, 对象上缺少 vars 方法'

    # 设置 default (实践直接定义 default 方法无效)
    default = _default


class _Flask(Flask):
    """设置 Flask 的 json_provider_class (实践使用 app.json_provider_class 设置无效)"""
    json_provider_class = MyJSONProvider
