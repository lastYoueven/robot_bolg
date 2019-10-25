#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-19 17:17
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : setting.py
# @Software: PyCharm

# 站点配置
CHANNEL_SET = {
    "1000": "weibo",
    "1001": "zhihu",
    "1002": "",
    "1003": "",
    "1004": "",
    "1005": "",
}

# task 类型
TASK_TYPE = {
    "text_pub": 1,  # 知乎微信公众文章类型
    "video_pub": 2,  # 小破站视频发布类型
    "note_pub": 3  # 微博跟新
}

HEADER_CONF = {
    CHANNEL_SET["1000"]: {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "",
        "Host": "rm.api.weibo.com",
        "Referer": "https://weibo.com/u/3820855846/home?wvr=5&sudaref=www.baidu.com&retcode=6102",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    },
    CHANNEL_SET["1001"]: {

    }
}
