# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/31 02:50
"""
import json

from flask import request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    """
    APIException 基类
    """
    code = 500
    msg = 'sorry, we make a mistake (*￣︶￣)!'
    error_code = 999

    def __init__(self, code=None, msg=None, error_code=None, headers=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code

        super(APIException, self).__init__(description=msg, response=None)

    # 重写 get_body 与 get_headers 方法，返回 JSON 格式的数据
    def get_body(self, environ=None):
        body = dict(
            error_code=self.error_code,
            msg=self.msg,
            request=request.method + ' ' + self.get_url_no_param()
        )
        return json.dumps(body)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')[0]
        return main_path
