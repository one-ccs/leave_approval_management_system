#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union
from flask import request
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from flask_jwt_extended import get_jwt_identity, current_user
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from flasgger import swag_from
from ..plugins import db, jwt
from ..views import user_blue
from ..models import ERole, User, Admin, Teacher, Student
from ..utils import Result, RequestUtils, ObjectUtils


@jwt.user_identity_loader
def user_identity_lookup(user: User):
    return user

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return User(identity['id'])

@jwt.user_lookup_error_loader
def user_lookup_error_callback():
    return {'123'}

@user_blue.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
@jwt_required()
@swag_from('./api_docs/user/root.yml')
def root():
    if request.method == 'GET':
        id = RequestUtils.quick_data(request, ('id', int))
        user = User(id)
        # 获取详细信息
        any_user: Union[Admin, Teacher, Student] = None
        if user.role == ERole.ADMIN:
            any_user = Admin.query.filter_by(user_id=user.id).first()
        elif user.role == ERole.TEACHER:
            any_user = Teacher.query.filter_by(user_id=user.id).first()
        elif user.role == ERole.STUDENT:
            any_user = Student.query.filter_by(user_id=user.id).first()
        else:
            return Result.failure('未知角色')
        return Result.success('查询成功', { **user.vars(), **any_user.vars()})
    if request.method == 'PUT':
        pass
    if request.method == 'POST':
        request_data = RequestUtils.quick_data(request)
        result = User.query.filter(
            User.id == request_data.get('id', current_user.id),
        ).update(ObjectUtils.vars(request_data, ['id']))
        db.session.commit()
        if result > 0:
            return Result.success('修改成功')
        return Result.failure('修改失败')
    if request.method == 'DELETE':
        pass
    return Result.failure()

@user_blue.route('/pageQuery', methods=['GET'])
@jwt_required()
@swag_from('./api_docs/user/page_query.yml')
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
    query_wrapper = User.query.filter(
        User.username.like(query),
        or_(start_datetime >= User.create_datetime, start_datetime == None),
        or_(end_datetime <= User.create_datetime, end_datetime == None),
    )
    result = query_wrapper.paginate(page=page_index, per_page=page_size, error_out=False)

    return Result.success('查询成功', {
        'total': result.total,
        'list': result.items,
    })

@user_blue.route('/login', methods=['GET', 'POST'])
def login():
    """ 登录视图 """
    # 判断是否存在该用户
    if request.method == 'GET':
        username = RequestUtils.quick_data(request, 'username')
        if not username:
            return Result.failure('请输入账号')
        if User(username=username).exist():
            return Result.success('存在该用户', True)
        else:
            return Result.success('不存在该用户', False)
    # 用户登录
    if request.method == 'POST':
        username, password, remember = RequestUtils.quick_data(
            request,
            'username',
            'password',
            ('remember', bool),
        )
        if not username or not password:
            return Result.failure('请输入账号和密码')
        else:
            user = User(username=username)

            if not user.exist():
                return Result.failure('登录失败\n不存在该用户')
            if not user.check_password_hash(password):
                return Result.failure('登录失败\n密码错误')
            # 获取详细信息
            any_user: Union[Admin, Teacher, Student] = None
            if user.role == ERole.ADMIN:
                any_user = Admin.query.filter_by(user_id=user.id).first()
            elif user.role == ERole.TEACHER:
                any_user = Teacher.query.filter_by(user_id=user.id).first()
            elif user.role == ERole.STUDENT:
                any_user = Student.query.filter_by(user_id=user.id).first()
            else:
                return Result.failure('登录失败\n角色数据异常\n请联系管理员')
            # 登录用户
            access_token = create_access_token(identity=user)
            refresh_token = create_refresh_token(identity=user)
            return Result.success('登录成功', {
                **user.vars(),
                **any_user.vars(),
                'accessToken': access_token,
                'refreshToken': refresh_token,
            })
    return Result.method_not_allowed()

@user_blue.route('refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """ 使用刷新 token 获取新的访问 token """
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return Result.success(access_token)

@user_blue.route('/register', methods=['POST'])
def register():
    """ 注册视图 """
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')

        if not username or not password:
            return Result.failure('请输入账号和密码')
        else:
            try:
                user = User(username=username, password=password)
                db.session.add(user)
                db.session.commit()
            except IntegrityError:
                return Result.failure('账号已存在')
            return Result.success('注册成功')
    return Result.method_not_allowed()

@user_blue.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """ 登出视图 """
    if request.method == 'POST':
        if 1:
            return Result.success('登出成功')
        return Result.failure('登出失败')
    return Result.method_not_allowed()
