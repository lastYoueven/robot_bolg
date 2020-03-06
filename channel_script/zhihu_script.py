#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-19 17:13
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : zhihu_script.py
# @Software: PyCharm
import random

from channel_script.base_rebot import BaseReboot
from conf.setting import USER_AGENT


class ZhiHuRobot(BaseReboot):
    """
    知乎爬虫
    """
    TYPE_SEARCH = 1
    TYPE_EXPLORE = 2

    def __init__(self):
        # 主页面url
        self.home_url = 'https://www.zhihu.com/explore'
        # 搜索url
        self.search_url = 'https://www.zhihu.com/search?type=content&q={}'

    def init_headers(self, type: int):
        """
        组装头部数据
        :return:
        """
        if self.TYPE_SEARCH == type:
            return {
                "upgrade-insecure-requests": "1",
                "user-agent": random.choice(USER_AGENT['pc']),
                "sec-fetch-user": "?1",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "navigate",
                "referer": self.home_url,
                "Content-Type": "text/html; charset=utf-8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                # "cookies": "_zap=897e9fa7-6d47-477c-a0ab-d701ef599db5;d_c0=\"AIBWuNar1RCPTswCFGKu6jR9xl7iOPp2Ciw=|1581997141\";q_c1=149da6b289c74c3da22f734ece79542f|1582107012000|1582107012000;tshl=;tst=r;_ga=GA1.2.1283835290.1582682629;_xsrf=f9f01311-5f22-4e45-8f94-89ece59ed2fd;_gid=GA1.2.334805483.1583120108;Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1583293944,1583379221,1583463452,1583474175;capsion_ticket=\"2|1:0|10:1583478845|14:capsion_ticket|44:NjU1NDBhMGJjODg2NDA3ZmJhMWRkMjg3YWNhOWM3NzI=|c03f4c8880068a10f6fd035e68b2801276848e7b0ae0d8bcfa49ed1f6c62a253\";Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1583478971;_gat_gtag_UA_149949619_1=1;KLBRSID=e42bab774ac0012482937540873c03cf|1583478978|1583478970"
            }

        if self.TYPE_EXPLORE == type:
            return {
                "upgrade-insecure-requests": "1",
                "user-agent": random.choice(USER_AGENT['pc']),
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "sec-fetch-site": "none",
                "sec-fetch-mode": "navigate",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8"
            }

    def get_key_info(self, explore_key: str):
        """
        获取关键词相关信息
        """
        self.robot_session = self.get_request_session()
        header_data = self.init_headers(1)
        response_data = self.robot_session.get(url=self.search_url.format(explore_key), headers=header_data)
        print(response_data.text)


if __name__ == '__main__':
    key = 'go语言'
    ZH = ZhiHuRobot()
    ZH.get_key_info(key)
