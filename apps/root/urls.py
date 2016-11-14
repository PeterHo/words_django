# coding=utf-8

from django.conf.urls import url

from . import views

__author__ = 'peter'

urlpatterns = [
    url(r'^$', views.list, name='all'),
    url(r'^list/$', views.list, name='list'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^rootJSON/(?P<id>\d+)/$', views.rootJSON, name='rootJSON'),
    url(r'^roots/$', views.rootsJSON, name='rootsJSON'),
]
