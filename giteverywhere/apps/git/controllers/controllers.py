from pyramid.view import view_config

from ..models import (
    DBSession,
    #include your models here
)

from ..lib.repository import get_commit_log
from ..lib.repository import get_branch_view
from ..lib.repository import get_current_branch

from .. import APP_NAME, PROJECT_NAME, APP_BASE


@view_config(route_name=APP_NAME+'.home', renderer='%s:templates/list.mako' % APP_BASE)
def my_view(request):
    return {'APP_BASE': APP_BASE}


@view_config(route_name=APP_NAME+'.log', renderer='%s:templates/log.mako' % APP_BASE)
def log_view(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    # repository_path = '/MyWork/Projects/eims-dev'
    repository_path = '/home/bint-e-shafiq/gt'
    repository_name = "EIMS"
   
    commit_log = get_commit_log(repository_path)
    return {'APP_BASE': APP_BASE,
            'repository_path': repository_path,
            'repository_name': repository_name,
            'commit_log': commit_log}
            
            
            
            
@view_config(route_name=APP_NAME+'.branch', renderer='%s:templates/branch.mako' % APP_BASE)
def branch_log(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    # repository_path = '/MyWork/Projects/eims-dev'
    repository_path = '/home/bint-e-shafiq/giteverywhere'
    repository_name = "giteverywhere"
   
    branch_view = get_branch_view(repository_path)
    return {'APP_BASE': APP_BASE,
            'repository_path': repository_path,
            'repository_name': repository_name,
            'branch_view': branch_view}

            
            
@view_config(route_name=APP_NAME+'.cbranch', renderer='%s:templates/c_branch.mako' % APP_BASE)
def current_branch(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    # repository_path = '/MyWork/Projects/eims-dev'
    repository_path = '/home/bint-e-shafiq/giteverywhere'
    repository_name = "giteverywhere"
   
    branch_view = get_current_branch(repository_path)
    return {'APP_BASE': APP_BASE,
            'repository_path': repository_path,
            'repository_name': repository_name,
            'branch_view': branch_view}
