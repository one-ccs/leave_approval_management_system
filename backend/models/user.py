#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from ..app import db
from ..utils import DateTimeUtils


class User(db.Model, UserMixin):
    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(32), index=True, unique=True, nullable=False)
    password_hash   = db.Column(db.String(255))
    role            = db.Column(db.SmallInteger)
    create_datetime = db.Column(db.DateTime, default=DateTimeUtils.str_now())
    avatar          = db.Column(db.String(255))

    def __init__(self, id=None, username=None) -> None:
        """ 若初始化时指定 id 或 username 将用数据库数据初始化 """
        user = None
        if id:
            user = User.query.get(id)
        if username:
            user = User.query.filter_by(username=username).first()
        if user:
            self.id = user.id
            self.username = user.username
            self.password_hash = user.password_hash
            self.role = user.role
            self.create_datetime = user.create_datetime
            self.avatar = user.avatar

    def __repr__(self):
        return '<models.Student {' + \
            f'id: {self.id}' + \
            f', username: {self.username}' + \
            f', role: {self.role}' + \
            f', create_datetime: {self.create_datetime}' + \
            f', avatar: {self.avatar}' + \
        '}>'

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)

    def exist(self):
        """ 返回当前对象是否存在 """
        if self.id and self.username:
            return True
        return False

    def vars(self, ignore=None, ignore_default=['_sa_instance_state', 'id', 'password_hash']):
        _dict = { ** vars(self)}

        if ignore is None:
            ignore = ignore_default
        for key in ignore:
            if key in _dict:
                del _dict[key]

        return _dict
