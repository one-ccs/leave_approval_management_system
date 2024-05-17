#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union
from flask import request
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token
from flask_jwt_extended import current_user
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from flasgger import swag_from
from ..plugins import db, redis, jwt
from ..views import user_blue
from ..models import ERole, MixUser, User, Admin, Assistant, Student
from ..utils import Result, RequestUtils, ObjectUtils, DateTimeUtils


@jwt.user_identity_loader
def user_identity_loader(mix_user: MixUser):
    """ 创建 JWT 时，设置 identity 的回调函数 """
    return mix_user

@jwt.user_lookup_loader
def user_lookup_loader(jwt_header, jwt_data):
    """ 通过 JWT 加载用户对象，可通过 current_user 或 get_current_user() 获取 """
    identity = jwt_data['sub']
    return MixUser(User().withDict(**identity), identity['anyUser'])

@jwt.user_lookup_error_loader
def user_lookup_error_loader(jwt_header, jwt_payload: dict):
    """ 加载用户错误时的响应 """
    return Result.failure('获取用户信息失败，无法验证用户')

@jwt.token_in_blocklist_loader
def token_in_blocklist_loader(jwt_header, jwt_payload: dict):
    """ 返回 JWT 是否有效 """
    id = ObjectUtils.get_value_from_dict(jwt_payload, 'sub.id', None)
    return not redis.get(id)

@jwt.expired_token_loader
def expired_token_loader(jwt_header, jwt_payload: dict):
    """ 令牌过期时的响应 """
    ttype = jwt_payload['type']
    return Result.failure(f'{ttype} 令牌已过期', None, 401.8)

@jwt.invalid_token_loader
def invalid_token_loader(reason: str):
    """ 令牌无效时的响应 """
    return Result.unauthorized(f'无效的令牌\n({reason})')

@jwt.needs_fresh_token_loader
def needs_fresh_token_loader(jwt_header, jwt_payload: dict):
    """ 令牌不新鲜时的响应 """
    return Result.forbidden('需要验证密码')

@jwt.revoked_token_loader
def revoked_token_loader(jwt_header, jwt_payload: dict):
    """ 令牌已撤销时的响应 """
    return Result.unauthorized('用户已登出，请重新登录')

@jwt.token_verification_failed_loader
def token_verification_failed_loader(jwt_header, jwt_payload: dict):
    """ 令牌验证失败时的响应 """
    ttype = jwt_payload['type']
    return Result.unauthorized(f'无效的 {ttype} 令牌')

@jwt.unauthorized_loader
def unauthorized_loader(reason: str):
    """ 没有令牌时的响应 """
    return Result.unauthorized()


@user_blue.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
@jwt_required()
@swag_from('./api_docs/user/root.yml')
def root():
    # 查询
    if request.method == 'GET':
        id = RequestUtils.quick_data(request, ('id', int))
        user = User(id)
        # 获取详细信息
        any_user: Union[Admin, Assistant, Student] = None
        if user.role == ERole.ADMIN:
            any_user = Admin.query.filter_by(user_id=user.id).first()
        elif user.role == ERole.TEACHER:
            any_user = Assistant.query.filter_by(user_id=user.id).first()
        elif user.role == ERole.STUDENT:
            any_user = Student.query.filter_by(user_id=user.id).first()
        else:
            return Result.failure('未知角色')
        return Result.success('查询成功', { **user.vars(), **any_user.vars()})
    # 添加
    if request.method == 'PUT':
        pass
    # 修改
    if request.method == 'POST':
        request_data = RequestUtils.quick_data(request)
        result = User.query.filter(
            User.id == request_data.get('id', current_user.id),
        ).update(ObjectUtils.vars(request_data, ['id']))
        db.session.commit()
        if result > 0:
            return Result.success('修改成功')
        return Result.failure('修改失败')
    # 删除
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
            any_user: Union[Admin, Assistant, Student] = None
            assistant: Assistant = None
            if user.role == ERole.ADMIN:
                any_user = Admin.query.filter_by(user_id=user.id).first()
            elif user.role == ERole.TEACHER:
                any_user = Assistant.query.filter_by(user_id=user.id).first()
            elif user.role == ERole.STUDENT:
                any_user = Student.query.filter_by(user_id=user.id).first()
                assistant = Assistant.query.filter_by(id=any_user.assistant_id).first()
            else:
                return Result.failure('登录失败\n角色数据异常\n请联系管理员')

            # 登录用户 (设置 15 分钟内为新鲜)
            access_token = create_access_token(identity=MixUser(user, any_user.vars()), fresh=DateTimeUtils.timedelta(minutes=15))
            refresh_token = create_refresh_token(identity=MixUser(user, any_user.vars()))

            # 持久化记录用户登录状态
            redis.set(user.id, 1)

            return Result.success('登录成功', {
                **user.vars(),
                **any_user.vars(),
                'assistantUserId': assistant and assistant.user_id,
                'accessToken': access_token,
                'refreshToken': refresh_token,
            })
    return Result.method_not_allowed()

@user_blue.route('/refreshToken', methods=['POST'])
@jwt_required(refresh=True)
def refresh_token():
    """ 使用刷新 token 获取新的访问 token, 并标记为不新鲜 """
    access_token = create_access_token(identity=current_user, fresh=False)
    return Result.success('刷新令牌成功', access_token)

@user_blue.route('/register', methods=['POST'])
def register():
    """ 注册视图 """
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

@user_blue.route('/logout', methods=['POST'])
@jwt_required(verify_type=False)
def logout():
    """ 登出视图 """
    # 将对应用户 id 拉黑
    redis.set(current_user.id, 0)

    return Result.success('登出成功')
