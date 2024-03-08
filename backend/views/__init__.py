#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint

errorhandler_blue = Blueprint('errorhandler', __name__)
user_blue = Blueprint('user', __name__, url_prefix='/api/user')
admin_blue = Blueprint('admin', __name__, url_prefix='/api/admin')
teacher_blue = Blueprint('assistant', __name__, url_prefix='/api/assistant')
student_blue = Blueprint('student', __name__, url_prefix='/api/student')
leave_blue = Blueprint('leave', __name__, url_prefix='/api/leave')
upload_blue = Blueprint('upload', __name__, url_prefix='/api/upload')

from . import errorhandler
from . import user
from . import admin
from . import teacher
from . import student
from . import leave
from . import upload
