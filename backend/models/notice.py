#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..plugins import db
from ..utils import ObjectUtils, DateTimeUtils


class Notice(db.Model):
    """公告表"""
    id         = db.Column(db.Integer, primary_key=True, comment='请假条 id')
    user_id    = db.Column(db.Integer, db.ForeignKey("user.id"), comment='发布者用户 id')
    title      = db.Column(db.String(30), comment='标题')
    content    = db.Column(db.String(255), comment='内容')
    status     = db.Column(db.SmallInteger, default=1, comment='状态（0 不显示、1 显示）')
    release_datetime = db.Column(db.DateTime, default=DateTimeUtils.now, comment='发布时间')

    def __repr__(self):
        return ObjectUtils.repr(self, ('_sa_instance_state',))

    def vars(self, ignore=None, ignore_default=('_sa_instance_state', )):
        if ignore is None:
            ignore = ignore_default
        return ObjectUtils.vars(self, ignore, style='camel')

    def withDict(self, **kw):
        return ObjectUtils.update_with_dict(self, **kw, ignore=('_sa_instance_state',), is_snake=True)
