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
