#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..app import db

class Teacher(db.Model):
    """教师表"""
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("user.id"))
    name       = db.Column(db.String(32))
    gender     = db.Column(db.String(2))
    telephone  = db.Column(db.String(11))

    def __repr__(self):
        return '<models.Student {' + \
            f'id: {self.id}' + \
            f', user_id: {self.user_id}' + \
            f', name: {self.name}' + \
            f', gender: {self.gender}' + \
            f', telephone: {self.telephone}' + \
        '}>'

    def vars(self, ignore=None, ignore_default=['_sa_instance_state', 'id', 'user_id']):
        _dict = { ** vars(self)}

        if ignore is None:
            ignore = ignore_default
        for key in ignore:
            if key in _dict:
                del _dict[key]

        return _dict
