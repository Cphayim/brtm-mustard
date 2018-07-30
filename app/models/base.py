# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/31 03:54
"""
from contextlib import contextmanager
from datetime import date, datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, DateTime, Boolean

from app.exceptions.error_res import NotFound


class SQLAlchemy(_SQLAlchemy):
    """
    继承原 SQLAlchemy 类，实现 auto_commit 上下文管理器
    """

    @contextmanager
    def auto_commit(self):
        """
        自动执行提交的上下文管理器
        :return:
        """
        try:
            # 开始事务
            yield
            # with 块执行完毕自动 commit
            self.session.commit()
            pass
        except Exception as e:
            # 若出现异常，执行回滚
            self.session.rollback()
            raise e


class Query(BaseQuery):

    def filter_by(self, **kwargs):
        """
        重写 filter_by
        默认查询未被标记删除的数据
        :param kwargs:
        :return:
        """
        if 'del_flag' not in kwargs.keys():
            kwargs['del_f'] = False

        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        """
        重写 get_or_404
        :param ident: 主键
        :return:
        """
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self):
        """
        重写 first_or_404
        :return:
        """
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


# 初始化 SQLAlchemy，指定自定义的 Query 类
db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    """
    模型基类
    """
    __abstract__ = True

    """通用字段"""
    # ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 创建时间
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    # 逻辑删除标记
    del_f = Column(Boolean, nullable=False, default=False)

    def set_attrs(self, attrs_dict):
        """
        动态为对象设置属性
        传入一个字典，将与字典中有同名的 key 的值赋给对象的属性
        :param attrs_dict:
        :return:
        """
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def keys(self):
        """
        获取需要被转为 json 的字段名列表
        :return:
        """
        return getattr(self, 'fields', [])

    def hide(self, *keys):
        """ 隐藏部分字段的显示（仅影响 keys 中返回的字段名）"""
        for key in keys:
            self.fields.remove(key)

    def show(self, *keys):
        """ 添加部分字段的显示（仅影响 keys 中返回的字段名）"""
        for key in keys:
            self.fields.add(key)

    def delete(self):
        """
        逻辑删除这条记录
        :return:
        """
        self.del_f = True
   