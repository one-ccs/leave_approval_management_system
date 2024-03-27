#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..config import FlasggerConfig
from flasgger import Swagger

flasgger = Swagger(
    config=FlasggerConfig.CONFIG,
    template=FlasggerConfig.TEMPLATE,
)
