# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/31 01:22
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


class Success(APIException):
    """
    提交(POST/PUT)成功
    """
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    """
    删除(DELETE)成功
    """
    # 这里不使用标准 RESTFul 中规定的 204 状态码，因为 204 状态码不会携带任何响应体
    # 为便于前端判断，这里使用 code 为 202，error_code 为 1 表示删除成功
    code = 202
    error_code = 1


class ParameterException(APIException):
    """
    参数错误
    """
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class Duplicate(ParameterException):
    """
    重复提交
    """
    msg = 'duplicate information'
    error_code = 2001


class AuthFailed(APIException):
    """
    授权失败
    """
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class Forbidden(APIException):
    """
    拒绝访问（权限不够）
    """
    code = 403
    msg = 'forbidden, not in scope'
    error_code = 1004


class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found 0__0...'
    error_code = 1001


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999
