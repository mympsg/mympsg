import os

defaultdb = DATABASES['default']
for key in ('USER', 'PASSWORD', 'HOST', 'PORT'):
    defaultdb[key] = os.environ['OPENSHIFT_POSTGRESQL_DB_' + key]
