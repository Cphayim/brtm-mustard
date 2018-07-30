# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/27 23:41
"""
from datetime import date

from flask.json import JSONEncoder as _JSONEncoder
from flask import Flask as _Flask

from app.libs.error import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(0, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
