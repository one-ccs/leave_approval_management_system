#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..app import db
from ..utils import ObjectUtils


class Teacher(db.Model):
    """教师表"""
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("user.id"))
    name       = db.Column(db.String(32))
    gender     = db.Column(db.String(2))
    telephone  = db.Column(db.String(11))

    def __repr__(self):
        return ObjectUtils.repr(self, ('_sa_instance_state',))

    def vars(self, ignore=None, ignore_default=('_sa_instance_state', 'id', 'user_id')):
        if ignore is None:
            ignore = ignore_default
        return ObjectUtils.vars(self, ignore)

    def withDict(self, **kw):
        return ObjectUtils.update_with_dict(self, **kw, ignore=('_sa_instance_state',), is_snake=True)
