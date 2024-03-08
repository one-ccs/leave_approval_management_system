#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, session, make_response, render_template, url_for, redirect
from os import path
from ..app import db
from ..views import admin_blue


@admin_blue.before_request
def check_login():
    if 'role' not in session:
        if request.path == '/admin/':
            return redirect('/session')
        else:
            return make_response({'state': 'fail', 'msg': '请登录后操作'}, 401)
    if session.get('role').get('role') != '管理员':
        return make_response({'state': 'fail', 'msg': '非法操作, 拒绝访问'}, 403)

@admin_blue.route('/')
def root():
    rid = session.get('role').get('rid')
    args = {'avatar': ''}
    result = db.execute('SELECT * FROM admin WHERE aid=?', (rid, ))
    if len(result):
        result = result[0]
        args = {
            'rid': result['aid'],
            'name': result['name'],
            'gender': result['gender'],
        }
    else:
        args = {
            'rid': session.get('role').get('rid'),
            'name': session.get('role').get('name'),
        }
    avatar_path = url_for('static', filename=f'user_upload/avatar/{args["rid"]}.webp')
    if path.isfile('frontend' + avatar_path):
        args['avatar'] = avatar_path
    return render_template('/admin.html', **args)

@admin_blue.route('/students', methods=['GET', 'POST', 'DELETE'])
def students():
    res = None
    if request.method == 'GET': # 查询
        query = request.values.get('query', None)
        if query == 'all':
            result = db.execute('SELECT row_number() OVER(ORDER BY sid ASC) as "on",b.name tname,a.* FROM student a LEFT JOIN teacher b WHERE a.tid=b.tid')
            dict = {
                'state': 'ok',
                'msg': '查询成功',
                'length': len(result),
                'data': []
            }
            for row in result:
                dict['data'].append({
                    'on': row['on'],
                    'id': row['id'],
                    'sid': row['sid'],
                    'name': row['name'],
                    'gender': row['gender'],
                    'tid': row['tid'],
                    'tname': row['tname'],
                    'department': row['department'],
                    'faculty': row['faculty'],
                    'major': row['major'],
                    'grade': row['grade'],
                    'class': row['class'],
                })
            res = make_response(dict, 200)
        else:
            res = make_response({'state': 'fail', 'msg': f'不支持的查询 "{query}", 请求已拒绝'}, 403)
    if request.method == 'POST': # 修改
        action = request.values.get('action')
        if action == 'modify':
            ids = request.values.get('ids')
            if not ids or len(ids) == 0:
                return make_response({'state': 'fail', 'msg': '未提供 ID'}, 403)
            ids = ids.split(',')

            name = request.values.get('name')
            gend = request.values.get('gender')
            tid = request.values.get('tid')
            depa = request.values.get('department')
            facu = request.values.get('faculty')
            majo = request.values.get('major')
            grad = request.values.get('grade')
            clas = request.values.get('class')

            if len(ids) == 1: # 单独修改
                result = db.execute(
                    'UPDATE student SET tid=?,name=?,gender=?,department=?,faculty=?,major=?,grade=?,class=? WHERE id=?',
                    (tid, name, gend, depa, facu, majo, grad, clas, ids[0])
                )
                if result:
                    res = make_response({'state': 'ok', 'msg': f'修改成功, 修改 {result} 条数据'}, 200)
                else:
                    res = make_response({'state': 'fail', 'msg': f'结果: 修改失败;<br>原因: : {db.last_error}'}, 403)
            else: # 批量修改
                list = []
                for id in ids:
                    list.append((tid, depa, facu, majo, grad, clas, id))
                result = db.executemany(
                    'UPDATE student SET tid=?,department=?,faculty=?,major=?,grade=?,class=? WHERE id=?',
                    tuple(list)
                )
                if result:
                    res = make_response({'state': 'ok', 'msg': f'修改成功, 修改 {result} 条数据'}, 200)
                else:
                    res = make_response({'state': 'fail', 'msg': f'结果: 修改失败（批量）;<br>原因: : {db.last_error}'}, 403)
        elif action == 'add':
            name, password = request.values.get('name'), request.values.get('password')
            if not name or not password:
                return make_response({'state': 'fail', 'msg': '用户名和密码不能为空'}, 403)
            user = Student(name, password)
            result = db.execute(
                'INSERT INTO user(username,password) VALUES(?,?)',
                (user.username, user.hash_password)
            )
            if not result:
                return make_response({'state': 'fail', 'msg': '用户名已存在'}, 403)

            res = make_response({'state': 'ok', 'msg': '添加成功'}, 200)
        else:
            res = make_response({'state': 'fail', 'msg': f'不支持的操作 "{action}", 请求已拒绝'}, 403)
    if request.method == 'DELETE': # 删除
        sids = request.values.get('sids')
        if not sids or len(sids) == 0:
            return make_response({'state': 'fail', 'msg': '未提供要删除的学号'}, 403)
        sids = sids.split(',')
        _sids = []
        for sid in sids:
            _sids.append((sid, ))
        result = db.executemany('DELETE FROM student WHERE sid=?', tuple(_sids))
        if result and result > 0:
            res = make_response({'state': 'ok', 'msg': f'删除成功, 共删除 {result} 条'}, 200)
        else:
            res = make_response({'state': 'fail', 'msg': '删除失败'}, 403)
    return res

