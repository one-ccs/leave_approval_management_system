#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, send_from_directory
from flask_jwt_extended import jwt_required
from mimetypes import guess_type
from ..config import AppConfig
from ..utils import Result, RequestUtils, PathUtils
from ..views import file_blue


@file_blue.route('/<path:file_path>', methods=['GET'])
def resource(file_path):
    """ 返回文件
    注意：不能使用 @jwt_required() 进行身份校验，会导致响应体格式变为 application/json
    """
    directory = f'{AppConfig.UPLOAD_FOLDER}/{file_path}'
    mimetype, encoding = guess_type(directory)

    return send_from_directory(directory, '', as_attachment=False, mimetype=mimetype)

@file_blue.route('/upload/avatar', methods=['POST'])
@jwt_required()
def upload():
    file, filename = RequestUtils.quick_data(request, 'file', 'filename')

    if not file:
        return Result.failure('上传文件为空')
    if not filename:
        return Result.failure('文件名参数为空')

    suffix = PathUtils.splitext(file.filename)[1][1:]
    if suffix not in AppConfig.ALLOWED_IMAGE_EXTENSIONS:
        return Result.failure('不支持的文件格式')

    filename = PathUtils.secure_filename(f'{filename}.{suffix}')
    file.save(f'{AppConfig.UPLOAD_FOLDER}/image/avatar/{filename}')

    return Result.success('头像上传成功', f'/image/avatar/{filename}')

@file_blue.route('/download/<path:file_path>', methods=['GET'])
def download(file_path):
    """ 下载文件
    注意：不能使用 @jwt_required() 进行身份校验，会导致响应体格式变为 application/json
    """
    directory = f'{AppConfig.UPLOAD_FOLDER}/{file_path}'
    mimetype, encoding = guess_type(directory)

    return send_from_directory(directory, '', as_attachment=True, mimetype=mimetype)
