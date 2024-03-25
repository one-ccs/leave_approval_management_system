#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .app import app
from .plugins import db
from .plugins import login_manager
from .plugins import migrate

db.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)

from .views import errorhandler_blue
from .views import user_blue
from .views import admin_blue
from .views import teacher_blue
from .views import student_blue
from .views import leave_blue
from .views import notice_blue
from .views import upload_blue
from .views import file_blue

app.register_blueprint(errorhandler_blue)
app.register_blueprint(user_blue)
app.register_blueprint(admin_blue)
app.register_blueprint(teacher_blue)
app.register_blueprint(student_blue)
app.register_blueprint(leave_blue)
app.register_blueprint(notice_blue)
app.register_blueprint(upload_blue)
app.register_blueprint(file_blue)
