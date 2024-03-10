#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .user import User
from .admin import Admin
from .teacher import Teacher
from .student import Student
from .leave import Leave


class Role():
    ADMIN = 9
    TEACHER = 1
    STUDENT = 0
