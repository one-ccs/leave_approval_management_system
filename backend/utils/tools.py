#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import re


class DateTimeUtils(object):
    format = r'%Y-%m-%d %H:%M:%S'

    @staticmethod
    def set_format(format: str):
        """设置字符串日期时间的默认格式"""
        DateTimeUtils.format = format
        return DateTimeUtils

    @staticmethod
    def now() -> datetime:
        """返回 datetime 格式的当前时间"""
        return datetime.now()

    @staticmethod
    def str_now() -> str:
        """返回字符串格式的当前时间"""
        return datetime.now().strftime(DateTimeUtils.format)

    @staticmethod
    def diff(minuend: str, minus: str) -> timedelta:
        """返回 minuend 减去 minus 的时间差"""
        return datetime.strptime(minuend, DateTimeUtils.format) - datetime.strptime(minus, DateTimeUtils.format)

    @staticmethod
    def stime2year(stime: str) -> int:
        """返回字符串时间格式中的 年"""
        return datetime.strptime(stime, DateTimeUtils.format).year

    @staticmethod
    def stime2month(stime: str) -> int:
        """返回字符串时间格式中的 月"""
        return datetime.strptime(stime, DateTimeUtils.format).month

    @staticmethod
    def stime2day(stime: str) -> int:
        """返回字符串时间格式中的 日"""
        return datetime.strptime(stime, DateTimeUtils.format).day

    @staticmethod
    def stime2hour(stime: str) -> int:
        """返回字符串时间格式中的 时"""
        return datetime.strptime(stime, DateTimeUtils.format).hour

    @staticmethod
    def stime2minute(stime: str) -> int:
        """返回字符串时间格式中的 分"""
        return datetime.strptime(stime, DateTimeUtils.format).minute

    @staticmethod
    def stime2second(stime: str) -> int:
        """返回字符串时间格式中的 秒"""
        return datetime.strptime(stime, DateTimeUtils.format).second


class RequestUtils(object):

    @staticmethod
    def quick_data(request, *keys) -> tuple:
        """将 request 中的请求参数按照 values, form, json, args 的优先级解构为元组

        :param keys 字段列表
               字段列表为空时, 直接返回整个数据
               字段列表为字符串时, 直接返回获取到的值 (str)
               字段列表为长度为 2 的元组时, 索引 0 为字段名, 索引 1 为字段类型
               字段列表为长度为 3 的元组时, 索引 0 为字段名, 索引 1 为默认值, 索引 2 为字段类型
        :return 返回包含所有获取到的值的元组
        """
        data = None
        if len(request.values):
            data = request.values
        elif len(request.form):
            data = request.form
        elif len(request.args):
            data = request.args
        else:
            try:
                data = request.get_json(force=True)
            except Exception as e:
                return None
        if not keys:
            return data
        values = []
        for key in keys:
            if (isinstance(key, list) or isinstance(key, tuple)):
                if len(key) == 2:
                    values.append(data.get(key[0], None, key[1]))
                    continue
                if len(key) == 3:
                    values.append(data.get(key[0], key[1], key[2]))
                    continue
                continue
            values.append(data.get(key))

        return tuple(values)


class ObjectUtils(object):

    @staticmethod
    def json_str(obj: object, ignore=[]):
        """将对象转为 JSON 字符串"""
        pass

    @staticmethod
    def repr(obj: object, ignore=[]) -> str:
        """将对象转为描述属性的字符串
        :param obj 对象
        :param ignore (可选) 忽略属性列表
        :return 对象详情字符串
        """
        class_name = obj.__class__.__name__
        attributes = [f'{k}={v}' for k, v in obj.__dict__.items() if k not in ignore]
        attributes_str = ', '.join(attributes)
        return f'{class_name}{{{attributes_str}}}'

    @staticmethod
    def vars(obj: object, ignore=[]) -> dict:
        """将对象的属性转为字典形式
        :param obj 对象
        :param ignore (可选) 忽略属性列表
        :return 对象 { 属性: 值 } 组成的字典
        """
        return {k: v for k, v in obj.__dict__.items() if k not in ignore}

    @staticmethod
    def update_with_dict(obj:object, **kw) -> object:
        """用关键字参数将对象赋值, 并忽略对象上不存在的属性
        :param obj 对象
        :param **kw 关键字参数
        :param ignore (可选) 忽略属性列表
        :param is_snake (可选) 是否将驼峰转为下划线形式
        :return 更新数据后的对象
        """
        is_snake = kw.get('is_snake', False)
        ignore = kw.get('ignore', [])
        for k, v in kw.items():
            if is_snake:
                k = StringUtils.camel_to_snake(k)
            if hasattr(obj, k) and k not in ignore:
                setattr(obj, k, v)
        return obj


class StringUtils(object):

    @staticmethod
    def camel_to_snake(camel_str: str) -> str:
        """将驼峰命名的字符串转换为下划线形式"""
        pattern = re.compile(r'(?<!^)(?=[A-Z])')
        return pattern.sub('_', camel_str).lower()
