#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-23 14:53
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : weixin_manger.py
# @Software: PyCharm
from wxpy import Bot
import queue


class WXManger():

    def __init__(self):
        # 登陆队列
        self.login_queue = queue.Queue()

    def new_login(self):
        """
        实例化登陆对象
        :return:
        """
        bot = Bot()


def test():
    bot = Bot()
    # 向文件传输助手发送消息
    bot.file_helper.send('Hello from wxpy!')

def run():
    pass

if __name__ == '__main__':
    test()