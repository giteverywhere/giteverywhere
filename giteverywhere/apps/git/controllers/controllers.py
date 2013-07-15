from pyramid.view import view_config
import os
from ..models import (
    DBSession,
    #include your models here
)

from ....models import (
      Repository,
      )

from ..lib.repository import get_commit_log
from ..lib.repository import get_branch_view
from ..lib.repository import get_current_branch
from ..lib.repository import get_comit_log
from ..lib.repository import get_tag_list
from ..lib.repository import get_tag_detail
from ..lib.repository import get_commit_difference
from ..lib.repository import get_file_name
from ..lib.repository import get_file_contents

from .. import APP_NAME, PROJECT_NAME, APP_BASE


@view_config(route_name=APP_NAME+'.home', renderer='%s:templates/list.mako' % APP_BASE)
def my_view(request):
    return {'APP_BASE': APP_BASE}
    
@view_config(route_name=APP_NAME+'.clog', renderer='%s:templates/clog.mako' %APP_BASE)
def log(request):
    #repo_path = '/home/bint-e-shafiq/test_repo'
    #repository_name = "test_repo"
 
    comit_log = get_comit_log(repo_path)
    return {'APP_BASE': APP_BASE,   
            'repo_path': repo_path,
            'repository_name': repository_name,
            'comit_log': comit_log}
  
    
    


@view_config(route_name=APP_NAME+'.log', renderer='%s:templates/log.mako' % APP_BASE)
def log_view(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
   
    repo_path = '/home/bint-e-shafiq/test_repo'
    repository_name = "test_repo"
    b_name = request.matchdict['b_name']
    commit_log = get_commit_log(repo_path,b_name)
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repository_name': repository_name,
            'b_name' : b_name,
            'commit_log': commit_log}
            
            
@view_config(route_name=APP_NAME+'.branch', renderer='%s:templates/branch.mako' % APP_BASE)
def branch_log(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    repo_path = '/home/bint-e-shafiq/test_repo'
    repository_name = "test_repo"
   
    #branch_view = get_branch_view(repository_path)
    branch_view = get_branch_view(repo_path)
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repository_name': repository_name,
            'branch_view': branch_view}

            
            
@view_config(route_name=APP_NAME+'.cbranch', renderer='%s:templates/c_branch.mako' % APP_BASE)
def current_branch(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    # repository_path = '/MyWork/Projects/eims-dev'
    repository_path = '/home/bint-e-shafiq/test_repo'
    repository_name = "giteverywhere"
   
    branch_view = get_current_branch(repository_path)
    return {'APP_BASE': APP_BASE,
            'repository_path': repository_path,
            'repository_name': repository_name,
            'branch_view': branch_view}
            
@view_config(route_name=APP_NAME+'.tag', renderer='%s:templates/tag.mako' % APP_BASE)
def tag_title(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    repo_path = '/home/bint-e-shafiq/sample_repo'
    repository_name = "sample_repo"
   
    #branch_view = get_branch_view(repository_path)
    tag_list = get_tag_list(repo_path)
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repository_name': repository_name,
            'tag_list': tag_list}
            

@view_config(route_name=APP_NAME+'.showtag', renderer='%s:templates/tag.mako' % APP_BASE)
def tag_detail(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    repo_path = '/home/bint-e-shafiq/test_repo'
    repository_name = "test_repo"
   
    #branch_view = get_branch_view(repository_path)
    tag_list = get_tag_detail(repo_path)
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repository_name': repository_name,
            'tag_list': tag_list}
            
            
@view_config(route_name=APP_NAME+'.diff', renderer='%s:templates/diff.mako' % APP_BASE)
def commit_diff(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    #view = DBSession.query(RepoName).all()
   # return {'view':view}
   # R = DBSession.query(RepoName)
   # path = R.repo_path
   # R = DBSession.query(RepoName.repo_name, RepoName.repo_path).all()
    #path = RepoName.repo_path
    repo_path = '/home/bint-e-shafiq/sample_repo'
    #repo_path = DBSession.query(Repository).filter_by(repo_path='_repo')
    repository_name = "sample_repo"
   
    view_diff = get_commit_difference(repo_path)
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repository_name': repository_name,
            'view_diff': view_diff
            }
            
@view_config(route_name=APP_NAME+'.files', renderer='%s:templates/file_names.mako' % APP_BASE)
def file_list(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    repo_path = '/home/bint-e-shafiq/test_repo'
    repository_name = "test_repo"
   
    #branch_view = get_branch_view(repository_path)
    file_names = get_file_name(repo_path)
   
    #f_name = file_names
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repository_name': repository_name,
            'file_names': file_names}
            
            
@view_config(route_name=APP_NAME+'.contents', renderer='%s:templates/file_contents.mako' % APP_BASE)
def file_content(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    repo_path = '/home/bint-e-shafiq/test_repo'
    repository_name = "test_repo"
    #repo = request.matchdict['repo_name']
    f_name = request.matchdict['f_name']
   
    #branch_view = get_branch_view(repository_path)
    file_contents = get_file_contents(repo_path,f_name)
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
	    #'repo':repo,
            'repository_name': repository_name,
            'f_name':f_name,
            'file_contents': file_contents}
            
@view_config(route_name=APP_NAME+'.manage', renderer='%s:templates/manage.mako' % APP_BASE)
def manage_branch(request):
  
 
 
    #view = DBSession.query(RepoName).all()
    repo = request.matchdict['repo']


    R = DBSession.query(Repository).filter_by(repo_name=repo).first()
   
    repo_path = R.repo_path 

   # repo_path = os.path.join('/home/bint-e-shafiq',repo)
   # repo_path = DBSession.query(Repository).filter(Repository.repo_name)

    branch_view = get_branch_view(repo_path)
    commit_log = get_commit_log(repo_path)
    comit_log = get_comit_log(repo_path)
    tag_list = get_tag_list(repo_path)
    tag_show = get_tag_detail(repo_path)
    
    
   
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repo': repo,
            'repo_path':repo_path,
            'branch_view': branch_view,
            'commit_log':commit_log,
            'comit_log':comit_log,
            'tag_list':tag_list,
            'tag_show':tag_show
     #       'view':view
     }
            

              
        
            

            



