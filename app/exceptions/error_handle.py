# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/31 01:56
"""
from werkzeug.exceptions import HTTPException

from app.exceptions.base import APIException
from app.exceptions.error_res import ServerError


def error_handle(e, app):
    """
    错误处理
    """
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        return APIException(code=e.code, msg=e.description, error_code=1007)
    else:
        # TODO log
        if not app.config.get('DEBUG'):
            # 非调试模式，返回概要信息
            return ServerError()
        else:
            # 调试模式，返回完整错误堆栈
            raise e
