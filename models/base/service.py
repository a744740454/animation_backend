#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：animation_backend 
@File    ：service.py
@Author  ：sadnesspineapple
@Date    ：2022/9/2 13:55 
'''

# built-in package

# project package
from models import session

# third package
from sqlalchemy import desc


class BaseModel:

    def _query(self, class_name, page, page_size, order_by=True):
        """
        分页查询，默认按创建时间进行倒叙
        """
        # todo 根据传入的order_by参数直接进行规则的排序
        if order_by:
            return session.query(class_name).order_by(
                class_name.create_time.desc()).limit(page_size).offset((page - 1) * page_size)
        return session.query(class_name).limit(page_size).offset((page - 1) * page_size)
