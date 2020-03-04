#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-19 17:12
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : weibo_script.py.py
# @Software: PyCharm
from channel_script.base_rebot import BaseReboot


class WeiBoRobot(BaseReboot):
    """
    微博爬虫
    """
    def __init__(self):
        # 主页面url
        self.home_url = 'https://weibo.com/'
        # TODO
        # 头条新闻
        # self.new_url = 'https://weibo.com/?category=1760'
        # 搜索url
        self.search = 'https://s.weibo.com/weibo?'

    def get_the_info(self):
        """
        获取关键词相关信息
        """
