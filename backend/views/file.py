#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, send_from_directory
from flask_jwt_extended import jwt_required
from mimetypes import guess_type
from ..config import AppConfig
from ..views import file_blue
from ..utils import Result, RequestUtils, PathUtils


@file_blue.route('/<path:file_path>', methods=['GET'])
def resource(file_path):
    """ 返回文件
    注意：不能使用 @jwt_required() 进行身份校验，会导致响应体格式变为 application/json
    """
    directory = f'{AppConfig.UPLOAD_FOLDER}/{file_path}'
    mimetype, encoding = guess_type(directory)

    return send_from_directory(
        PathUtils.path.dirname(directory),
        PathUtils.path.basename(directory),
        as_attachment=False,
        mimetype=mimetype,
    )

@file_blue.route('/<path:file_path>', methods=['POST'])
@jwt_required()
def upload(file_path: str):
    """文件上传接口"""
    file, filename = RequestUtils.quick_data(request, 'file', 'filename')

    if not file:
        return Result.failure('上传文件为空')
    if not filename:
        return Result.failure('文件名参数为空')

    suffix = PathUtils.path.splitext(file.filename)[1][1:]
    if suffix not in AppConfig.ALLOWED_IMAGE_EXTENSIONS:
        return Result.failure('不支持的文件格式')

    filename = PathUtils.secure_filename(f'{filename}.{suffix}')
    file.save(f'{AppConfig.UPLOAD_FOLDER}/{file_path}/{filename}')

    return Result.success('文件上传成功', f'/{file_path}/{filename}')
