#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-23 14:53
# @Author  : 598020642@qq.com
# @Site    : 提供附加功能
# @File    : decorator_tool.py
# @Software: PyCharm
import logging

from conf.log_setting import setup_logger

decorator_logger = setup_logger('decorator_logger', level=logging.WARNING)


def control_pyppeteer_driver():
    """
    退出pypp句柄
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:

                decorator_logger.error(f'error file:{e.__traceback__.tb_frame.f_globals["__file__"]} , '
                                                 f'error line:{e.__traceback__.tb_lineno}, error message:{e.args}')
        return wrapper
    return decorator


def test():
    pass


if __name__ == '__main__':
    test()
