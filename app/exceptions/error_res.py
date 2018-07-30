# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/31 01:22
"""
from app.exceptions.base import APIException


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
