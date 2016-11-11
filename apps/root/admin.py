# coding=utf-8
from django.contrib import admin

from .models import Root, Meaning, Word

__author__ = 'peter'

admin.site.register(Root)
admin.site.register(Meaning)
admin.site.register(Word)
