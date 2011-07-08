import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
ugettext = lambda s: s

DEBUG = False
TEMPLATE_DEBUG = DEBUG

LANGUAGES = (
    ('pt-br', ugettext('Portuguese (Brazil)')),
    ('en-us', ugettext('English (U.S.A.)')),
)

ADMINS = (
    ('Diego Maia', 'diegocmsantos@gmail.com'),
    ('Frank', 'frankcasallo@yahoo.com.br'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/var/www/frankarturo/frank.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'
USE_I18N = True


SITE_ID = 1

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static')
MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'evn-8)f=%7_q8cj7@nkk0#60b%h2o3(27sr_j&bh#4crm*mk$i'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    #~ 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'frankarturo.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.sitemaps',
    
    # thirdy-party
    'contact_form',
    'ajax_validation',
    
    'www',
    'mylovelymontreal',
    'tagging',
)

TRAC_URL = 'http://trac.montrealconsultoria.com.br/login/xmlrpc'
TRAC_USERNAME = 'django_admin'
TRAC_PASSWORD = 'django_adminq1w2e33e2w1q'
TRAC_REALM = 'montreal_trac'
TRAC_DEFAULT_CC = 'nicholas diego'
TRAC_DEFAULT_KEYWORDS = 'mylovelymontreal'
TRAC_DEFAULT_COMPONENT = 'SupportRequest'
TRAC_DEFAULT_REPORTER = 'FrankArturo'

INTERNAL_IPS = ('127.0.0.1', )

DEBUG_TOOLBAR_CONFIG  = {
    'INTERCEPT_REDIRECTS' : False,
}

try:
    from local_settings import *
except ImportError:
    pass

