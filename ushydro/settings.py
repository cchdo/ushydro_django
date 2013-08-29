import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# Django settings for ushydro project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
        # ('Your Name', 'your_email@example.com'),
        )

MANAGERS = ADMINS

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'ushydro_django',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
            }
        }

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

LANGUAGES = [
        ('en', 'English'),
        ]

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
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

CMS_PAGE_MEDIA_PATH = 'cms_page_media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "static_root")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(PROJECT_PATH, 'static'),
        )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
        )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'hx03f-a5&6$^6_l$wzc_ymo69x71er4dpqkfy)&5z*n(=sq*72'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        #     'django.template.loaders.eggs.Loader',
        )

# Requiered for django cms
TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'cms.context_processors.media',
        'sekizai.context_processors.sekizai',
        )

MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'cms.middleware.page.CurrentPageMiddleware',
        'cms.middleware.user.CurrentUserMiddleware',
        'cms.middleware.toolbar.ToolbarMiddleware',
        'cms.middleware.language.LanguageCookieMiddleware',
        )

ROOT_URLCONF = 'ushydro.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ushydro.wsgi.application'

TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(PROJECT_PATH, "templates"),
        )


INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
        'hydrotable',
        'bibliography',
        'smart_load_tag',
        'cms',
        'mptt',
        'menus',
        'south',
        'sekizai',
        'cms.plugins.text',
        'cms.plugins.link',
        'filer',
        'easy_thumbnails',
        'cmsplugin_filer_image',
        'cmsplugin_blog',
        'djangocms_utils',
        'simple_translation',
        'tagging',
        'missing',
        'sorl.thumbnail',
        'imagestore',
        'imagestore.imagestore_cms',
        )

JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'
THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        #'easy_thumbnails.processors.scale_and_crop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
        )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
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

### CMS Config Stuff Here
CMS_PERMISSION = True

CMS_TEMPLATES = (
        ('home_page.html', 'Home Page'),
        ('template_2.html', 'Template Two'),
        )

CMS_PLACEHOLDER_CONF = {
        'home_page.html left_main_image':{
            'plugins': ('FilerImagePlugin',),
            'name': 'Main Left Image',
            'limits': {
                'global': 1,
                },
            },
        'home_page.html right_upper_left':{
            'plugins': ('FilerImagePlugin',),
            'name': 'Right Upper Left Image',
            'limits': {
                'global': 1,
                },
            },
        'home_page.html right_upper_right':{
            'plugins': ('FilerImagePlugin',),
            'name': 'Right Upper Right Image',
            'limits': {
                'global': 1,
                },
            },
        'home_page.html right_lower_left':{
            'plugins': ('FilerImagePlugin',),
            'name': 'Right Lower Left Image',
            'limits': {
                'global': 1,
                },
            },
        'home_page.html right_lower_right':{
            'plugins': ('FilerImagePlugin',),
            'name': 'Right Lower Right Image',
            'limits': {
                'global': 1,
                },
            },
        }

IMAGESTORE_SHOW_USER = False
THUMBNAIL_DEBUG = True
