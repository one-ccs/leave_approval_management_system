#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..plugins import db
from ..utils import ObjectUtils, DateTimeUtils


class Leave(db.Model):
    """请假条表"""
    id         = db.Column(db.Integer, primary_key=True, comment='请假条 id')
    user_id    = db.Column(db.Integer, db.ForeignKey("user.id"), comment='用户 id')
    state      = db.Column(db.SmallInteger, default=0, comment='请假条状态 (0 待审批|1 已撤回|2 审批中|3 已驳回|4 待销假|5 销假中|6 已完成)')
    category   = db.Column(db.SmallInteger, comment='请假条类别 (0 事假|1 病假|2 公假|3 出校申请)')
    apply_datetime   = db.Column(db.DateTime, default=DateTimeUtils.now, comment='申请时间')
    start_datetime   = db.Column(db.DateTime, comment='开始时间')
    end_datetime     = db.Column(db.DateTime, comment='结束时间')
    duration         = db.Column(db.SmallInteger, comment='持续天数')
    leave_reason     = db.Column(db.Text, comment='请假原因')
    annex_url        = db.Column(db.String(255), comment='附件链接')
    cancel_datetime  = db.Column(db.DateTime, comment='撤销申请时间')
    revoke_datetime  = db.Column(db.DateTime, comment='申请销假时间')
    revoke_longitude = db.Column(db.Float, comment='销假时经度坐标')
    revoke_latitude  = db.Column(db.Float, comment='销假时纬度坐标')
    approver1_id     = db.Column(db.Integer, comment='审批人 id')
    a1_datetime      = db.Column(db.DateTime, comment='审批时间')
    approver2_id     = db.Column(db.Integer, comment='二次审批人 id')
    a2_datetime      = db.Column(db.DateTime, comment='二次审批时间')
    reject_id        = db.Column(db.Integer, comment='驳回人 id')
    reject_datetime  = db.Column(db.DateTime, comment='驳回时间')
    reject_reason    = db.Column(db.Text, comment='驳回原因')

    def __repr__(self):
        return ObjectUtils.repr(self, ('_sa_instance_state',))

    def vars(self, ignore=None, ignore_default=('_sa_instance_state', 'user_id')):
        if ignore is None:
            ignore = ignore_default
        return ObjectUtils.vars(self, ignore, style='camel')

    def withDict(self, **kw):
        return ObjectUtils.update_with_dict(self, **kw, ignore=('_sa_instance_state',), is_snake=True)
