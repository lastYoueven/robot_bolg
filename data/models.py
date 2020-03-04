#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-20 15:03
# @Author  : 598020642@qq.com
# @Site    : 
# @File    : models.py
# @Software: PyCharm
import datetime
import uuid

from flask_mongoengine import Document
from mongoengine import (
    ObjectIdField,
    StringField,
    DateTimeField,
    DictField,
    IntField,
    FloatField,
    BooleanField,
    ListField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    EmbeddedDocumentListField
)


class AccountCookies(Document):
    """
    账号 cookies 储存模型

    @DateTime :  2019-08-16 16:09
    """
    channel = IntField(required=True, choices=CHANNEL_CHOICE, verbose_name="平台")
    landlord_id = StringField(required=True, verbose_name='房东 ID')
    username = StringField(required=True, verbose_name='账号')
    cookies = StringField(verbose_name="cookies 值")
    status = StringField(verbose_name="cookies 状态", default='valid')
    update_time = DateTimeField(default=datetime.datetime.now, verbose_name="更新时间")
    create_time = DateTimeField(default=datetime.datetime.now, verbose_name="创建时间")
    newest = BooleanField(verbose_name="是否为最新的数据标记", default=True)

    def save(self, *args, **kwargs):
        self.update_time = datetime.datetime.now()
        return super(AccountCookies, self).save(*args, **kwargs)

    meta = {
        'strict': False,
        'db_alias': 'comprehensive_db',
        'indexes': [
            'username',
            'channel',
            'status',
            'newest',
            '-create_time',
        ],
        'index_background': True,
    }

    def to_dict(self):
        return {
            'channel': self.channel,
            'landlord_id': self.landlord_id,
            'username': self.username,
            'status': self.status,
            'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')
        }

    # 更新cookie状态
    def update_cookie_status(self):
        # 修改cookie状态
        self.status = "invalid"
        self.save()


class OriginData(Document):
    """
    原始数据
    """
    url = StringField(required=True, verbose_name='原始数据来源')
    data_str = StringField(default='', verbose_name='数据来源内容')
    data_uuid = StringField(required=True, verbose_name='数据来源id')
    create_time = DateTimeField(default=datetime.datetime.now, verbose_name="创建时间")

    meta = {
        'strict': False,
        'db_alias': 'comprehensive_db',
        'indexes': [
            'url',
            'data_str',
            'data_uuid',
            '-create_time',
        ],
        'index_background': True,
    }

    def save(self, *args, **kwargs):
        return super(OriginData, self).save(*args, **kwargs)

    def to_dict(self):
        return {
            'url': self.url,
            'data_str': self.data_str,
            'data_uuid': self.data_uuid,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        }


class OriginKeyData(Document):
    """
    网络来源的原始数据
    """

    the_key = StringField(required=True, verbose_name='数据来源关键词')
    data_uuid = StringField(default=uuid.uuid4(), verbose_name='数据来源关键词')
    data_str = StringField(default=uuid.uuid4(), verbose_name='数据来源内容')
    status = StringField(verbose_name="关键词状态", default='valid')
    create_time = DateTimeField(required=True, verbose_name='数据创建时间')
    update_time = DateTimeField(default=datetime.datetime.now, verbose_name="更新时间")

    meta = {
        'strict': False,
        'db_alias': 'comprehensive_db',
        'indexes': [
            'the_key',
            'data_uuid',
            'status',
            '-create_time',
        ],
        'index_background': True,
    }

    def to_dict(self):
        return {
            'the_key': self.the_key,
            'data_uuid': self.data_uuid,
            'data_str': self.data_str,
            'status': self.status,
            'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')
        }

    def save(self, *args, **kwargs):
        self.update_time = datetime.datetime.now()
        return super(OriginKeyData, self).save(*args, **kwargs)