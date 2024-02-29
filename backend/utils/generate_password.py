#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash

if __name__ == '__main__':
    pwd = input('请输入明文密码: ')
    hash_pwd = generate_password_hash(pwd)[21:]
    print('加密后的密码为: ')
    print(hash_pwd)
