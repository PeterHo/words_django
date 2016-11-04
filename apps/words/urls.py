# coding=utf-8

from django.conf.urls import url

from . import views

__author__ = 'peter'

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
