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

    def __repr__(self):
        return '<models.Student {' + \
            f'id: {self.id}' + \
            f', user_id: {self.user_id}' + \
            f', teacher_id: {self.teacher_id}' + \
            f', name: {self.name}' + \
            f', gender: {self.gender}' + \
            f', department: {self.department}' + \
            f', faculty: {self.faculty}' + \
            f', major: {self.major}' + \
            f', grade: {self.grade}' + \
            f', _class: {self._class}' + \
        '}>'

    def vars(self, ignore=None, ignore_default=['_sa_instance_state', 'id', 'user_id', 'teacher_id']):
        _dict = { ** vars(self)}

        if ignore is None:
            ignore = ignore_default
        for key in ignore:
            if key in _dict:
                del _dict[key]

        return _dict
