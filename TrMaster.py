# -*- coding: utf-8 -*-

__author__ = 'qmax'


import redis
from web import TrAgent

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

ba = TrAgent.BasicAgent('755w', '2250', r)

# 需要知道全路由信息

# 点部列表 中专场列表