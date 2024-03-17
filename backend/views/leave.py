#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_login import current_user, login_required
from sqlalchemy import or_
from sqlalchemy.orm import load_only
from ..plugins import db
from ..views import leave_blue
from ..models import ERole, ELeaveState, User, Leave
from ..utils import Result, RequestUtils, ObjectUtils, DateTimeUtils


# 所有请求都需要登录 且为指定角色
@leave_blue.before_request
@login_required
def authentication():
    role = User(current_user.get_id()).role
    if request.path in [
        '/api/leave',
        '/api/leave/brief',
    ] and role not in [ ERole.STUDENT, ERole.TEACHER]:
        return Result.forbidden()
    if request.path in [
        '/api/leave/cancel',
        '/api/leave/revoke',
    ] and role not in [ ERole.STUDENT ]:
        return Result.forbidden()
    if request.path in [
        '/api/leave/agreeLeave',
        '/api/leave/reject',
        '/api/leave/agreeRevoke',
    ] and role not in [ ERole.TEACHER ]:
        return Result.forbidden()

@leave_blue.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def leave():
    # 查询
    if request.method == 'GET':
        id = RequestUtils.quick_data(request, ('id', int))
        if not id:
            return Result.failure('请假条 id 不能为空')
        result = Leave.query.filter(Leave.id == id).first()

        return Result.success('查询成功', result)
    # 添加
    if request.method == 'PUT':
        request_data = RequestUtils.quick_data(request)
        start_datetime = request_data.get('startDatetime')
        end_datetime = request_data.get('endDatetime')
        if not start_datetime:
            return Result.failure('缺少开始时间')
        if not end_datetime:
            return Result.failure('缺少结束时间')
        duration = -1
        try:
            duration = DateTimeUtils.diff(
                end_datetime, start_datetime,
                r'%Y-%m-%d %H:%M',
            ).total_seconds()
        except:
            duration = DateTimeUtils.diff(
                end_datetime, start_datetime,
            ).total_seconds()
        if duration < 0:
            return Result.failure('错误， 请假时长为负')
        # 请假天数
        duration = int(0.5 + duration / 3600 / 24)
        leave = Leave().withDict(
            **request_data,
            user_id=current_user.get_id(),
            duration=duration,
        )
        # 添加并提交事务 失败自动回滚
        db.session.add(leave)
        db.session.commit()
        if leave.id:
            return Result.success('添加成功')
        return Result.failure('添加失败')
    # 修改
    if request.method == 'POST':
        request_data = RequestUtils.quick_data(request)
        result = Leave.query.filter(
            Leave.id == request_data.get('id')
        ).update(ObjectUtils.vars(request_data, ['id']))
        db.session.commit()
        if result > 0:
            return Result.success('修改成功')
        return Result.failure('修改失败')
    # 删除
    if request.method == 'DELETE':
        id = RequestUtils.quick_data(request, ('id', int))
        if not id:
            return Result.failure('请假条 id 不能为空')
        result = Leave.query.filter(Leave.id == id).delete()
        db.session.commit()
        if result > 0:
            return Result.success('删除成功')
        return Result.failure('删除失败')

@leave_blue.route('/brief', methods=['GET'])
def leavePageBrief():
    """分页查询简要信息"""
    pageIndex, pageSize, state, category = RequestUtils.quick_data(
        request,
        ('pageIndex', int, 1),
        ('pageSize', int, 10),
        ('state', int),
        ('category', int),
    )
    query = Leave.query \
        .options(load_only(
            Leave.id,
            Leave.state,
            Leave.category,
            Leave.start_datetime,
            Leave.end_datetime,
        )).filter(
            Leave.user_id == current_user.get_id(),
            or_(Leave.state == state, state == None),
            or_(Leave.category == category, category == None,
        ))
    result = query.paginate(page=pageIndex, per_page=pageSize)

    return Result.success('查询成功', {
        'total': result.total,
        'list': result.items
    })

@leave_blue.route('/cancel', methods=['POST'])
def leaveCancel():
    """撤销申请"""
    id = RequestUtils.quick_data(request, ('id', int))
    if not id:
        return Result.failure('请假条 id 不能为空')
    result = Leave.query.filter(
        Leave.id == id,
        Leave.state ==
        ELeaveState.PENDING
    ).update({
        'state': ELeaveState.WITHDRAWN,
    })
    db.session.commit()
    if result > 0:
        return Result.success('撤销申请成功')
    return Result.failure('撤销申请失败')

@leave_blue.route('/revoke', methods=['POST'])
def leaveRevoke():
    """申请销假"""
    id, longitude, latitude = RequestUtils.quick_data(
        request,
        'id',
        'coords.longitude',
        'coords.latitude',
    )
    if not id:
        return Result.failure('请假条 id 不能为空')
    if not longitude or not latitude:
        return Result.failure('经纬度坐标不能为空')
    result = Leave.query.filter(
        Leave.id == id,
        Leave.state == ELeaveState.CANCEL,
    ).update({
        'state': ELeaveState.CANCELING,
        'revoke_longitude': longitude,
        'revoke_latitude': latitude,
    })
    db.session.commit()
    if result > 0:
        return Result.success('申请销假成功')
    return Result.failure('申请销假失败')

@leave_blue.route('/agreeLeave', methods=['POST'])
def leaveAgreeLeave():
    """同意请假申请"""
    id = RequestUtils.quick_data(request, ('id', int))
    if not id:
        return Result.failure('请假条 id 不能为空')
    # 请假时长 < 3 天, 待销假
    result = Leave.query.filter(
        Leave.id == id,
        Leave.state == ELeaveState.PENDING,
        Leave.duration < 3,
    ).update({
        'state': ELeaveState.CANCEL,
    })
    # 请假时长 >= 3 天, 审批中
    if not result:
        result = Leave.query.filter(
            Leave.id == id,
            Leave.state == ELeaveState.PENDING
        ).update({
            'state': ELeaveState.APPROVING,
        })
    db.session.commit()
    if result > 0:
        return Result.success('同意申请成功')
    return Result.failure('同意申请失败')

@leave_blue.route('/reject', methods=['POST'])
def leaveReject():
    """驳回请假申请"""
    id = RequestUtils.quick_data(request, ('id', int))
    if not id:
        return Result.failure('请假条 id 不能为空')
    result = Leave.query.filter(
        Leave.id == id,
        Leave.state == ELeaveState.PENDING
    ).update({
        'state': ELeaveState.REJECTED,
    })
    db.session.commit()
    if result > 0:
        return Result.success('驳回申请成功')
    return Result.failure('驳回申请失败')

@leave_blue.route('/agreeRevoke', methods=['POST'])
def leaveAgreeRevoke():
    """同意销假申请"""
    id = RequestUtils.quick_data(request, ('id', int))
    if not id:
        return Result.failure('请假条 id 不能为空')
    result = Leave.query.filter(
        Leave.id == id,
        Leave.state == ELeaveState.CANCELING
    ).update({
        'state': ELeaveState.DONE,
    })
    db.session.commit()
    if result > 0:
        return Result.success('同意销假申请成功')
    return Result.failure('同意销假申请失败')
