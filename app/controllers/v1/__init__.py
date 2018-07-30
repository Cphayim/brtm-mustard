# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/28 00:25
"""

from flask import Blueprint


def create_blueprint_v1():
    """
    创建 v1 蓝图
    :return:
    """
    bp_v1 = Blueprint('v1', __name__, url_prefix='/v1')
    # 注册红图
    return bp_v1