import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '6i4fx=5ex$t)t+5^wm7yhgcv01)6mai87+d%j66u(9&j(ny13u'
DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

#################  CELERY  ########################

BROKER_BACKEND = "redis"
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_DEFAULT_QUEUE = 'default'
# CELERY_CONCURRENCY = 2
# CELERY_MAX_TASKS_PER_CHILD = 4
# CELERY_PREFETCH_MULTIPLIER = 1

from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    # http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
    'add-every-1-min': {
        'task': 'core.tasks.task_number4',
        'schedule': crontab(),
        # or
        # 'schedule': crontab(minute='*/1', hour='*'),
        # or
        # 'schedule': 60.0,
        'args': []
    },
    'add-every-day': {
        'task': 'core.tasks.task_number4',
        'schedule': crontab(minute=0, hour=0),
        'args': []
    },
}

from kombu import Exchange, Queue
CELERY_QUEUES = (
    Queue('high',
          Exchange('high', ),
          routing_key='high'
          ),
    Queue('default',
          Exchange('default', ),
          routing_key='default'
          ),

    Queue('low',
          Exchange('low', ),
          routing_key='low'
          ),

)

