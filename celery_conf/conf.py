#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-19 17:37
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : conf.py
# @Software: PyCharm

from celery.schedules import crontab

CELERY_TIMEZONE = 'Asia/Chongqing'
# CELERYD_TASK_SOFT_TIME_LIMIT = 60
CELERY_TASK_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 2
CELERYD_CONCURRENCY = 2
CELERYD_MAX_MEMORY_PER_CHILD = 200000  # 每个 worker 最大内存占用 200MB

# 防止使用 eta 或 countdown 延时执行的任务重复执行，visibility_timeout 改为 1 周,
# eta 或 countdown 如果在 visibility_timeout 内不执行就会重新发送一个任务
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 60 * 60 * 24 * 7}

# 每个 worker 预取得任务数
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_TASK_ACKS_LATE = True

# Crontab
CELERYBEAT_SCHEDULE = {
    # 每天同步一次有效账号的房源信息
    'get_hot_top_news': {
        'task': 'get_hot_top_news',
        'schedule': crontab(minute=0, hour=10),
    },
    # 每日检查热点（）
    'note_auto_pub': {
        'task': 'note_auto_pub',
        'schedule': crontab(hour=2, minute=0),
        'args': (2,),
    }
}