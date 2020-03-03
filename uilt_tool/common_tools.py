#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-23 14:53
# @Author  : 598020642@qq.com
# @Site    :
# @File    : common_tools.py
# @Software: PyCharm
from http.client import HTTPException


class ExceptionList:

    @HTTPException
    def http_exception(self):
        """
        网络请求情况集合
        """
        pass

    @OSError
    def io_exception(self):
        """
        io情况集合
        """
        pass

    @Exception
    def common_exception(self):
        """
        通用情况集合
        """
        pass


def start():
    """
    测试
    """
    pass


if __name__ == '__main__':
    start()
