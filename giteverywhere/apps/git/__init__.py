from apps import PROJECT_NAME,project_package
#from .. import PROJECT_NAME, project_package

APP_NAME = 'git'
APP_BASE = '%s.apps.%s' % (PROJECT_NAME, APP_NAME)

from routes import application_routes


