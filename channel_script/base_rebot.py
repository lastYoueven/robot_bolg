#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-20 14:58
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : base_rebot.py
# @Software: PyCharm

import asyncio
from pyppeteer import launch


class BaseReboot:

    def __init__(self):
        self.my_driver = await launch({
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

    def login_with_cookie(self):
        """
        使用cookie进行登陆
        :return:
        """
        pass

    def login(self, url):
        """
        登陆获登陆信息
        :param url:
        :return:
        """


    def login_out(self):
        pass

