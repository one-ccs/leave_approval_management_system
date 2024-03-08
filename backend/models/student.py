#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..app import db

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
