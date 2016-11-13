#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # 设置第三方库路径
    root = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(root, 'site-packages'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
