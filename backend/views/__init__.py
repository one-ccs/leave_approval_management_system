#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint

errorhandle_blue = Blueprint('errorhandle', __name__)
student_blue = Blueprint('student', __name__, url_prefix='/student')
assistant_blue = Blueprint('assistant', __name__, url_prefix='/assistant')
office_blue = Blueprint('office', __name__, url_prefix='/office')
attendance_blue = Blueprint('attendance', __name__, url_prefix='/attendance')
admin_blue = Blueprint('admin', __name__, url_prefix='/admin')

from . import errorhandle
from . import student
from . import assistant
from . import office
from . import attendance
from . import admin
