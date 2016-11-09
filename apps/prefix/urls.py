# coding=utf-8

from django.conf.urls import url

from . import views

__author__ = 'peter'

urlpatterns = [
    url(r'^$', views.list, name='all'),
    url(r'^list/(?P<letter>[a-z]+)/$', views.list, name='list'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^prefixJSON/(?P<id>\d+)/$', views.prefixJSON, name='prefixJSON'),
    url(r'^prefixes/$', views.prefixesJSON, name='prefixesJSON'),
    url(r'^template/meaning/$', views.meaningTemplate, name='meaningTemplate'),
    url(r'^template/word/$', views.wordTemplate, name='wordTemplate'),
]
