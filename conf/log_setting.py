# -*- coding: utf-8 -*-
# @Time     : 2020-3-7 18:23

import logging
import os
from logging.config import dictConfig
from logging.handlers import *
from os.path import dirname

from seleniumwire.proxy.handler import log as LOGGER

# 日志记录级别
LOGGER.setLevel(logging.WARNING)

PROJECT_ROOT = dirname(dirname(os.path.abspath(__file__))).replace('\\', '/')
LOG_PATH = os.path.join(PROJECT_ROOT, 'logs', 'robot_bolg.log')

# 将文件路径分割出来
file_dir = os.path.split(LOG_PATH)[0]

# 创建多级目录
if not os.path.isdir(file_dir):
    os.makedirs(file_dir)

LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] \ '
                      ' [%(levelname)s]- %(message)s'
        },
        # 其他的 formatter
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': LOG_PATH,
            'level': 'WARNING',
            'formatter': 'standard'
        },
        # handler other
    },
    'loggers': {
        'spider': {
            # 既有 console Handler，还有 file Handler
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    }
}

dictConfig(LOG_CONFIG)


def setup_logger(name, log_file=None, level=logging.INFO, propagate=False):
    """Function setup as many loggers as you want"""
    if not log_file:
        log_file = name + '.log'

    # 设置 logger handler 及每个 handler 处理的最低日志级别
    formatter = logging.Formatter('%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] \ '
                                  ' [%(levelname)s]- %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.DEBUG)
    file_handler = RotatingFileHandler(os.path.join(PROJECT_ROOT, 'logs', log_file), maxBytes=50 * 1024 * 1024,
                                       backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    # 生成 logger 并加入 handlers 以及 logger 处理的最低日志级别
    logger = logging.getLogger(name)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = propagate

    return logger


# test debug
test_logger = setup_logger('test')
# 接口 log
api_logger = setup_logger('api', level=logging.ERROR)
