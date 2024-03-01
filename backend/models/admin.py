#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..app import db

class Admin(db.Model):
    """管理员表"""
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("user.id"))
    name       = db.Column(db.String(32))
    gender     = db.Column(db.String(2))
