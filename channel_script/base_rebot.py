#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-20 14:58
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : base_rebot.py
# @Software: PyCharm

import asyncio

import requests
from pyppeteer import launch


class BaseReboot:
    """
    请求公共爬虫
    """
    # robot运行状态 False 不需要身份（cookies），True 需要身份
    run_state = False

    def __init__(self):
        self.launch_driver = None
        self.robot_session = None

    def init_pyppeteer_driver(self):
        """
        初始化pyppeteer句柄
        """
        return await launch({
            'headless': False,  # 关闭无头模式
            'devtools': True,  # 打开 chromium 的 devtools
            # 'executablePath': 'Chromium.app/Contents/MacOS/Chromiu',
            'args': [
                '--disable-extensions',
                '--hide-scrollbars',
                '--disable-bundled-ppapi-flash',
                '--mute-audio',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-gpu',
            ],
            'dumpio': True
        })

    def init_request_session(self):
        """
        初始化pyppeteer句柄
        """
        self.robot_session = requests.session()
        return

    def login_with_cookie(self):
        """
        使用cookie进行登陆 (子用父)
        :return:
        """
        pass

    def login(self, url):
        """
        登陆获登陆信息 (子用父)
        :param url:
        :return:
        """
        pass

    def login_out(self):
        pass

