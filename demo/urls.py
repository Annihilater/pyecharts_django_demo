#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2020/4/17 6:01 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : urls.py


# demo/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bar/$', views.ChartView.as_view(), name='demo'),
    url(r'^index/$', views.IndexView.as_view(), name='demo'),
]
