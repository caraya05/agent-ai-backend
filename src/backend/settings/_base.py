import os  # pylint:disable=C0114
import environ
from django.utils.translation import gettext_lazy as _

root = environ.Path(__file__) - 3
env = environ.Env()

if os.path.exists(os.path.join(root, '.env')):
    env.read_env(os.path.join(root, '.env'))

# Application definition
DJANGO_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modeltranslation',
]

THIRD_PARTY_APPS = [
    'solo',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'django_filters',
    'geoposition',
    'django_celery_beat',
    'django_celery_results',
    'rangefilter',
    'mptt',
    'corsheaders',
    'import_export',
    'hijack',
    'compat',
    'storages',
    'defender',
    'loducode_utils',
]

LOCAL_APPS = [
    'configurations',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'crum.CurrentRequestUserMiddleware',
    'defender.middleware.FailedLoginMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {  # Adding this section should work around the issue.
                'staticfiles': 'django.templatetags.static',
            },
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = str(root) + '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = str(root) + '/media/'

# REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    # "DATE_FORMAT": "%d/%m/%Y",
    # "DATETIME_FORMAT": "%d/%m/%Y %H:%M:%S",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'EXCEPTION_HANDLER': 'loducode_utils.views_api.handler500',
}

LOCALE_PATHS = [
    str(root) + '/locale/',
]

LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English')),
]

GEOPOSITION_GOOGLE_MAPS_API_KEY = env('GEOPOSITION_GOOGLE_MAPS_API_KEY', default='test')
GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'maxZoom': 15,
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

HIJACK_LOGIN_REDIRECT_URL = '/'  # Where admins are redirected to after hijacking a user
# Where admins are redirected to after releasing a user
HIJACK_LOGOUT_REDIRECT_URL = '/admin/auth/user/'

X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CELERY SETTINGS
CELERY_BROKER_URL = 'redis://{}:{}'.format(env('REDIS_HOST', default='redis'),
                                           env('REDIS_PORT', default='6379'))  # pylint:disable=C0301
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Bogota'
CELERY_RESULT_BACKEND = 'django-db'

# Defender settings
DEFENDER_REDIS_URL = 'redis://{}:{}/0'.format(env('REDIS_HOST', default='redis'),
                                              env('REDIS_PORT', default='6379'))
# DEFENDER_BEHIND_REVERSE_PROXY = True
DEFENDER_LOCK_OUT_BY_IP_AND_USERNAME = True
# DEFENDER_LOCKOUT_URL = '/lock'
