import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') or 'UNSAFE_DEFAULT'
TIME_ZONE = os.environ.get('TIME_ZONE') or 'Europe/London'

LOG_RENDERING_PERFORMANCE = True
LOG_CACHE_PERFORMANCE = True
LOG_METRIC_ACCESS = True

if 'MEMCACHE_HOSTS' in os.environ:
    MEMCACHE_HOSTS = os.environ['MEMCACHE_HOSTS'].split(',')

GRAPHITE_ROOT = '/usr/share/graphite-web'
CONF_DIR = '/etc/graphite'
STORAGE_DIR = '/var/lib/graphite/whisper'
CONTENT_DIR = '/usr/share/graphite-web/static'
WHISPER_DIR = '/var/lib/graphite/whisper'
LOG_DIR = '/var/log/graphite'
INDEX_FILE = '/var/lib/graphite/search_index'  # Search index file

DATABASES = {
    'default': {
        'NAME': '/var/lib/graphite/graphite.db',
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}
