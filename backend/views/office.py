#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, session, make_response, render_template, url_for, redirect
from os import path
from ..app import db
from ..views import office_blue


@office_blue.before_request
def check_login():
    if 'role' not in session:
        if request.path == '/office/':
            return redirect('/session')
        else:
            return make_response({'state': 'fail', 'msg': '请登录后操作'}, 401)
    if session.get('role').get('role') != '教务处':
        return make_response({'state': 'fail', 'msg': '非法操作, 拒绝访问'}, 403)

@office_blue.route('/')
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
    return render_template('/office.html', **args)

@office_blue.route('/leaves', methods=['GET', 'POST'])
def leaves():
    res = None
    tid = session.get('role').get('rid')
    if request.method == 'GET': # 返回待审批及总览
        result = []
        query = request.values.get('query')
        if query == 'approval':
            result = db.execute('SELECT a.*,b.name name,c.name a1,d.name a2, e.name r FROM leave a LEFT JOIN student b ON a.sid=b.sid LEFT JOIN teacher c ON a.approver1_id=c.tid LEFT JOIN teacher d ON a.approver2_id=d.tid LEFT JOIN teacher e ON a.revoke_id=e.tid WHERE state IN ("待审批", "审批中", "销假中")')
        elif query == 'total':
            result = db.execute('SELECT a.*,b.name name,c.name a1,d.name a2, e.name r FROM leave a LEFT JOIN student b ON a.sid=b.sid LEFT JOIN teacher c ON a.approver1_id=c.tid LEFT JOIN teacher d ON a.approver2_id=d.tid LEFT JOIN teacher e ON a.revoke_id=e.tid')
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
                'a1_timestamp': row['a1_timestamp'],
                'a2': row['a2'],
                'a2_timestamp': row['a2_timestamp'],
                'r': row['r'],
                'r_timestamp': row['r_timestamp'],
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
                # 查询请假条状态, 过滤无效请假条
                result = db.execute('SELECT state,start_timestamp,end_timestamp FROM leave WHERE id=?', (id, ))
                if not len(result):
                    continue
                if result[0]['state'] not in ('待审批', '审批中', '销假中'):
                    continue
                # 销假中修改为“已完成”, 修改状态为“待销假”
                if result[0]['state'] == '销假中':
                    values.append(('已完成', tid, id))
                elif result[0]['state'] in ('待审批', '审批中'):
                    values.append(('待销假', tid, id))
            if not len(values):
                return make_response({'state': 'fail', 'msg': '未提供有效的请假条信息'}, 403)
            revokes = [value for value in values if value[0] == '已完成']
            approvals = [value for value in values if value[0] in ('审批中', '待销假')]
            result1 = result2 = 0
            if len(revokes):
                result1 = db.executemany('UPDATE leave SET state=?,revoke_id=?,r_timestamp=CURRENT_TIMESTAMP WHERE id=?', tuple(revokes))
            if len(approvals):
                result2 = db.executemany('UPDATE leave SET state=?,approver2_id=?,a2_timestamp=CURRENT_TIMESTAMP WHERE id=?', tuple(approvals))
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
                if result[0]['state'] not in ('待审批', '审批中'):
                    continue
                refuses.append(('已驳回', tid, id))
            if not len(refuses):
                return make_response({'state': 'fail', 'msg': '未提供有效的请假条信息'}, 403)
            if len(refuses):
                result = db.executemany('UPDATE leave SET state=?,approver2_id=?,a2_timestamp=CURRENT_TIMESTAMP WHERE id=?', tuple(refuses))
            if result:
                res = make_response({'state': 'ok', 'msg': f'操作成功, 成功修改 {result} 条数据'}, 200)
            else:
                res = make_response({'state': 'fail', 'msg': '操作失败'}, 403)
        else:
            res = make_response({'state': 'fail', 'msg': f'不支持的操作 "{action}"'}, 403)
    return res
