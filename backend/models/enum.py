#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ERole():
    ADMIN = 9
    TEACHER = 1
    STUDENT = 0

class ELeaveState():
    # 待审批
    PENDING = 0
    # 已撤回
    WITHDRAWN = 1
    # 审批中
    APPROVING = 2
    # 已驳回
    REJECTED = 3
    # 待销假
    CANCEL = 4
    # 销假中
    CANCELING = 5
    # 已完成
    DONE = 6

class ELeaveCategory():
    # 事假
    PERSONAL = 0
    # 病假
    SICK = 1
    # 公假
    PUBLIC = 2
    # 出校申请
    LEAVE_SCHOOL = 3

class ENoticeType():
    # 系统通知
    SYSTEM = 0
    # 学校通知
    SCHOOL = 1
    # 学院通知
    COLLEGE = 2
    # 辅导员通知
    TEACHER = 3
