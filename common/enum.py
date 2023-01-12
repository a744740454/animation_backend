#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：animation_backend 
@File    ：enum.py
@Author  ：sadnesspineapple
@Date    ：2022/10/20 18:31 
'''
# built-in package
import enum

# project package

# third package


class UserRelImageActionEnum(enum.Enum):
    collect = "collect"  # 收藏
    upload = "upload"  # 上传

    @classmethod
    def get_values(cls):
        return [member.value for member in cls]

    @classmethod
    def names(cls):
        return [member.name for member in cls]

if __name__ == '__main__':
    print(*UserRelImageActionEnum.get_values())
