#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-17 21:53
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : login_manger.py
# @Software: PyCharm
import requests


class LoginManger():
    """
    主要登陆管理模块
    """

    def __init__(self):
        pass


class APIManger():

    header_data = {

    }
    """
    接口管理
    """
    def __init__(self, set_connection='keep-alive'):
        self.se_session = None
        self.header_data['Connection'] = set_connection
        pass

    def _init_request(self):
        """
        初始化请求
        :return:
        """
        pass

    def _init_session(self):
        """
        初始化会话请求
        :return:
        """
        self.se_session = requests.session()
        pass


class SplinterManger():
    """
    自动化管理
    """
    def __init__(self):
        pass
