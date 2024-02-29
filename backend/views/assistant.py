#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, session, make_response, render_template, url_for, redirect
from os import path
from ..flaskapp import db
from ..views import assistant_blue
from classes import Datetime


@assistant_blue.before_request
def check_login():
    if 'role' not in session:
        if request.path == '/assistant/':
            return redirect('/session')
        else:
            return make_response({'state': 'fail', 'msg': '请登录后操作'}, 401)
    if session.get('role').get('role') != '辅导员':
        return make_response({'state': 'fail', 'msg': '非法操作, 拒绝访问'}, 403)

@assistant_blue.route('/')
def root():
    rid = session.get('role').get('rid')
    args = {'avatar': ''}
    result = db.execute('SELECT * FROM teacher WHERE tid=?', (rid, ))
    if len(result):
        result = result[0]
        args = {
            'rid': result['tid'],
            'name': result['name'],
            'gender': result['gender'],
            'telphone': result['telphone']
        }
    else:
        args = {
            'rid': session.get('role').get('rid'),
            'name': session.get('role').get('name'),
        }
    avatar_path = url_for('static', filename=f'user_upload/avatar/{args["rid"]}.webp')
    if path.isfile('fontend' + avatar_path):
        args['avatar'] = avatar_path
    return render_template('/assistant.html', **args)

@assistant_blue.route('/leaves', methods=['GET', 'POST'])
def leaves():
    res = None
    tid = session.get('role').get('rid')
    if request.method == 'GET': # 返回待审批及总览
        query = request.values.get('query')
        if query == 'approval':
            result = db.execute(
                'SELECT a.*,b.name name,c.name a1,d.name a2 FROM leave a LEFT JOIN student b ON a.sid=b.sid LEFT JOIN teacher c ON a.approver1_id=c.tid LEFT JOIN teacher d ON a.approver2_id=d.tid WHERE b.tid=? and state IN ("待审批", "审批中", "销假中")',
                (tid, )
            )
        elif query == 'total':
            result = db.execute(
                'SELECT a.*,b.name name,c.name a1,d.name a2 FROM leave a LEFT JOIN student b ON a.sid=b.sid LEFT JOIN teacher c ON a.approver1_id=c.tid LEFT JOIN teacher d ON a.approver2_id=d.tid WHERE b.tid=?',
                (tid, )
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
                'sid': row['sid'],
                'name': row['name'],
                'apply_timestamp': row['apply_timestamp'],
                'category': row['category'],
                'start_timestamp': row['start_timestamp'],
                'end_timestamp': row['end_timestamp'],
                'reason': row['reason'],
                'a1': row['a1'],
                'a2': row['a2'],
                'state': row['state'],
            })
        res = make_response(dict, 200)
    if request.method == 'POST': # 同意或驳回申请
        ids = request.values.get('ids')
        if not ids:
            return make_response({'state': 'fail', 'msg': '未提供要删除的学号'}, 403)
        ids = ids.split(',')
        action = request.values.get('action')
        if action == 'agree': # 同意
            result, values = None, []
            for id in ids:
                # 查询请假条状态, 过滤无效请假条, 计算请假时长
                result = db.execute('SELECT state,start_timestamp,end_timestamp FROM leave WHERE id=?', (id, ))
                if not len(result):
                    continue
                if result[0]['state'] not in ('待审批', '销假中'):
                    continue
                # 请假天数, 向上取整, 时长不足 24 小时但跨天则算 2 天
                diff_day = int(0.5 + Datetime.diff(result[0]['end_timestamp'], result[0]['start_timestamp']).total_seconds() / 3600 / 24)
                start_day = Datetime.day(result[0]['start_timestamp'])
                end_day = Datetime.day(result[0]['end_timestamp'])
                if diff_day == 1 and start_day != end_day:
                    diff_day = 2
                # 大于等于 3 天，修改状态为“审批中”; 小于三天，修改状态为“待销假”
                if result[0]['state'] == '销假中':
                    values.append(('已完成', tid, id))
                else:
                    values.append(('审批中' if diff_day >= 3 else '待销假', tid, id))
            if not len(values):
                return make_response({'state': 'fail', 'msg': '未提供有效的请假条信息'}, 403)
            revokes = [value for value in values if value[0] == '已完成']
            approvals = [value for value in values if value[0] in ('审批中', '待销假')]
            result1 = result2 = 0
            if len(revokes):
                result1 = db.executemany('UPDATE leave SET state=?,revoke_id=?,r_timestamp=CURRENT_TIMESTAMP WHERE id=?', tuple(revokes))
            if len(approvals):
                result2 = db.executemany('UPDATE leave SET state=?,approver1_id=?,a1_timestamp=CURRENT_TIMESTAMP WHERE id=?', tuple(approvals))
            if result1 or result2:
                res = make_response({'state': 'ok', 'msg': f'操作成功, 成功修改 {result1 + result2} 条数据'}, 200)
            else:
                res = make_response({'state': 'fail', 'msg': '操作失败'}, 403)
        elif action == 'refuse': # 驳回
            result, refuses = None, []
            for id in ids:
                # 查询请假条状态, 过滤无效请假条
                result = db.execute('SELECT state,start_timestamp,end_timestamp FROM leave WHERE id=?', (id, ))
                if not len(result):
                    continue
                if result[0]['state'] != '待审批':
                    continue
                refuses.append(('已驳回', tid, id))
            if not len(refuses):
                return make_response({'state': 'fail', 'msg': '未提供有效的请假条信息'}, 403)
            if len(refuses):
                result = db.executemany('UPDATE leave SET state=?,approver1_id=?,a1_timestamp=CURRENT_TIMESTAMP WHERE id=?', tuple(refuses))
            if result:
                res = make_response({'state': 'ok', 'msg': f'操作成功, 成功修改 {result} 条数据'}, 200)
            else:
                res = make_response({'state': 'fail', 'msg': '操作失败'}, 403)
        else:
            res = make_response({'state': 'fail', 'msg': f'不支持的操作 "{action}"'}, 403)
    return res
