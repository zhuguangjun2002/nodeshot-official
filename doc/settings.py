# -*- coding: utf-8 -*-

import os


# ------ BEGIN DON'T TOUCH AREA ------ #

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = 'g_gi_2a71(9928rb011m!-_3f91kjw)w4@)$^!-1^z-=b3)*6u'

ROOT_URLCONF = 'dev.urls' #

WSGI_APPLICATION = 'dev.wsgi.application'

# ------ END DON'T TOUCH AREA ------ #


DEBUG = True
DOMAIN = 'localhost'
SUBDIR = '/'  # edit this line if you are installing in a sub directory, like /nodeshot
SITE_NAME = 'dev'  # site name, you can change this

# 使用中文名字，会在`发送邮件`时，报编码错误。
#为了简化处理，我们使用英文名称,暂不采用中文名称。
#SITE_NAME = '中国移动设备管理平台'  # site name, you can change this

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'nodeshot_italy',
        'USER': 'nodeshot',
        'PASSWORD': 'nodeshot',
        'HOST': '127.0.0.1',
        'PORT': '',
    },
    # Import data from older versions
    # More info about this feature here: http://nodeshot.readthedocs.org/en/latest/topics/oldimporter.html
    #'old_nodeshot': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'nodeshot',
    #    'USER': 'user',
    #    'PASSWORD': 'password',
    #    'OPTIONS': {
    #           "init_command": "SET storage_engine=INNODB",
    #    },
    #    'HOST': '',
    #    'PORT': '',
    #}
}

#POSTGIS_VERSION = (2, 1)
#我们在ubuntu16.04上，实际使用的postgis版本为2.4.
POSTGIS_VERSION = (2, 4)

# sentry integration
#RAVEN_CONFIG = {
#    'dsn': 'https://<api-public-key>:<api-secret-key>@<sentry.host>/<id>?timeout=5&verify_ssl=0',
#}

# import the default nodeshot settings
# do not move this import
from nodeshot.conf.settings import *


# ------ All settings customizations must go here ------ #


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
#TIME_ZONE = 'Europe/Amsterdam'
# 使用`上海时区`
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-gb'
# 简体中文
# django1.8,使用`zh-cn`,或者`zh-Hans`
LANGUAGE_CODE = 'zh-cn'
# `zh-Hans` also work well
# you need create a directory in `locale`,called `zh_Hans`
#LANGUAGE_CODE = 'zh-Hans'

## `语言选项`-`LANGUAGE`
#如果什么也不加，那么就会是`所有的语言`都支持，
#只要其被翻译了，`locale`文件夹下,有其对应的`目录`即可。

# 添加`语言选项`
# 只支持: 中文简体,英文，
# 不支持: 意大利文，西班牙文，加泰罗尼亚文
LANGUAGES = (
    ('zh-cn', 'Chinese Simplified'),
    ('en', 'English'),
)

# 添加`语言选项`
# 支持: 中文简体,英文，意大利文，西班牙文，加泰罗尼亚文
# LANGUAGES = (
    # ('zh-cn', 'Chinese Simplified'),
    # ('en', 'English'),
    # ('es', 'Spanish'),
    # ('de', 'Germany'),
    # ('ca', 'Catalan'),
    # ('it', 'Italy'),
# )

# 表明我们的 locale 文件默认会放在 app 目录中的 locale 目录下
# 注释掉，实际测试，不需要，默认就是会搜索`app`下面的目录。
# LOCALE_PATHS = (
    # 'locale',
# )


ADMINS = (
    #('Your name', 'your@email.com'),
)

MANAGERS = ADMINS

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'root@localhost'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER  # used for error reporting
EMAIL_SUBJECT_PREFIX = '[Nodeshot] '

# LEAFLET_CONFIG.update({
    # 'DEFAULT_CENTER': (49.06775, 30.62011),
    # 'DEFAULT_ZOOM': 4,
    # 'MIN_ZOOM': 1,
    # 'MAX_ZOOM': 18,
    # # Uncomment to customize map tiles
    # # More information here: https://github.com/makinacorpus/django-leaflet#default-tiles-layer
    # #'TILES': [
    # #    ('Map', 'https://a.tile.openstreetmap.org/{z}/{x}/{y}.png', '&copy; <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> contributors | Tiles Courtesy of <a href="http://www.mapquest.com/" target="_blank">MapQuest</a> &nbsp;<img src="https://developer.mapquest.com/content/osm/mq_logo.png">'),
    # #    ('Satellite', 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', 'Source: <a href="http://www.esri.com/">Esri</a> &copy; and the GIS User Community ')
    # #],
# })

LEAFLET_CONFIG.update({
    'DEFAULT_CENTER': (37.5335,121.3920), # yantai
    #'SPATIAL_EXTENT': (119.5582,36.5732, 121.9295,38.4022),
    'DEFAULT_ZOOM': 8,
    'MAX_ZOOM': 20,
    'MIN_ZOOM':3,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': '烟台麦卡托信息技术有限公司 © Maikator Co., Ltd. 2018',
    'TILES': [('开放街道地图','https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{}),
              ('Mapbox街道地图', 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', 
                    {'id': 'mapbox.streets',
                     'maxZoom': '18',
                     'accessToken': 'pk.eyJ1Ijoiemh1Z3VhbmdqdW4yMDAyIiwiYSI6ImNqYzFkNGl2ZjAwa2oyeW4yMGh0cTAxcHAifQ.bbY8ctOlYyb77S4P0VZ25A'
                    }
              ),
              ('Mapbox卫星影像','https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}',
                   {'id': 'mapbox.satellite',
                    'maxZoom':'18',
                    'accessToken':'pk.eyJ1Ijoiemh1Z3VhbmdqdW4yMDAyIiwiYSI6ImNqYzFkNGl2ZjAwa2oyeW4yMGh0cTAxcHAifQ.bbY8ctOlYyb77S4P0VZ25A'
                   }
              ),
    ],
})


# social auth
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

# Uncomment this section to enable periodic tasks
#
#from datetime import timedelta
#
#CELERYBEAT_SCHEDULE.update({
#    'synchronize': {
#        'task': 'nodeshot.interop.sync.tasks.synchronize_external_layers',
#        'schedule': timedelta(hours=12),
#    },
#    # example of how to synchronize one of the layers with a different periodicity
#    'synchronize': {
#        'task': 'nodeshot.interop.sync.tasks.synchronize_external_layers',
#        'schedule': timedelta(minutes=30),
#        'args': ('layer_slug',)
#    },
#    # example of how to synchronize all layers except two layers
#    'synchronize': {
#        'task': 'nodeshot.interop.sync.tasks.synchronize_external_layers',
#        'schedule': timedelta(hours=12),
#        'kwargs': { 'exclude': 'layer1-slug,layer2-slug' }
#    }
#})
