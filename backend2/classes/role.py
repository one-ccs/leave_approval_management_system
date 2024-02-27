#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..classes import User


class Role(User):
    def __init__(self, name, password, rid, role):
        super().__init__(name, password)
        self.__rid = rid
        self.__role = role

    @property
    def rid(self):
        return self.__rid

    @rid.setter
    def rid(self, rid):
        if not isinstance(rid, int) or rid < 0:
            raise TypeError('类型错误: rid 必须为自然数.')
        self.__rid = rid
        return self

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        if role not in ('学生', '辅导员', '教务处', '考勤人员', '管理员'):
            raise TypeError('类型错误: role 必须为 [学生|辅导员|教务处|考勤人员|管理员].')
        self.__role = role
        return self
