#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_jwt_extended import jwt_required, current_user
from sqlalchemy import func, distinct, SmallInteger
from ..plugins import db
from ..views import chart_blue
from ..models import ERole, ELeaveState, User, Student, Leave
from ..utils import Result, RequestUtils


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
    duration = RequestUtils.quick_data(request, ('duration', int, 90))
    assistant_id = current_user.any_user.get('id')

    query_wrapper = db.session.query(
        Leave.state,
        func.count().label('count'),
    ).join(
        User,
        Leave.user_id == User.id
    ).join(
        Student,
        User.id == Student.user_id
    ).filter(
        Student.assistant_id == assistant_id,
    ).group_by(
        Leave.state,
    ).order_by(
        Leave.state.asc(),
    )

    # 时间范围
    if duration:
        query_wrapper = query_wrapper.filter(
            func.abs(func.datediff(Leave.apply_datetime, func.now())) <= duration,
        )

    rows = query_wrapper.all()

    # 给默认值
    data = [{ 'state': i, 'count': 0 } for i in range(ELeaveState.DONE + 1)]

    # 格式化数据
    for row in rows:
        data[row.state]['count'] = row.count

    return Result.success(data=data)

@chart_blue.route('/leaveCount')
def leave_count():
    """查询指定辅导员管理的班级（分组）请假人数统计"""
    duration = RequestUtils.quick_data(request, ('duration', int, 90))
    assistant_id = current_user.any_user.get('id')

    query_wrapper = db.session.query(
        Student.id,
        Student.name,
        Student.major,
        func.cast(Student._class, SmallInteger).label('_class'),
        func.count().label('count'),
    ).join(
        User,
        Student.user_id == User.id
    ).join(
        Leave,
        User.id == Leave.user_id
    ).filter(
        Student.assistant_id == assistant_id,
    ).group_by(
        Student.id,
        Student.name,
        Student.major,
        Student._class,
    ).order_by(
        Student.id,
    )

    # 时间范围
    if duration:
        query_wrapper = query_wrapper.filter(
            func.abs(func.datediff(Leave.apply_datetime, func.now())) <= duration,
        )

    rows = query_wrapper.all()

    # 班级列表
    _class_list = db.session.query(
        distinct(Student.major).label('major'),
        Student._class,
    ).filter(
        Student.assistant_id == assistant_id,
    ).order_by(
        db.asc('major'),
        Student._class.asc(),
    ).all()

    # 给默认值
    data = {}
    for _class in _class_list:
        t_class = f'{_class.major} {_class._class}班'

        if t_class not in data:
            data[t_class] = { '_class': t_class, 'leaveCount': { 'total': 0, 'list': [] } }

    # 格式化数据
    for row in rows:
        t_class = f'{row.major} {row._class}班'

        data[t_class]['leaveCount']['total'] += row.count
        data[t_class]['leaveCount']['list'].append({
            'id': row.id,
            'name': row.name,
            'count': row.count,
        })

    return Result.success(data=[value for value in data.values()])

@chart_blue.route('/leaveRank')
def leave_rank():
    """查询指定辅导员管理的学生中请假次数排行"""
    duration = RequestUtils.quick_data(request, ('duration', int, 90))
    assistant_id = current_user.any_user.get('id')

    query_wrapper = db.session.query(
        Leave.user_id,
        Leave.category,
        func.count().label('count'),
        Student.name,
    ).join(
        User,
        Leave.user_id == User.id
    ).join(
        Student,
        User.id == Student.user_id
    ).filter(
        Student.assistant_id == assistant_id,
        Leave.state != ELeaveState.WITHDRAWN,
        Leave.state != ELeaveState.REJECTED,
    ).group_by(
        Leave.user_id,
        Leave.category,
        Student.name,
    ).order_by(
        Leave.user_id.asc(),
        Leave.category.asc(),
    )

    # 时间范围
    if duration:
        query_wrapper = query_wrapper.filter(
            func.abs(func.datediff(Leave.apply_datetime, func.now())) <= duration,
        )

    rows = query_wrapper.all()

    # 格式化返回值 (给默认值)
    data = {}
    for row in rows:
        user_id = row.user_id

        if user_id not in data:
            data[user_id] = {
                'userId': user_id,
                'name': row.name,
                'total': 0,
                'categoryCount': [0, 0, 0, 0],
            }
        data[user_id]['total'] += row.count
        data[user_id]['categoryCount'][row.category] = row.count

    return Result.success(data=sorted([value for value in data.values()], key=lambda item: item['total'], reverse=True))

@chart_blue.route('/leaving')
def leaving():
    """查询在请假期间内的学生，及请假条信息"""
    assistant_id = current_user.any_user.get('id')

    query_wrapper = Student.query.join(
        Leave,
        Student.user_id == Leave.user_id
    ).join(
        User,
        Leave.user_id == User.id
    ).add_columns(
        Leave.category,
        Leave.state,
        Leave.apply_datetime,
        Leave.start_datetime,
        Leave.end_datetime,
        Leave.duration,
        Leave.leave_reason,
        Leave.annex_url,
    ).filter(
        Student.assistant_id == assistant_id,
        Leave.start_datetime <= func.now(),
        Leave.end_datetime >= func.now(),
    )

    rows = query_wrapper.all()

    return Result.success(data=[{
        **row[0].vars(),
    } for row in rows])
