#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from ..app import db


class User(db.Model, UserMixin):
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(32), index=True, unique=True, nullable=False)
    password_hash   = db.Column(db.String(255))
    token           = db.Column(db.String(255))
    create_datetime = db.Column(db.Date, default=datetime.now().strftime(r'%Y-%m-%d %H:%M:%S'))

    def __init__(self, id=None, name=None) -> None:
        """ 若初始化时指定 id 或 name 将用数据库数据初始化 """
        user = None
        if id:
            user = User.query.get(id)
        if name:
            user = User.query.filter_by(name=name).first()
        if user:
            self.id = user.id
            self.name = user.name
            self.password_hash = user.password_hash
            self.token = user.token
            self.create_datetime = user.create_datetime

    def __repr__(self):
        return f'<models.User {self.name}>'

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
        if self.id and self.name:
            return True
        return False

    def value_of(self):
        return {**{'id': self.id, 'name': self.name, 'createDatetime': self.create_datetime}}
