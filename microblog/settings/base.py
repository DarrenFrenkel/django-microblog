"""
Django settings for microblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

#from django.contrib import staticfiles
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
# here() gives us file paths from the root of the system to the directory
# holding the current file.
here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PROJECT_ROOT = here("..")
# root() gives us file paths from the root of the system to whatever
# folder(s) we pass it starting at the parent directory of the current file.
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ("Darren Frenkel", "darrenfrenkel@gmail.com"),		
)
MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'Australia/Melbourne'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = root("..", "..", "uploads")
MEDIA_URL = ''

STATIC_ROOT = root("..", "..", "static")
STATIC_URL = '/static/'

STATICFILES_DIRS =(
    root("..", "assets"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',	
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+iea4399%fjb@84b74zbl4=6l7chcnkq5@f1zeeu2asc+d_88%'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'microblog.urls'

WSGI_APPLICATION = 'microblog.wsgi.application'

TEMPLATE_DIRS =( 
    root("templates"),
)

MEDIA_ROOT = root("..", "uploads")

ALLOWED_HOSTS = ['localhost']


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',
)

LOCAL_APPS = (
    'blog',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false':{
            '()': 'django.utils.log.RequireDebugFalse'	
        }
    },
    'handlers': {
        'mail_admins':{
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler' 			
        }
    },
    'loggers': {
        'django.requests': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,			
        },    
	}	
}




















