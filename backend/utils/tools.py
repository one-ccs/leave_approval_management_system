#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

class DateTimeUtils:
    format = r'%Y-%m-%d %H:%M:%S'

    @staticmethod
    def set_format(format: str):
        """设置字符串日期时间的默认格式"""
        DateTimeUtils.format = format
        return DateTimeUtils

    @staticmethod
    def now():
        """返回 datetime 格式的当前时间"""
        return datetime.now()

    @staticmethod
    def str_now():
        """返回字符串格式的当前时间"""
        return datetime.now().strftime(DateTimeUtils.format)

    @staticmethod
    def diff(minuend: str, minus: str) -> timedelta:
        """返回 minuend 减去 minus 的时间差"""
        return datetime.strptime(minuend, DateTimeUtils.format) - datetime.strptime(minus, DateTimeUtils.format)

    @staticmethod
    def stime2year(stime):
        """返回字符串时间格式中的 年"""
        return datetime.strptime(stime, DateTimeUtils.format).year

    @staticmethod
    def stime2month(stime):
        """返回字符串时间格式中的 月"""
        return datetime.strptime(stime, DateTimeUtils.format).month

    @staticmethod
    def stime2day(stime):
        """返回字符串时间格式中的 日"""
        return datetime.strptime(stime, DateTimeUtils.format).day

    @staticmethod
    def stime2hour(stime):
        """返回字符串时间格式中的 时"""
        return datetime.strptime(stime, DateTimeUtils.format).hour

    @staticmethod
    def stime2minute(stime):
        """返回字符串时间格式中的 分"""
        return datetime.strptime(stime, DateTimeUtils.format).minute

    @staticmethod
    def stime2second(stime):
        """返回字符串时间格式中的 秒"""
        return datetime.strptime(stime, DateTimeUtils.format).second
