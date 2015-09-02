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
