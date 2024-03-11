#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_login import login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError
from ..app import db, login_manager
from ..models import Role, User, Admin, Teacher, Student
from ..views import user_blue
from ..utils import Result, RequestUtils


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
    return User.query.get(user_id)

@user_blue.route('/')
def root():
    return Result.success('成功', True)

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
        username, password = RequestUtils.quick_data(request, 'username', 'password')

        if not username or not password:
            return Result.failure('请输入账号和密码')
        else:
            user = User(username=username)

            if not user.exist():
                return Result.failure('登录失败\n不存在该用户')
            if not user.check_password_hash(password):
                return Result.failure('登录失败\n密码错误')
            # 获取详细信息
            any_user = None
            if user.role == Role.ADMIN:
                any_user = Admin.query.filter_by(user_id=user.id).first()
            elif user.role == Role.TEACHER:
                any_user = Teacher.query.filter_by(user_id=user.id).first()
            elif user.role == Role.STUDENT:
                any_user = Student.query.filter_by(user_id=user.id).first()
            else:
                return Result.failure('登录失败\n角色数据异常\n请联系管理员')
            # 登录用户
            if login_user(user):
                data = { **user.vars(), **any_user.vars()}
                return Result.success('登录成功', data)
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
            return Result.success('注册成功', True)
    return Result.method_not_allowed()

@user_blue.route('/logout', methods=['POST'])
@login_required
def logout():
    """ 登出视图 """
    if request.method == 'POST':
        if logout_user():
            return Result.success('登出成功', True)
        return Result.failure('登出失败')
    return Result.method_not_allowed()
