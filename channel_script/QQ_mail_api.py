#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-25 17:07
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : QQ_mail_api.py
# @Software: PyCharm
from login_manger import APIManger


class TXMailManger(object):
    """
    qq邮箱登陆
    """
    request_manger = APIManger()
    header_data = request_manger.header_data
    header_data['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) ' \
                                'AppleWebKit/537.36 (KHTML, like Gecko)' \
                                ' Chrome/77.0.3865.120 Safari/537.36'
    header_data['accept-encoding'] = 'gzip, deflate, br'
    header_data['sec-fetch-mode'] = 'navigate'
    header_data['sec-fetch-site'] = 'none'
    header_data['sec-fetch-user'] = '?1'
    header_data['upgrade-insecure-requests'] = '1'

    login_url = "https://mail.qq.com/"

    def __init__(self):
        self.handle = self.request_manger.se_session

    def _login(self):
        """
        登陆邮箱页面
        :return:
        """
        self.handle.get(url=self.login_url)


def run():
    pass


if __name__ == '__main__':
    run()