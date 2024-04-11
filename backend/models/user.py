#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from ..plugins import db
from ..utils import DateTimeUtils, ObjectUtils


class User(db.Model):
    id              = db.Column(db.Integer, primary_key=True, comment='用户 id')
    username        = db.Column(db.String(32), index=True, unique=True, nullable=False, comment='用户名')
    password_hash   = db.Column(db.String(255), nullable=False, comment='密码')
    email           = db.Column(db.String(255), comment='电子邮件')
    role            = db.Column(db.SmallInteger, default=0, comment='角色')
    avatar          = db.Column(db.String(255), comment='头像链接')
    create_datetime = db.Column(db.DateTime, default=DateTimeUtils.now, comment='创建时间')

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
            self.email = user.email
            self.role = user.role
            self.create_datetime = user.create_datetime
            self.avatar = user.avatar

    def __repr__(self):
        return ObjectUtils.repr(self, ('_sa_instance_state', 'password_hash'))

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

    def vars(self, ignore=None, ignore_default=('_sa_instance_state', 'password_hash')):
        if ignore is None:
            ignore = ignore_default
        return ObjectUtils.vars(self, ignore, style='camel')

    def withDict(self, **kw):
        return ObjectUtils.update_with_dict(self, **kw, ignore=('_sa_instance_state',), is_snake=True)
