#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_login import current_user, login_required
from ..app import db
from ..models import Leave
from ..views import leave_blue
from ..utils import Result, RequestUtils


@leave_blue.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def leave():
    if request.method == 'GET':
        pageIndex, pageSize, state, category = RequestUtils \
            .quick_data(request, ('pageIndex', 1, int), ('pageSize', 10, int), ('state', int), ('category', int))
        result = Leave.query \
            .filter_by(user_id=current_user.get_id()) \
            .paginate(page=pageIndex, per_page=pageSize)
        return Result.success(data={ 'total': result.total, 'list': result.items })
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        data = RequestUtils.quick_data(request)
        leave = Leave().withDict(**data, user_id=current_user.get_id())
        # 添加并提交事务 失败自动回滚
        db.session.add(leave)
        db.session.commit()
        if leave.id:
            return Result.success('添加成功', True)
        return Result.failure('添加失败', False)
    if request.method == 'DELETE':
        pass
    return Result.method_not_allowed()
