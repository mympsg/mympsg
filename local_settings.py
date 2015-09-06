import os

defaultdb = DATABASES['default']
openshift_keys = (
    ('USER', 'OPENSHIFT_POSTGRESQL_DB_USERNAME'),
    ('PASSWORD', 'OPENSHIFT_POSTGRESQL_DB_PASSWORD'),
    ('HOST', 'OPENSHIFT_POSTGRESQL_DB_HOST'),
    ('PORT', 'OPENSHIFT_POSTGRESQL_DB_PORT'),
    ('NAME', 'OPENSHIFT_APP_NAME'),
)
for key, destkey in openshift_keys:
    defaultdb[key] = os.environ[destkey]

PIPELINE_SASS_BINARY = os.path.join(os.environ['OPENSHIFT_DATA_DIR'],
                                    'opt', 'sass', 'bin', 'sass')
PIPELINE_YUI_BINARY = os.path.join(os.environ['OPENSHIFT_REPO_DIR'],
                                   'bin', 'yui-compressor')

STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'],
                           'wsgi', 'static')

CACHES = {
    'default': {
        'TIMEOUT': None, # cache keys never expire; we invalidate them
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'mysite',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['MANDRILL_API_USER']
EMAIL_HOST_PASSWORD = os.environ['MANDRILL_API_KEY']
EMAIL_USE_TLS = True
