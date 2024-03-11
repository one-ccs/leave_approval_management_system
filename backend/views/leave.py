#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_login import current_user, login_required
from sqlalchemy import or_
from ..app import db
from ..models import User, Role, Leave
from ..views import leave_blue
from ..utils import Result, RequestUtils


# 所有请求都需要登录 且为指定角色
@leave_blue.before_request
@login_required
def authentication():
    if User(current_user.get_id()).role not in [ Role.STUDENT, Role.TEACHER]:
        return Result.forbidden()

@leave_blue.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def leave():
    if request.method == 'GET':
        pageIndex, pageSize, state, category = RequestUtils \
            .quick_data(request, ('pageIndex', 1, int), ('pageSize', 10, int), ('state', int), ('category', int))
        query = Leave.query.filter(Leave.user_id == current_user.get_id(),
                                   or_(Leave.state == state, state == None),
                                   or_(Leave.category == category, category == None))
        result = query.paginate(page=pageIndex, per_page=pageSize)

        return Result.success(data={ 'total': result.total, 'list': result.items })
    if request.method == 'PUT':
        data = RequestUtils.quick_data(request)
        leave = Leave().withDict(**data, user_id=current_user.get_id())
        # 添加并提交事务 失败自动回滚
        db.session.add(leave)
        db.session.commit()
        if leave.id:
            return Result.success('添加成功', True)
        return Result.failure('添加失败', False)
    if request.method == 'POST':
        data = RequestUtils.quick_data(request)
        Leave.query.filter_by(user_id=data.user_id)
        return Result.success()
    if request.method == 'DELETE':
        return Result.success()
    return Result.method_not_allowed()
