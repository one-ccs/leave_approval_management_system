#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, url_for, redirect
from .config import MAIN_KEY
from .utils import _Flask, Result, RequestUtils


app = _Flask(__name__)


@app.after_request
def cors(response):
    """放行不在白名单的域"""
    origin, origin_token = RequestUtils.quick_data(request, 'origin', 'originToken')
    if origin and origin_token == MAIN_KEY:
        response.headers['Access-Control-Allow-Origin'] = origin

    return response

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route('/api')
def api():
    return Result.success('ok', True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
