#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/27 23:35
"""
from app import create_app
from app.exceptions.error_handle import error_handle

app = create_app()


# 全局异常处理
@app.errorhandler(Exception)
def framework_error(e):
    return error_handle(e, app)


if __name__ == '__main__':
    app.run(
        debug=app.config.get('DEBUG', False)
    )
