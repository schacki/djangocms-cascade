ROOT_URLCONF = 'testurls'
SECRET_KEY = 'test'

SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

STATIC_URL = '/static/'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'django.core.context_processors.i18n',
            'django.core.context_processors.debug',
            'django.core.context_processors.request',
            'django.core.context_processors.media',
            'django.core.context_processors.csrf',
            'django.core.context_processors.tz',
            'sekizai.context_processors.sekizai',
            'django.core.context_processors.static',
            'cms.context_processors.cms_settings'
        ],
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.eggs.Loader'
        ],
    },
}]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.admin',
    'jsonfield',
    'reversion',
    'filer',
    'easy_thumbnails',
    'treebeard',
    'menus',
    'sekizai',
    'cms',
    'djangocms_text_ckeditor',
    'cmsplugin_cascade',
    'cmsplugin_cascade.extra_fields',
    'cmsplugin_cascade.sharable',
]
LANGUAGES = (
    ('en', 'English'),
)
LANGUAGE_CODE = 'en'
CMS_TEMPLATES = (
    ('testing.html', 'Default Page'),
)
CMSPLUGIN_CASCADE_PLUGINS = (
    'cmsplugin_cascade.link',
    'cmsplugin_cascade.bootstrap3',
)
CMSPLUGIN_CASCADE = {
    'plugins_with_extra_fields': [
        'BootstrapButtonPlugin', 'BootstrapContainerPlugin',
        'BootstrapColumnPlugin', 'BootstrapRowPlugin',
        'BootstrapPicturePlugin', 'SimpleWrapperPlugin',
    ],
    'plugins_with_sharables': {
        'BootstrapImagePlugin': (
            'image-shapes',
            'image-width-responsive',
            'image-width-fixed',
            'image-height',
            'resize-options',
        ),
        'BootstrapPicturePlugin': (
            'image-shapes',
            'responsive-heights',
            'image-size',
            'resize-options',
        ),
        'BootstrapButtonPlugin': ('link',),
        'TextLinkPlugin': ('link', 'target',),
    },
}

CMS_PLACEHOLDER_CONF = {
    'Main Content Container': {
        'plugins': ['BootstrapContainerPlugin'],
    },
    'Bootstrap Column': {
        'plugins': ['BootstrapRowPlugin', 'TextPlugin'],
        'parent_classes': {'BootstrapRowPlugin': []},
        'require_parent': False,
        'glossary': {
            'breakpoints': ['xs', 'sm', 'md', 'lg'],
            'container_max_widths': {
                'xs': 750,
                'sm': 750,
                'md': 970,
                'lg': 1170
            },
            'fluid': False,
            'media_queries': {
                'xs': ['(max-width: 768px)'],
                'sm': ['(min-width: 768px)', '(max-width: 992px)'],
                'md': ['(min-width: 992px)', '(max-width: 1200px)'],
                'lg': ['(min-width: 1200px)'],
            },
        },
    },
}
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
THUMBNAIL_PRESERVE_EXTENSIONS = True,
THUMBNAIL_OPTIMIZE_COMMAND = {
    'png': '/opt/local/bin/optipng {filename}',
    'gif': '/opt/local/bin/optipng {filename}',
    'jpeg': '/opt/local/bin/jpegoptim {filename}',
}
