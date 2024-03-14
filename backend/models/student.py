#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..app import db
from ..utils import ObjectUtils


class Student(db.Model):
    """学生表"""
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("user.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    name       = db.Column(db.String(32))
    gender     = db.Column(db.String(2))
    department = db.Column(db.String(38))
    faculty    = db.Column(db.String(38))
    major      = db.Column(db.String(38))
    grade      = db.Column(db.String(38))
    _class     = db.Column(db.String(38))

    def __repr__(self):
        return ObjectUtils.repr(self, ('_sa_instance_state',))

    def vars(self, ignore=None, ignore_default=('_sa_instance_state', 'id', 'user_id', 'teacher_id')):
        if ignore is None:
            ignore = ignore_default
        return ObjectUtils.vars(self, ignore, style='camel')

    def withDict(self, **kw):
        return ObjectUtils.update_with_dict(self, **kw, ignore=('_sa_instance_state',), is_snake=True)
