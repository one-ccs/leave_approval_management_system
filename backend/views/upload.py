#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, session
from ..app import UPLOAD_FOLDER
from ..views import upload_blue
from ..utils import Result

@upload_blue.route('/upload/<path:key>', methods=['POST'])
def upload(key):
    if key == 'avatar':
        file_data = request.files.get('file_data')
        if file_data:
            filename = f'{session.get("role").get("rid")}.webp'
            file_data.save(f'{UPLOAD_FOLDER}/avatar/{filename}')
        return Result.success(True, '头像上传成功')
    else:
        return Result.forbidden()
