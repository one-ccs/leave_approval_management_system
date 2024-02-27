#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
import sqlite3


class Database:
    """ 封装数据库操作 """
    last_error = ''

    def __new__(cls, *arg, **kw):
        # 实现单例模式
        if not hasattr(cls, '_instance'):
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_path):
        if not path.isfile(db_path):
            raise ValueError(f'无效的数据库文件路径({db_path}).')
        self.db_path = db_path

    def execute(self, sql, args=()):
        connection = sqlite3.connect(self.db_path)
        result = None
        try:
            if sql[:6].lower() == 'select':
                connection.row_factory = sqlite3.Row
                result = connection.execute(sql, args).fetchall()
            if sql[:6].lower() in ('insert', 'delete', 'update'):
                with connection:
                    result = connection.execute(sql, args).rowcount
        except sqlite3.IntegrityError as e:
            Database.last_error = e
            result = None
        except sqlite3.Error as e:
            Database.last_error = e
            raise e
        finally:
            connection.close()
        return result

    def executemany(self, sql, args=()):
        connection = sqlite3.connect(self.db_path)
        result = None
        try:
            if sql[:6].lower() == 'select':
                connection.row_factory = sqlite3.Row
                result = connection.executemany(sql, args).fetchall()
            if sql[:6].lower() in ('insert', 'delete', 'update'):
                with connection:
                    result = connection.executemany(sql, args).rowcount
        except sqlite3.IntegrityError as e:
            Database.last_error = e
            result = None
        except sqlite3.Error as e:
            Database.last_error = e
            raise e
        finally:
            connection.close()
        return result
