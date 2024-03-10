#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..app import db

class Leave(db.Model):
    """请假条表"""
    id         = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    state      = db.Column(db.String(8))
    category   = db.Column(db.String(8))
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
        return '<models.Student {' + \
            f'id: {self.id}' + \
            f', student_id: {self.student_id}' + \
            f', state: {self.state}' + \
            f', category: {self.category}' + \
            f', apply_timestamp: {self.apply_timestamp}' + \
            f', start_timestamp: {self.start_timestamp}' + \
            f', end_timestamp: {self.end_timestamp}' + \
            f', annex_url: {self.annex_url}' + \
            f', leave_reason: {self.leave_reason}' + \
            f', reject_reason: {self.reject_reason}' + \
            f', _class: {self.approver1_id}' + \
            f', a1_timestamp: {self.a1_timestamp}' + \
            f', approver2_id: {self.approver2_id}' + \
            f', a2_timestamp: {self.a2_timestamp}' + \
        '}>'

    def vars(self, ignore=None, ignore_default=['_sa_instance_state', 'id', 'student_id']):
        _dict = { ** vars(self)}

        if ignore is None:
            ignore = ignore_default
        for key in ignore:
            if key in _dict:
                del _dict[key]

        return _dict
