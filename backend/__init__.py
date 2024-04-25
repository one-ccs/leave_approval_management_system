#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .app import app

__all__ = ['app']

app.url_map.strict_slashes = False

from .config import FlaskConfig
from .config import FlaskCorsConfig
from .config import FlaskJWTExtendedConfig
from .config import FlaskSQLAlchemyConfig
from .config import FlasggerConfig

app.config.from_object(FlaskConfig)
app.config.from_object(FlaskCorsConfig)
app.config.from_object(FlaskJWTExtendedConfig)
app.config.from_object(FlaskSQLAlchemyConfig)
app.config.from_object(FlasggerConfig)

from .plugins import db
from .plugins import cors
from .plugins import jwt
from .plugins import migrate
from .plugins import flasgger

db.init_app(app)
cors.init_app(app)
jwt.init_app(app)
migrate.init_app(app, db)
flasgger.init_app(app)

from .views import errorhandler_blue
from .views import user_blue
from .views import admin_blue
from .views import teacher_blue
from .views import student_blue
from .views import leave_blue
from .views import notice_blue
from .views import file_blue

app.register_blueprint(errorhandler_blue)
app.register_blueprint(user_blue)
app.register_blueprint(admin_blue)
app.register_blueprint(teacher_blue)
app.register_blueprint(student_blue)
app.register_blueprint(leave_blue)
app.register_blueprint(notice_blue)
app.register_blueprint(file_blue)
