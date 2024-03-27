#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union
from flask import request
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from flasgger import swag_from
from ..plugins import db, login_manager
from ..views import user_blue
from ..models import ERole, User, Admin, Teacher, Student
from ..utils import Result, RequestUtils, ObjectUtils


# 会话保护模式 [None|'basic'|'strong']
login_manager.session_protection = "strong"

@login_manager.unauthorized_handler
def unauthorized_handler():
    """ 未登录或无权访问时将自动调用该函数, 默认返回 401 错误 """
    return Result.unauthorized()

@login_manager.needs_refresh_handler
def needs_refresh_handler():
    """ 处理 "非新鲜的" 刷新, 调用 login_manager.confirm_login 函数
        可以重新标记会话为 "新鲜"
    """
    print('need_refresh_handler')
    pass

@login_manager.user_loader
def load_user(user_id):
    """ 登录时自动调用该函数, 该函数是必须设置的, 期待返回一个继承自
        flask_login.UserMixin 的类, 主要是该类默认提供了 get_id 方法,
        用于在登录成功后获取用户 id
    """
    return User(user_id)

@user_blue.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
@login_required
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
@login_required
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
        username, password = RequestUtils.quick_data(
            request,
            'username',
            'password',
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
            if login_user(user):
                return Result.success('登录成功', { **user.vars(), **any_user.vars()})
    return Result.method_not_allowed()

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
@login_required
def logout():
    """ 登出视图 """
    if request.method == 'POST':
        if logout_user():
            return Result.success('登出成功')
        return Result.failure('登出失败')
    return Result.method_not_allowed()
