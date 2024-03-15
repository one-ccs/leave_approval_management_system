#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_login import current_user, login_required
from sqlalchemy import or_
from sqlalchemy.orm import load_only
from ..app import db
from ..models import User, Role, Leave
from ..views import leave_blue
from ..utils import Result, RequestUtils, ObjectUtils


# 所有请求都需要登录 且为指定角色
@leave_blue.before_request
@login_required
def authentication():
    if User(current_user.get_id()).role not in [ Role.STUDENT, Role.TEACHER]:
        return Result.forbidden()

@leave_blue.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def leave():
    # 查询
    if request.method == 'GET':
        id = RequestUtils.quick_data(request, ('id', int))
        result = Leave.query.filter(Leave.id == id).first()

        return Result.success('查询成功', result)
    # 添加
    if request.method == 'PUT':
        request_data = RequestUtils.quick_data(request)
        leave = Leave().withDict(**request_data, user_id=current_user.get_id())
        # 添加并提交事务 失败自动回滚
        db.session.add(leave)
        db.session.commit()
        if leave.id:
            return Result.success('添加成功', True)
        return Result.failure('添加失败', False)
    # 修改
    if request.method == 'POST':
        request_data = RequestUtils.quick_data(request)
        result = Leave.query.filter(Leave.id == request_data.get('id')).update(ObjectUtils.vars(request_data, ['id']))
        db.session.commit()
        if result > 0:
            return Result.success('修改成功', True)
        return Result.failure('修改失败')
    # 删除
    if request.method == 'DELETE':
        request_data = RequestUtils.quick_data(request)
        result = Leave.query.filter(Leave.id == request_data.get('id')).delete()
        db.session.commit()
        if result > 0:
            return Result.success('删除成功', True)
        return Result.failure('删除失败')

@leave_blue.route('/brief', methods=['GET'])
def leavePageBrief():
    """分页查询简要信息"""
    pageIndex, pageSize, state, category = RequestUtils \
        .quick_data(request, ('pageIndex', 1, int), ('pageSize', 10, int), ('state', int), ('category', int))
    query = Leave.query \
        .options(load_only(Leave.id, Leave.state, Leave.category, Leave.start_datetime, Leave.end_datetime)) \
        .filter(Leave.user_id == current_user.get_id(),
            or_(Leave.state == state, state == None),
            or_(Leave.category == category, category == None))
    result = query.paginate(page=pageIndex, per_page=pageSize)

    return Result.success('查询成功', { 'total': result.total, 'list': result.items })
