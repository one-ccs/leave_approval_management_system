#!/usr/bin/env python
# -*- coding: utf-8 -*-
from redis import StrictRedis
from ..config import RedisConfig

redis = StrictRedis(
    host=RedisConfig.HOST,
    port=RedisConfig.PORT,
    db=RedisConfig.DB,
    decode_responses=True,
)
