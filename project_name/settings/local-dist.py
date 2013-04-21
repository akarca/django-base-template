"""
This is an example settings/local.py file.
These settings overrides what's in settings/base.py
"""

from . import base


INSTALLED_APPS = base.INSTALLED_APPS + ('django_nose', )
INSTALLED_APPS = base.INSTALLED_APPS + ('django_extensions',)

# Debug Toolbar
INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar', )
MIDDLEWARE_CLASSES = base.MIDDLEWARE_CLASSES + ['debug_toolbar.middleware.DebugToolbarMiddleware',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql_db_name',
        'USER': 'root',
        'PASSWORD': 'root_password',
        'HOST': '',
        'PORT': '',
        #'OPTIONS': {
        #    'init_command': 'SET storage_engine=InnoDB',
        #    'charset' : 'utf8',
        #    'use_unicode' : True,
        #},
        #'TEST_CHARSET': 'utf8',
        #'TEST_COLLATION': 'utf8_general_ci',
    },
    # 'slave': {
    #     ...
    # },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': [
            '127.0.0.1:11211',
        ]
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = THUMBNAIL_DEBUG = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True

# SECURITY WARNING: keep the secret key used in production secret!
# Hardcoded values can leak through source control. Consider loading
# the secret key from an environment variable or a file instead.
SECRET_KEY = '{{ secret_key }}'

# Uncomment these to activate and customize Celery:
# CELERY_ALWAYS_EAGER = False  # required to activate celeryd
# BROKER_HOST = 'localhost'
# BROKER_PORT = 5672
# BROKER_USER = 'django'
# BROKER_PASSWORD = 'django'
# BROKER_VHOST = 'django'
# CELERY_RESULT_BACKEND = 'amqp'

## Log settings

# Remove this configuration variable to use your custom logging configuration
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'loggers': {
        '{{ project_name }}': {
            'level': "DEBUG"
        }
    }
}

INTERNAL_IPS = ('127.0.0.1')
