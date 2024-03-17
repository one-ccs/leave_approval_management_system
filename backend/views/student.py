#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, session, make_response, render_template, url_for, redirect
from os import path
from ..plugins import db
from ..views import student_blue

@student_blue.before_request
def check_login():
    if 'role' not in session:
        if request.path == '/student/':
            return redirect('/session')
        else:
            return make_response({'state': 'fail', 'msg': '请登录后操作'}, 401)
    if session.get('role').get('role') != '学生':
        return make_response({'state': 'fail', 'msg': '非法操作, 拒绝访问'}, 403)

@student_blue.route('/')
def root():
    rid = session.get('role').get('rid')
    args = {'avatar': ''}
    result = db.execute('SELECT * FROM student WHERE sid=?', (rid, ))
    if len(result):
        result = result[0]
        args = {
            'rid': result['sid'],
            'name': result['name'],
            'gender': result['gender'],
            'department': result['department'],
            'faculty': result['faculty'],
            'major': result['major'],
            '_class': result['class']
        }
    else:
        args = {
            'rid': session.get('role').get('rid'),
            'name': session.get('role').get('name'),
        }
    avatar_path = url_for('static', filename=f'user_upload/avatar/{args["rid"]}.webp')
    if path.isfile('frontend' + avatar_path):
        args['avatar'] = avatar_path
    return render_template('/student.html', **args)

@student_blue.route('/leaves', methods=['GET', 'POST', 'DELETE'])
def leaves():
    res = None
    sid = session.get('role').get('rid')
    if request.method == 'GET': # 查询
        result = None
        query = request.values.get('query')
        if query == 'apply': # 请假
            result = db.execute(
                'SELECT a.*,b.name a1,c.name a2,d.name r FROM leave a LEFT JOIN teacher b ON a.approver1_id=b.tid LEFT JOIN teacher c ON a.approver2_id=c.tid LEFT JOIN teacher d ON a.revoke_id=d.tid WHERE sid=? and state IN ("待审批", "审批中")',
                (sid, )
            )
        elif query == 'revoke': # 销假
            result = db.execute(
                'SELECT a.*,b.name a1,c.name a2,d.name r FROM leave a LEFT JOIN teacher b ON a.approver1_id=b.tid LEFT JOIN teacher c ON a.approver2_id=c.tid LEFT JOIN teacher d ON a.revoke_id=d.tid WHERE sid=? and state IN ("待销假", "销假中")',
                (sid, )
            )
        elif query == 'done': # 已完成
            result = db.execute(
                'SELECT a.*,b.name a1,c.name a2,d.name r FROM leave a LEFT JOIN teacher b ON a.approver1_id=b.tid LEFT JOIN teacher c ON a.approver2_id=c.tid LEFT JOIN teacher d ON a.revoke_id=d.tid WHERE sid=? and state IN ("已完成", "已驳回", "已撤回")',
                (sid, )
            )
        else:
            return make_response({'state': 'fail', 'msg': f'不支持的查询 "{query}", 请求已拒绝'}, 403)
        dict = {
            'state': 'ok',
            'msg': '查询成功',
            'length': len(result),
            'data': []
        }
        for row in result:
            dict['data'].append({
                'id': row['id'],
                'apply_timestamp': row['apply_timestamp'],
                'category': row['category'],
                'start_timestamp': row['start_timestamp'],
                'end_timestamp': row['end_timestamp'],
                'reason': row['reason'],
                'a1': row['a1'],
                'a2': row['a2'],
                'r': row['r'],
                'state': row['state'],
            })
        res = make_response(dict, 200)
    if request.method == 'POST': # 新建申请、申请销假
        action = request.values.get('action')
        if action == 'apply':
            category = request.values.get('category')
            start_timestamp = request.values.get('start_timestamp')
            end_timestamp = request.values.get('end_timestamp')
            reason = request.values.get('reason')
            if not category or not start_timestamp or not end_timestamp:
                return make_response({'state': 'fial', 'msg': '申请失败, 类别、开始日期和结束日期不能为空'}, 403)
            start_timestamp = start_timestamp.replace('T', ' ') + ':00'
            end_timestamp = end_timestamp.replace('T', ' ') + ':00'
            result = db.execute(
                'INSERT INTO leave(sid,state,category,start_timestamp,end_timestamp,reason) VALUES(?,?,?,?,?,?)',
                (sid, '待审批', category, start_timestamp, end_timestamp, reason)
            )
            if result and result > 0:
                res = make_response({'state': 'ok', 'msg': '申请成功'}, 200)
            else:
                res = make_response({'state': 'fail', 'msg': '申请失败, 开始日期必须大于当前日期, 结束日期必须大于开始日期'}, 403)
        elif action == 'revoke':
            id = request.values.get('id')
            if not id:
                return make_response({'state': 'fail', 'msg': '销假申请失败, 未知的请假条 ID'}, 403)
            result = db.execute('SELECT state FROM leave WHERE id=?', (id, ))
            if not result or result[0]['state'] != '待销假':
                return make_response({'state': 'fail', 'msg': f'销假申请失败, 无法销假状态为 "{result[0]["state"]}" 的请假条'}, 403)
            result = db.execute('UPDATE leave SET state="销假中" WHERE id=?', (id, ))
            if result and result > 0:
                res = make_response({'state': 'ok', 'msg': '销假申请成功'}, 200)
            else:
                res = make_response({'state': 'fail', 'msg': '销假申请失败'}, 403)
        elif action == 'recall':
            id = request.values.get('id')
            if not id:
                return make_response({'state': 'fail', 'msg': '撤回失败, 未知的请假条 ID'}, 403)
            result = db.execute('SELECT state FROM leave WHERE id=?', (id, ))
            if not result or result[0]['state'] not in ('审批中', '待审批'):
                return make_response({'state': 'fail', 'msg': f'撤回失败, 无法撤回状态为 "{result[0]["state"]}" 的请假条'}, 403)
            result = db.execute('UPDATE leave SET state="已撤回" WHERE id=?', (id, ))
            if result and result > 0:
                res = make_response({'state': 'ok', 'msg': '撤回成功'}, 200)
            else:
                res = make_response({'state': 'fail', 'msg': '撤回失败'}, 403)
        else:
            res = make_response({'state': 'fail', 'msg': f'不支持的操作 "{action}"'}, 403)
    return res
