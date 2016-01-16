import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '----------------your-key-here-------------------------'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LANGUAGE_CODE = 'en-us'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SITE_URL = 'http://leaza.ru' # no trailing slash



SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '--------your data here--------'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '--------your data here--------'

SOCIAL_AUTH_FACEBOOK_KEY = '--------your data here--------'
SOCIAL_AUTH_FACEBOOK_SECRET = '--------your data here--------'

#
# SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_KEY = '--------your data here--------'
# SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_SECRET = '--------your data here--------'
# SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_PUBLIC_NAME = '--------your data here--------'
#
# SOCIAL_AUTH_VK_OAUTH2_KEY = '--------your data here--------'
# SOCIAL_AUTH_VK_OAUTH2_SECRET = '--------your data here--------'
#
# SOCIAL_AUTH_MAILRU_OAUTH2_KEY = '--------your data here--------'
# SOCIAL_AUTH_MAILRU_OAUTH2_SECRET = '--------your data here--------'
#
#


EMAIL_HOST = '--------your data here--------'
EMAIL_HOST_USER = '--------your data here--------'
EMAIL_HOST_PASSWORD = '--------your data here--------'
DEFAULT_FROM_EMAIL = '--------your data here--------'
SERVER_EMAIL = '--------your data here--------'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True


ADMINS = (('Your name', 'Your email'),)
MANAGERS = ADMINS