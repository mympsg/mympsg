import os

defaultdb = DATABASES['default']
openshift_keys = (
    ('USER', 'USERNAME'),
    ('PASSWORD', 'PASSWORD'),
    ('HOST', 'HOST'),
    ('PORT', 'PORT'),
)
for key, destkey in openshift_keys:
    defaultdb[key] = os.environ['OPENSHIFT_POSTGRESQL_DB_' + destkey]

PIPELINE_SASS_BINARY = os.path.join(os.environ['OPENSHIFT_DATA_DIR'],
                                    'opt', 'sass', 'bin', 'sass')
PIPELINE_YUI_BINARY = os.path.join(os.path.dirname(__file__),
                                   'bin', 'yui-compressor')
