#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_jwt_extended import jwt_required, current_user
from sqlalchemy import func, SmallInteger
from ..plugins import db
from ..views import chart_blue
from ..models import ERole, User, Student, Leave
from ..utils import Result


# 所有请求都需要登录 且为指定角色
@chart_blue.before_request
@jwt_required()
def authentication():
    if request.method == 'OPTIONS':
        return
    # 实际请求
    role = current_user.role
    if request.path in [
        '/api/chart/leaveState',
        '/api/chart/leaveCount',
    ] and role not in [ ERole.TEACHER, ]:
        return Result.forbidden()

@chart_blue.route('/leaveState')
def leave_state():
    """查询指定辅导员所有请假类别（分组）统计"""
    teacher_id = current_user.any_user.get('id')

    rows = db.session.query(
        Leave.state,
        func.count().label('count'),
    ).join(
        User,
        Leave.user_id == User.id
    ).join(
        Student,
        User.id == Student.user_id
    ).filter(
        Student.teacher_id == teacher_id,
    ).group_by(
        Leave.state,
    ).order_by(
        Leave.state.asc(),
    ).all()

    return Result.success(data=[{ 'state': row.state, 'count': row.count } for row in rows])

@chart_blue.route('/leaveCount')
def leave_count():
    """查询指定辅导员管理的班级（分组）请假人数统计"""
    teacher_id = current_user.any_user.get('id')

    rows = db.session.query(
        func.cast(Student._class, SmallInteger).label('_class'),
        func.coalesce(func.count(), 0).label('count'),
    ).join(
        User,
        Student.user_id == User.id
    ).join(
        Leave,
        User.id == Leave.user_id
    ).filter(
        Student.teacher_id == teacher_id,
        # Leave.start_datetime <= func.now(),
        # Leave.end_datetime >= func.now(),
    ).group_by(
        Student._class,
    ).order_by(
        '_class',
    ).all()

    return Result.success(data=[{ '_class': row._class, 'count': row.count } for row in rows])

@chart_blue.route('/leaveRank')
def leave_rank():
    """查询指定辅导员管理的学生中请假次数排行"""
    teacher_id = current_user.any_user.get('id')

    rows = db.session.query(
        Leave.user_id,
        func.count().label('count'),
    ).join(
        User,
        Leave.user_id == User.id
    ).join(
        Student,
        User.id == Student.user_id
    ).filter(
        Student.teacher_id == teacher_id,
    ).group_by(
        Leave.user_id,
    ).order_by(
        db.desc('count'),
    ).all()

    return Result.success(data=[{ 'userId': row.user_id, 'count': row.count } for row in rows])
