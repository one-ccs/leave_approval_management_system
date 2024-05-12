#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .user import User
from .admin import Admin
from .teacher import Teacher
from .student import Student
from .leave import Leave
from .notice import Notice
from .enum import ERole, ELeaveState, ELeaveCategory, ENoticeType
from ..utils import ObjectUtils


class MixUser(User):
    """继承 User 并挂载额外的 any_user 属性"""

    def __init__(self, user: User, any_user: dict = {}) -> None:
        ObjectUtils.update_with_dict(self, **user.vars())
        self.any_user = any_user
