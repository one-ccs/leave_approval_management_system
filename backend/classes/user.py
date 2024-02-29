#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    """ 用户类 """
    def __init__(self, name, password):
        if not name or not password:
            raise ValueError('值错误: 用户名和密码不能为空.')
        self.__id = -1
        self.__name = str(name)
        self.__password = str(password)
        self.__hash_password = generate_password_hash(self.__password)[21:]

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            try:
                id = int(id)
            except:
                raise TypeError(f'类型错误: id 必须为自然数 (id={id}).')
        if id < 0:
            raise TypeError('类型错误: id 必须大于 0.')
        self.__id = id
        return self

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('值错误: 用户名不能为空.')
        self.__name = str(name)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not password:
            raise ValueError('值错误: 密码不能为空.')
        self.__password = str(password)
        self.__hash_password = generate_password_hash(self.__password)[21:]

    @property
    def hash_password(self):
        return self.__hash_password

    def check_password(self, pwhash):
        return check_password_hash(f'pbkdf2:sha256:260000${pwhash}', self.__password)
    