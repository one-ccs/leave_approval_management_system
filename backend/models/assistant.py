#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..plugins import db
from ..utils import ObjectUtils


class Assistant(db.Model):
    """辅导员表"""
    id         = db.Column(db.Integer, primary_key=True, comment='辅导员 id')
    user_id    = db.Column(db.Integer, db.ForeignKey("user.id"), comment='用户 id')
    name       = db.Column(db.String(32), comment='姓名')
    gender     = db.Column(db.String(2), comment='性别')

    def __repr__(self):
        return ObjectUtils.repr(self, ('_sa_instance_state',))

    def vars(self, ignore=None, ignore_default=('_sa_instance_state', )):
        if ignore is None:
            ignore = ignore_default
        return ObjectUtils.vars(self, ignore, style='camel')

    def withDict(self, **kw):
        return ObjectUtils.update_with_dict(self, **kw, ignore=('_sa_instance_state',), is_snake=True)
