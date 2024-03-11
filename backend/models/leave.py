#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..app import db
from ..utils import ObjectUtils


class Leave(db.Model):
    """请假条表"""
    id         = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    state      = db.Column(db.SmallInteger)
    category   = db.Column(db.SmallInteger)
    apply_timestamp = db.Column(db.DateTime)
    start_timestamp = db.Column(db.DateTime)
    end_timestamp   = db.Column(db.DateTime)
    annex_url       = db.Column(db.String(255))
    leave_reason    = db.Column(db.Text)
    reject_reason   = db.Column(db.Text)
    approver1_id    = db.Column(db.Integer)
    a1_timestamp    = db.Column(db.DateTime)
    approver2_id    = db.Column(db.Integer)
    a2_timestamp    = db.Column(db.DateTime)

    def __repr__(self):
        return ObjectUtils.repr(self, ('_sa_instance_state',))

    def vars(self, ignore=None, ignore_default=('_sa_instance_state', 'id', 'user_id')):
        if ignore is None:
            ignore = ignore_default
        return ObjectUtils.vars(self, ignore)

    def withDict(self, **kw):
        return ObjectUtils.update_with_dict(self, **kw, ignore=('_sa_instance_state',), is_snake=True)
