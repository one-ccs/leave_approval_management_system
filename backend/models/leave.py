#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..app import db
from ..utils import ObjectUtils, DateTimeUtils


class Leave(db.Model):
    """请假条表"""
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("student.id"))
    state      = db.Column(db.SmallInteger, default=0)
    category   = db.Column(db.SmallInteger)
    apply_datetime  = db.Column(db.DateTime, default=DateTimeUtils.now)
    start_datetime  = db.Column(db.DateTime)
    end_datetime    = db.Column(db.DateTime)
    duration        = db.Column(db.SmallInteger)
    leave_reason    = db.Column(db.Text)
    annex_url       = db.Column(db.String(255))
    reject_reason   = db.Column(db.Text)
    approver1_id    = db.Column(db.Integer)
    a1_datetime     = db.Column(db.DateTime)
    approver2_id    = db.Column(db.Integer)
    a2_datetime     = db.Column(db.DateTime)

    def __repr__(self):
        return ObjectUtils.repr(self, ('_sa_instance_state',))

    def vars(self, ignore=None, ignore_default=('_sa_instance_state', 'user_id')):
        if ignore is None:
            ignore = ignore_default
        return ObjectUtils.vars(self, ignore, style='camel')

    def withDict(self, **kw):
        return ObjectUtils.update_with_dict(self, **kw, ignore=('_sa_instance_state',), is_snake=True)
