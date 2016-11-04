# coding=utf-8
from .base import *

DEBUG = True

SECRET_KEY = 'c!^iyuxfdo8d14kza)r3!ymoja7=^%fp(rlq)#ej)ml8fju%=9'

ALLOWED_HOSTS = [
    '.duapp.com',
]

# 文件上传
# 修改上传时文件在内存中可以存放的最大size为10m
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760

# # sae的本地文件系统是只读的，修改django的file storage backend为Storage
# DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'
# 使用media这个bucket
STORAGE_BUCKET_NAME = 'media'

# 发送邮件
ADMINS = (
    ('PeterHo', 'peterho1024@gmail.com'),
)

# 数据库配置
# TODO 正式发布后改为mysql方式
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'gsLwdofEwAWxQrmzGxfH',
#         'USER': "d57a784e853f43a7aae49221d60afc91",
#         'PASSWORD': "eeb61d122e634cf1870b3ba5fa5e5af2",
#         'HOST': "sqld.duapp.com",
#         'PORT': 4050,
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': const.CACHE_ADDR,
#         'TIMEOUT': 60,
#     }
# }

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

bae_ak = "d57a784e853f43a7aae49221d60afc91"
bae_sk = "eeb61d122e634cf1870b3ba5fa5e5af2"
