# Django settings for dojo project.
import os

DEBUG = True
LOGIN_REDIRECT_URL = '/'
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
ENABLE_DEDUPLICATION = False
ENABLE_JIRA = False
# True will display S0, S1, S2, ect in most places
# False will display Critical, High, Medium, etc
S_FINDING_SEVERITY_NAMING = False
URL_PREFIX = ''

# Uncomment this line if you enable SSL
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

ADMINS = (
    ('Your Name', 'your.name@yourdomain')
)

MANAGERS = ADMINS

DOJO_ROOT = 'DOJODIR'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2',
        # 'mysql','sqlite3' or 'oracle'.
        'NAME': 'MYSQLDB',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'MYSQLUSER',
        'PASSWORD': 'MYSQLPWD',
        'HOST': 'MYSQLHOST',  # Empty for localhost through domain sockets
        # or '127.0.0.1' for localhost through TCP.
        'PORT': 'MYSQLPORT',  # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = 'DOJO_MEDIA_ROOT'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = "DOJO_STATIC_ROOT"

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

FILE_UPLOAD_HANDLERS = ("django.core.files.uploadhandler.TemporaryFileUploadHandler",)

# where should bower install components
# collect static will move them to the static root
BOWER_COMPONENTS_ROOT = 'BOWERDIR'

# what components should be installed
BOWER_INSTALLED_APPS = (
    'fontawesome',
    'https://github.com/BlackrockDigital/startbootstrap-sb-admin-2.git',
    'fullcalendar',
    'jquery-cookie',
    'jquery-ui',
    'jquery-highlight',
    # directly from github since no bower comp available
    'https://github.com/jumjum123/JUMFlot.git',
    'https://github.com/markrcote/flot-axislabels.git',
    'chosen',
    'chosen-bootstrap',
    'bootswatch-dist#readable',
    'bootstrap-wysiwyg-steveathon',
    'justgage'
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'DOJOSECRET'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dojo.middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'dojo.urls'
LOGIN_URL = '/login'
LOGIN_EXEMPT_URLS = (
    r'^%sstatic/' % URL_PREFIX,
    r'^%swebhook/' % URL_PREFIX,
    r'^%smetrics/all$' % URL_PREFIX,
    r'^%smetrics$' % URL_PREFIX,
    r'^%smetrics/product/type/(?P<mtype>\d+)$' % URL_PREFIX,
    r'^%smetrics/simple$' % URL_PREFIX,
    r'^%sapi/v1/' % URL_PREFIX,
    r'^%sajax/v1/' % URL_PREFIX,
    r'^%sreports/cover$' % URL_PREFIX,
    r'^%sfinding/image/(?P<token>[^/]+)$' % URL_PREFIX
)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'dojo.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polymorphic',  # provides admin templates
    'overextends',
    'django.contrib.admin',
    'django.contrib.humanize',
    'gunicorn',
    'tastypie',
    'djangobower',
    'auditlog',
    'dojo',
    'tastypie_swagger',
    'watson',
    'tagging',
    'custom_field',
    'imagekit',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtpout.your_domain.com'
EMAIL_PORT = '25'
EMAIL_USE_TLS = True

PORT_SCAN_CONTACT_EMAIL = 'email@your_host'
PORT_SCAN_RESULT_EMAIL_FROM = 'email@your_host'
PORT_SCAN_EXTERNAL_UNIT_EMAIL_LIST = ['email@your_host']
PORT_SCAN_SOURCE_IP = '127.0.0.1'

# Used in a few places to prefix page headings and in email
# salutations
TEAM_NAME = 'Security Engineering'

# Celery settings
BROKER_URL = 'sqla+sqlite:///dojo.celerydb.sqlite'
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERY_IGNORE_RESULT = True
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_RESULT_EXPIRES = 86400
CELERYBEAT_SCHEDULE_FILENAME = DOJO_ROOT + '/dojo.celery.beat.db'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

# wkhtmltopdf settings
WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'

# django-tagging settings
FORCE_LOWERCASE_TAGS = True
MAX_TAG_LENGTH = 25

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)d] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(funcName)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
