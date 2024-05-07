#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_jwt_extended import jwt_required, current_user
from sqlalchemy import or_
from ..plugins import db
from ..views import notice_blue
from ..models import User, Admin, Teacher, Notice, ENoticeType
from ..utils import Result, RequestUtils


@notice_blue.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
@jwt_required()
def root():
    if request.method == 'GET':
        id = RequestUtils.quick_data(request, ('id', int))
        if not id:
            return Result.failure('通知 id 不能为空')

        result = Notice.query.join(
            User,
            Notice.user_id == User.id
        ).add_columns(
            User.username,
        ).filter(Notice.id == id).first()

        return Result.success('查询成功', {
            **result[0].vars(),
            'username': result[1],
        })
    if request.method == 'PUT':
        request_data = RequestUtils.quick_data(request)

        if not request_data.get('title'):
            return Result.failure('title 不能为空')
        if not request_data.get('content'):
            return Result.failure('content 不能为空')

        notice = Notice().withDict(**request_data)
        notice.user_id = current_user.id
        db.session.add(notice)
        db.session.commit()

        if not notice.id:
            return Result.failure('添加失败')
        return Result.success('添加成功', notice.vars())
    if request.method == 'POST':
        pass
    if request.method == 'DELETE':
        id = RequestUtils.quick_data(request, ('id', int))

        if not id:
            return Result.failure('通知 id 不能为空')

        result = Notice.query.filter(Notice.id == id).delete()
        db.session.commit()

        if result > 0:
            return Result.success('删除成功')
        return Result.failure('删除失败')
    return Result.failure()

@notice_blue.route('/detail', methods=['GET'])
@jwt_required()
def detail():
    """获取通知详情"""
    id = RequestUtils.quick_data(request, ('id', int))

    if not id:
        return Result.failure('通知 id 不能为空')

    result = Notice.query.join(
        User,
        Notice.user_id == User.id
    ).join(
        Teacher,
        Notice.user_id == Teacher.user_id
    ).add_columns(
        User.username,
        User.role,
        Teacher.name,
    ).filter(Notice.id == id).first()

    if not result:
        result = Notice.query.join(
            User,
            Notice.user_id == User.id
        ).join(
            Admin,
            Notice.user_id == Admin.user_id
        ).add_columns(
            User.username,
            User.role,
            Admin.name,
        ).filter(Notice.id == id).first()

    return Result.success('查询成功', {
        **result[0].vars(),
        'username': result[1],
        'role': result[2],
        'name': result[3],
    })

@notice_blue.route('/pageQuery', methods=['GET'])
@jwt_required()
def page_query():
    """分页查询"""
    page_index, page_size, query, start_datetime, end_datetime, _type, user_id = RequestUtils.quick_data(
        request,
        ('pageIndex', int, 1),
        ('pageSize', int, 10),
        'query',
        'startDatetime',
        'endDatetime',
        ('_type', int, -1),
        ('userId', int),
    )

    query_wrapper = Notice.query.join(
        User,
        Notice.user_id == User.id
    ).add_columns(
        User.username,
    )

    # 查询条件
    if query:
        query_wrapper = query_wrapper.filter(or_(
            User.username.contains(query),
            Notice.title.contains(query),
            Notice.content.contains(query),
        ))
    if start_datetime:
        query_wrapper = query_wrapper.filter(or_(start_datetime >= Notice.release_datetime))
    if end_datetime:
        query_wrapper = query_wrapper.filter(or_(end_datetime <= Notice.release_datetime))
    if _type != -1:
        query_wrapper = query_wrapper.filter(Notice._type == _type)
    if user_id != None and _type == ENoticeType.TEACHER:
        query_wrapper = query_wrapper.filter(Notice.user_id == user_id)

    result = query_wrapper.paginate(page=page_index, per_page=page_size, error_out=False)

    return Result.success('查询成功', {
        'total': result.total,
        'finished': not result.has_next,
        'list': [{
            **item[0].vars(),
            'username': item[1],
        } for item in result.items ],
    })
