#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import send_from_directory
from flask_login import login_required
from mimetypes import guess_type
from ..config import AppConfig
from ..views import file_blue


@file_blue.route('/<path:file_path>', methods=['GET'])
@login_required
def file(file_path):
    # 注意 f'.{UPLOAD_FOLDER}/{file_path}' 之前的 "."
    directory = f'.{AppConfig.UPLOAD_FOLDER}/{file_path}'
    mimetype, encoding = guess_type(directory)

    return send_from_directory(directory, '', as_attachment=True, mimetype=mimetype)
