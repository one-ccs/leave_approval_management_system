#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_jwt_extended import jwt_required
from sqlalchemy import or_
from ..plugins import db
from ..views import assistant_blue
from ..models import User, Assistant
from ..utils import Result, RequestUtils, ObjectUtils


@assistant_blue.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
@jwt_required()
def root():
    # 查询
    if request.method == 'GET':
        id = RequestUtils.quick_data(request, ('id', int))
        if not id:
            return Result.failure('辅导员 id 不能为空')
        result = Assistant.query.filter(Assistant.id == id).first()

        return Result.success('查询成功', result)
    # 添加
    if request.method == 'PUT':
        request_data = RequestUtils.quick_data(request)
        if not request_data.get('name'):
            return Result.failure('辅导员姓名不能为空')
        user = User().withDict(**request_data)
        db.session.add(user)
        if not user.id:
            return Result.failure('添加失败')
        student = Assistant().withDict(
            **request_data,
            user_id=user.id,
        )
        # 添加并提交事务 失败自动回滚
        db.session.add(student)
        db.session.commit()
        if student.id:
            return Result.success('添加成功')
        return Result.failure('添加失败')
    # 修改
    if request.method == 'POST':
        request_data = RequestUtils.quick_data(request)
        if not request_data.get('id'):
            return Result.failure('辅导员 id 不能为空')
        result = Assistant.query.filter(
            Assistant.id == request_data.get('id')
        ).update(ObjectUtils.vars(request_data, ['id', 'user_id']))
        db.session.commit()
        if result > 0:
            return Result.success('修改成功')
        return Result.failure('修改失败')
    # 删除
    if request.method == 'DELETE':
        user_id = RequestUtils.quick_data(request, ('userId', int))
        if not user_id:
            return Result.failure('辅导员 user_id 不能为空')
        result = Assistant.query.filter(Assistant.user_id == user_id).delete()
        result = User.query.filter(User.id == user_id).delete()
        db.session.commit()
        if result > 0:
            return Result.success('删除成功')
        return Result.failure('删除失败')

@assistant_blue.route('/pageQuery', methods=['GET'])
@jwt_required()
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
    query_wrapper = Assistant.query.join(
        User,
        User.id == Assistant.user_id,
    ).add_columns(
        User.username,
        User.avatar,
        User.role,
    )
    if query:
        query_wrapper = query_wrapper.filter(or_(
            User.username.contains(query),
            User.telephone.contains(query),
            Assistant.name.contains(query),
        ))
    if start_datetime:
        query_wrapper = query_wrapper.filter(or_(start_datetime >= User.create_datetime))
    if end_datetime:
        query_wrapper = query_wrapper.filter(or_(end_datetime <= User.create_datetime))
    result = query_wrapper.paginate(page=page_index, per_page=page_size, error_out=False)

    return Result.success('查询成功', {
        'total': result.total,
        'list': [ {
            **item[0].vars(),
            'username': item[1],
            'avatar': item[2],
            'role': item[3],
        } for item in result.items ],
    })
