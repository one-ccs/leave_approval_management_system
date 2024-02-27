#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .flaskapp import UPLOAD_FOLDER
from .flaskapp import ALLOWED_IMAGE_EXTENSIONS

from .flaskapp import flaskapp
from .flaskapp import db


__all__ = ('UPLOAD_FOLDER', 'ALLOWED_IMAGE_EXTENSIONS', 'flaskapp', 'db')


from .views import errorhandle_blue
from .views import student_blue
from .views import assistant_blue
from .views import office_blue
from .views import attendance_blue
from .views import admin_blue

flaskapp.register_blueprint(errorhandle_blue)
flaskapp.register_blueprint(student_blue)
flaskapp.register_blueprint(assistant_blue)
flaskapp.register_blueprint(office_blue)
flaskapp.register_blueprint(attendance_blue)
flaskapp.register_blueprint(admin_blue)
