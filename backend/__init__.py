#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .app import UPLOAD_FOLDER
from .app import ALLOWED_IMAGE_EXTENSIONS

from .app import app
from .app import db


__all__ = ('UPLOAD_FOLDER', 'ALLOWED_IMAGE_EXTENSIONS', 'app', 'db')


from .views import errorhandler_blue
from .views import user_blue
from .views import admin_blue
from .views import teacher_blue
from .views import student_blue
from .views import leave_blue
from .views import upload_blue

app.register_blueprint(errorhandler_blue)
app.register_blueprint(user_blue)
app.register_blueprint(admin_blue)
app.register_blueprint(teacher_blue)
app.register_blueprint(student_blue)
app.register_blueprint(leave_blue)
app.register_blueprint(upload_blue)
