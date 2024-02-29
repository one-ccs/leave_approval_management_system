
from flask import request
from flask_login import login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError
from ..flaskapp import db, login_manager, unify_response
from ..models import User
from ..views import user_blue


# 会话保护模式 [None|'basic'|'strong']
login_manager.session_protection = "strong"

@login_manager.unauthorized_handler
def unauthorized_handler():
    """ 未登录或无权访问时将自动调用该函数, 默认返回 401 错误 """
    return unify_response(401, False, '未登录, 拒绝访问')

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
        flask_login.fUserMixin 的类, 主要是该类默认提供了 get_id 方法,
        用于在登录成功后获取用户 id
    """
    return User.query.get(user_id)

@user_blue.route('/')
def root():
    return unify_response(200, msg='成功')


@user_blue.route('/login', methods=['GET', 'POST'])
def login():
    """ 登录视图 """
    # 判断是否存在该用户
    if request.method == 'GET':
        args = session.get('role', {})
        return render_template('/session.html', **args)
    # 用户登录
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')

        if not username or not password:
            return unify_response(401, msg='请输入账号和密码')
        else:
            user = User(name=username)

            if not user.exist():
                return unify_response(401, False, '登录失败, 不存在该用户')
            if not user.check_password_hash(password):
                return unify_response(401, False, '登录失败, 密码错误')
            if login_user(user):
                data = user.value_of()
                del data['id']
                del data['userId']
                return unify_response(200, data, '登录成功')
    return unify_response(405, '无效的请求')

@user_blue.route('/regist', methods=['POST'])
def regist():
    """ 注册视图 """
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')

        if not username or not password:
            return unify_response(401, msg='请输入账号和密码')
        else:
            try:
                user = User(name=username, password=password)
                db.session.add(user)
                db.session.commit()
            except IntegrityError:
                return unify_response(403, msg='账号已存在')
            return unify_response(200, True, '注册成功')
    return unify_response(405, '无效的请求')

@user_blue.route('/logout', methods=['POST'])
@login_required
def logout():
    """ 登出视图 """
    if request.method == 'POST':
        if logout_user():
            return unify_response(200, True, '登出成功')
        return unify_response(403, False, '登出失败')
    return unify_response(405, '无效的请求')
