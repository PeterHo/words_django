# coding=utf-8
import os

__author__ = 'peter'

# 判断需要载入哪种配置
if 'SERVER_SOFTWARE' in os.environ:
    from .production import *
else:
    from .local import *