@admin_blue.route('/teachers', methods=['GET', 'POST', 'DELETE'])
def teachers():
    res = None
    if request.method == 'GET': # 查询
        query = request.values.get('query', None)
        if query == 'all':
            result = db.execute('SELECT row_number() OVER(ORDER BY tid ASC) as "on",teacher.*,role.role FROM teacher,role where teacher.tid=role.rid')
            dict = {
                'state': 'ok',
                'msg': '查询成功',
                'length': len(result),
                'data': []
            }
            for row in result:
                dict['data'].append({
                    'on': row['on'],
                    'id': row['id'],
                    'tid': row['tid'],
                    'name': row['name'],
                    'gender': row['gender'],
                    'telephone': row['telephone'],
                    'role': row['role'],
                })
            res = make_response(dict, 200)
        elif query == 'simple':
            result = db.execute('SELECT tid,name,role FROM teacher a LEFT JOIN role b WHERE a.tid=b.rid AND role="辅导员"')
            dict = {
                'state': 'ok',
                'msg': '查询成功',
                'length': len(result),
                'data': []
            }
            for row in result:
                dict['data'].append({
                    'tid': row['tid'],
                    'name': row['name'],
                })
            res = make_response(dict, 200)
        else:
            res = make_response({'state': 'fail', 'msg': f'不支持的查询 "{query}", 请求已拒绝'}, 403)
    if request.method == 'POST': # 修改
        action = request.values.get('action')
        if action == 'modify':
            ids = request.values.get('ids')
            tids = request.values.get('tids')
            if not ids or len(ids) == 0:
                return make_response({'state': 'fail', 'msg': '未提供 ID'}, 403)
            if not tids or len(tids) == 0:
                return make_response({'state': 'fail', 'msg': '未提供教师编号'}, 403)
            ids = ids.split(',')
            tids = tids.split(',')

            name = request.values.get('name')
            gend = request.values.get('gender')
            telp = request.values.get('telephone')
            role = request.values.get('role')

            if len(ids) == 1: # 单独修改
                result = db.execute(
                    'UPDATE teacher SET tid=?,name=?,gender=?,telephone=? WHERE id=?',
                    (tids[0], name, gend, telp, ids[0])
                )
                if result:
                    res = make_response({'state': 'ok', 'msg': f'修改成功, 修改 {result} 条数据'}, 200)
                else:
                    res = make_response({'state': 'fail', 'msg': f'结果: 修改失败;<br>原因: : {db.last_error}'}, 403)
            else: # 批量修改
                count = 0
                if gend: # 修改性别
                    list = []
                    for id in ids:
                        list.append((gend, id))
                    result = db.executemany(
                        'UPDATE teacher SET gender=? WHERE id=?',
                        tuple(list)
                    )
                    count = result or 0
                if role: # 修改职能
                    list = []
                    for tid in tids:
                        list.append((role, tid))
                    result = db.executemany(
                        'UPDATE role SET role=? WHERE rid=?',
                        tuple(list)
                    )
                    count = result or 0
                if count:
                    res = make_response({'state': 'ok', 'msg': f'修改成功, 修改 {count} 条数据'}, 200)
                else:
                    res = make_response({'state': 'fail', 'msg': f'结果: 修改失败（批量）;<br>原因: : {db.last_error}'}, 403)
        elif action == 'add':
            name, password = request.values.get('name'), request.values.get('password')
            if not name or not password:
                return make_response({'state': 'fail', 'msg': '用户名和密码不能为空'}, 403)
            user = Student(name, password)
            result = db.execute(
                'INSERT INTO user(username,password) VALUES(?,?)',
                (user.username, user.hash_password)
            )
            if not result:
                return make_response({'state': 'fail', 'msg': '用户名已存在'}, 403)

            res = make_response({'state': 'ok', 'msg': '添加成功'}, 200)
        else:
            res = make_response({'state': 'fail', 'msg': f'不支持的操作 "{action}", 请求已拒绝'}, 403)
    if request.method == 'DELETE': # 删除
        tids = request.values.get('tids')
        if not tids or len(tids) == 0:
            return make_response({'state': 'fail', 'msg': '未提供要删除的学号'}, 403)
        tids = tids.split(',')
        _tids = []
        for tid in tids:
            _tids.append((tid, ))
        result = db.executemany('DELETE FROM teacher WHERE tid=?', tuple(_tids))
        if result and result > 0:
            res = make_response({'state': 'ok', 'msg': f'删除成功, 共删除 {result} 条'}, 200)
        else:
            res = make_response({'state': 'fail', 'msg': '删除失败'}, 403)
    return res
