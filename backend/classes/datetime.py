#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

class Datetime:
    @staticmethod
    def diff(minuend, minus, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(minuend, format) - datetime.strptime(minus, format)
    
    @staticmethod
    def year(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).year
    
    @staticmethod
    def month(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).month
    
    @staticmethod
    def day(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).day
    
    @staticmethod
    def hour(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).hour
    
    @staticmethod
    def minute(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).minute
    
    @staticmethod
    def second(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).second
