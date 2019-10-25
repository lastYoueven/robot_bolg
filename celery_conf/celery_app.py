#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-19 17:37
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : celery_app.py
# @Software: PyCharm

import celery

from config import CELERY_BROKER_URL, CELERY_BACKEND_URL

app = celery.Celery('app',
                    broker=CELERY_BROKER_URL,
                    # backend=CELERY_BACKEND_URL,
                    include=['celery_conf.tasks', 'celery_conf.php_tasks']
                    )

app.config_from_object('celery_conf.conf')