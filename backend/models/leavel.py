#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..app import db

class Leave(db.Model):
    """请假条表"""
    id         = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    state      = db.Column(db.String(8))
    category   = db.Column(db.String(8))
    apply_timestamp = db.Column(db.Datetime)
    start_timestamp = db.Column(db.Datetime)
    end_timestamp   = db.Column(db.Datetime)
    annex_url     = db.Column(db.String(255))
    leave_reason  = db.Column(db.LongText)
    reject_reason = db.Column(db.LongText)
    approver1_id  = db.Column(db.Integer)
    a1_timestamp  = db.Column(db.Datetime)
    approver2_id  = db.Column(db.Integer)
    a2_timestamp  = db.Column(db.Datetime)
