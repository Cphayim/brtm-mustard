# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/27 23:37
"""

from app.app import Flask


def create_app():
    """
    创建 app
    """
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprint(app)
    register_plugin(app)
    return app


def register_blueprint(app):
    """
    注册蓝图
    :param app: Flask
    """
    from app.controllers.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1())


def register_plugin(app):
    """
    注册插件
    :param app: Flask
    """
    pass
