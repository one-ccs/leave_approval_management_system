#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..classes import User


class Teacher(User):
    def __init__(self, name, password, tid, gender='', telphone=''):
        super().__init__(name, password)
        self.__tid = tid
        self.gender = gender
        self.telphone = telphone

    @property
    def tid(self):
        return self.__tid

    @tid.setter
    def tid(self, tid):
        if not isinstance(tid, int) or tid < 0:
            raise TypeError('类型错误: tid 必须为自然数.')
        self.__tid = tid
        return self
