#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_login import login_required, current_user
from sqlalchemy import or_
from ..plugins import db
from ..views import student_blue
from ..models import User, Teacher, Student
from ..utils import Result, RequestUtils


@student_blue.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
@login_required
def root():
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'DELETE':
        pass
    return Result.failure()

@student_blue.route('/pageQuery', methods=['GET'])
def page_query():
    """分页查询"""
    page_index, page_size, query, start_datetime, end_datetime = RequestUtils.quick_data(
        request,
        ('pageIndex', int, 1),
        ('pageSize', int, 10),
        'query',
        'startDatetime',
        'endDatetime',
    )
    query = Student.query.join(
        User,
        User.id == Student.user_id,
    ).join(
        Teacher,
        Teacher.id == Student.teacher_id,
    ).filter(
        or_(
            or_(
                User.username.contains(query),
                Teacher.name.contains(query),
                Student.name.contains(query),
            ),
            query == None, query == '',
        ),
        or_(start_datetime >= User.create_datetime, start_datetime == None, start_datetime == ''),
        or_(end_datetime <= User.create_datetime, end_datetime == None, end_datetime == ''),
    ).order_by(
        Student.grade.asc(),
        Student.major.asc(),
        Student._class.asc(),
    ).add_columns(User.username, User.avatar, User.role, Teacher.name)
    result = query.paginate(page=page_index, per_page=page_size, error_out=False)

    return Result.success('查询成功', {
        'total': result.total,
        'list': [ {
            **item[0].vars(),
            'username': item[1],
            'avatar': item[2],
            'role': item[3],
            'teacherName': item[4],
        } for item in result.items ],
    })
