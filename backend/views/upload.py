#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_login import login_required
from werkzeug.utils import secure_filename
from os import path
from ..config import AppConfig
from ..views import upload_blue
from ..utils import Result, RequestUtils


@upload_blue.route('/avatar', methods=['POST'])
@login_required
def upload():
    file, filename = RequestUtils.quick_data(request, 'file', 'filename')

    if not file:
        return Result.failure('上传文件为空')
    if not filename:
        return Result.failure('文件名参数为空')

    suffix = path.splitext(file.filename)[1][1:]
    if suffix not in AppConfig.ALLOWED_IMAGE_EXTENSIONS:
        return Result.failure('不支持的文件格式')

    filename = secure_filename(f'{filename}.{suffix}')
    file.save(f'{AppConfig.UPLOAD_FOLDER}/image/avatar/{filename}')

    return Result.success('头像上传成功', f'/image/avatar/{filename}')
