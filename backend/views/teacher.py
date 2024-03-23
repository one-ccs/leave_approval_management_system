#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_login import login_required, current_user
from sqlalchemy import or_
from ..plugins import db
from ..views import teacher_blue
from ..models import User, Teacher
from ..utils import Result, RequestUtils


@teacher_blue.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
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

@teacher_blue.route('/pageQuery', methods=['GET'])
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
    query = User.query.filter(
        User.username.like(query),
        or_(start_datetime >= User.create_datetime, start_datetime == None),
        or_(end_datetime <= User.create_datetime, end_datetime == None),
    )
    result = query.paginate(page=page_index, per_page=page_size, error_out=False)

    return Result.success('查询成功', {
        'total': result.total,
        'list': result.items,
    })
