#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..plugins import db
from ..utils import ObjectUtils


class Student(db.Model):
    """学生表"""
    id         = db.Column(db.Integer, primary_key=True, comment='学生 id')
    user_id    = db.Column(db.Integer, db.ForeignKey("user.id"), comment='用户 id')
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"), comment='教师 id')
    name       = db.Column(db.String(32), comment='姓名')
    gender     = db.Column(db.String(2), comment='性别')
    department = db.Column(db.String(38), comment='学部')
    faculty    = db.Column(db.String(38), comment='学系')
    major      = db.Column(db.String(38), comment='专业')
    grade      = db.Column(db.String(38), comment='年级')
    _class     = db.Column(db.String(38), comment='班级')

    def __repr__(self):
        return ObjectUtils.repr(self, ('_sa_instance_state',))

    def vars(self, ignore=None, ignore_default=('_sa_instance_state', 'id', 'user_id', 'teacher_id')):
        if ignore is None:
            ignore = ignore_default
        return ObjectUtils.vars(self, ignore, style='camel')

    def withDict(self, **kw):
        return ObjectUtils.update_with_dict(self, **kw, ignore=('_sa_instance_state',), is_snake=True)
