#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint

errorhandler_blue = Blueprint('errorhandler', __name__)
user_blue = Blueprint('user', __name__, url_prefix='/api/user')
admin_blue = Blueprint('admin', __name__, url_prefix='/api/admin')
assistant_blue = Blueprint('assistant', __name__, url_prefix='/api/assistant')
student_blue = Blueprint('student', __name__, url_prefix='/api/student')
leave_blue = Blueprint('leave', __name__, url_prefix='/api/leave')
notice_blue = Blueprint('notice', __name__, url_prefix='/api/notice')
chart_blue = Blueprint('chart', __name__, url_prefix='/api/chart')
file_blue = Blueprint('file', __name__, url_prefix='/api/file')

from . import errorhandler
from . import user
from . import admin
from . import assistant
from . import student
from . import leave
from . import notice
from . import chart
from . import file
