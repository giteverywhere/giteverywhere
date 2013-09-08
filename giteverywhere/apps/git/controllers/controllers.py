from pyramid.view import view_config
import os

#import operator

import re

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
from ..lib.repository import get_comit_difference
from ..lib.repository import get_file_name
from ..lib.repository import get_file_contents
from ..lib.repository import get_subdir
from ..lib.repository import get_dir
from ..lib.repository import dir_detail
from ..lib.repository import get_branch_name
from ..lib.repository import get_commit_record

from .. import APP_NAME, PROJECT_NAME, APP_BASE


@view_config(route_name=APP_NAME+'.home', renderer='%s:templates/list.mako' % APP_BASE)
def my_view(request):
    return {'APP_BASE': APP_BASE}
    
@view_config(route_name=APP_NAME+'.clog', renderer='%s:templates/clog.mako' %APP_BASE)
def log(request):
    #repo_path = '/home/bint-e-shafiq/test_repo'
    #repository_name = "test_repo"
 
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    
    comit_log = get_comit_log(r.repo_path)
    return {'APP_BASE': APP_BASE,   
            'repo_path': r.repo_path,
            'repo': r.repo_name,
            'comit_log': comit_log}
  

@view_config(route_name=APP_NAME+'.log', renderer='%s:templates/log.mako' % APP_BASE)
def log_view(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for

    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
   # repo_path = '/home/bint-e-shafiq/test_repo'

   
   

    repository_name = "test_repo"
    b_name = request.matchdict['b_name']
    commit_log = get_commit_log(r.repo_path,b_name)
   # commit_log = sorted(comit, key=lambda k: k['message'])   
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': repository_name,
            'b_name' : b_name,
            'commit_log': commit_log}
            
            
@view_config(route_name=APP_NAME+'.branch', renderer='%s:templates/branch.mako' % APP_BASE)
def branch_log(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    #repo_path = '/home/muslim/test_repo'
    #repository_name = "test_repo"
    
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
   
    #branch_view = get_branch_view(repository_path)
    branch_view = get_branch_view(r.repo_path)
    d = []
    a = range(len(branch_view))
    for s in a:
        m = branch_view[s]['branch_name']
        d.append(m)
        
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            'branch_view': branch_view,
            'd':d
            }

            
            
@view_config(route_name=APP_NAME+'.cbranch', renderer='%s:templates/c_branch.mako' % APP_BASE)
def current_branch(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    # repository_path = '/MyWork/Projects/eims-dev'
    repository_path = '/home/muslim/test_repo'
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
    #repo_path = '/home/muslim/sample_repo'
    #repository_name = "sample_repo"
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    #branch_view = get_branch_view(repository_path)
    tag_list = get_tag_list(r.repo_path)
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            'tag_list': tag_list}
            

@view_config(route_name=APP_NAME+'.showtag', renderer='%s:templates/tag.mako' % APP_BASE)

def tag_info(request):
  
    repo_path = '/home/bint-e-shafiq/test_repo'
    repository_name = "test_repo"
   

    tag_list = get_tag_detail(repo_path)
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repository_name': repository_name,
            'tag_list': tag_list}
'''
def tag_detail(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    repo_path = '/home/muslim/giteverywhere'
    repository_name = "giteverywhere"

   

    tag_list = get_tag_detail(repo_path)
   
    line = "";

    matchObj = re.search( r'(.*) + (\.*)', line, re.M|re.I)

    if matchObj:
      matchObj.group()
  
   
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repository_name': repository_name,
            'tag_list': tag_list}
 '''           
            
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
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    #repo_path = '/home/bint-e-shafiq/sample_repo'
    #repo_path = DBSession.query(Repository).filter_by(repo_path='_repo')
    #repository_name = "sample_repo"
   
    view_diff = get_commit_difference(r.repo_path)
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            'view_diff': view_diff
            }
            
            
@view_config(route_name=APP_NAME+'.cdiff', renderer='%s:templates/cdiff.mako' % APP_BASE)
def com_diff(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    c_hash = request.matchdict['hash']
    comit_diff = get_comit_difference(r.repo_path,c_hash)
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            'comit_diff': comit_diff
            }
            
            
@view_config(route_name=APP_NAME+'.files', renderer='%s:templates/file_names.mako' % APP_BASE)
def file_list(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for
    '''

    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()

    f_name = get_file_name(r.repo_path)

    repo_path = '/home/muslim/giteverywhere'
    repository_name = ""
   
    #branch_view = get_branch_view(repository_path)
    f_name = get_file_name(repo_path)

    #file_name = f_name

    
    
    #d = f_name[0]['file_name']
    a = range(len(f_name))
    d = []

    #for s in range(len(f_name)): 
    for s in a:
      m = f_name[s]['file_name']
      d.append(m)
     # d = f_name[s]['file_name']

    for s in a:
     
       
     m = f_name[s]['file_name']
     d.append(m)
     

          
    for i in f_name:
      l = i['file_name']
      
    return {'APP_BASE': APP_BASE,
            'repo_name':r.repo_name,
            'repo_path': r.repo_path,
            'f_name': f_name,
            
            'l': l,
            'a': a,

            's': s,
            'i': i

            'd' : d,
            'm': m,
            's': s

            #'file_name':file_name
            }
    '''
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()

    f_name = get_file_name(r.repo_path)
    #file_name = f_name

    
    
    #d = f_name[0]['file_name']
    a = range(len(f_name))
    d = []
    #for s in range(len(f_name)): 
    for s in a:
      m = f_name[s]['file_name']
      d.append(m)
     # d = f_name[s]['file_name']
          
    for i in f_name:
      l = i['file_name']
      
    return {'APP_BASE': APP_BASE,
            'repo_name':r.repo_name,
            'repo_path': r.repo_path,
            'f_name': f_name,
            'd' : d,
            'l': l,
            'a': a,
            's': s,
            'i': i
            #'file_name':file_name
            }
            
@view_config(route_name=APP_NAME+'.contents', renderer='%s:templates/file_contents.mako' % APP_BASE)
def file_content(request):
    #Note: change the repository path to a repository on your system
    #      that you want to view the log for

    #repo_path = '/home/muslim/giteverywhere'
    #repository_name = "test_repo"

    
    #r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    '''f_name = request.matchdict['f_name'] 
    repo_path = os.path.join('/home/bint-e-shafiq',request.matchdict['repo'])
    s = os.path.isdir(os.path.join(repo_path, f_name))
    #if not item.startswith('.'):
    directory = {}
    file_contents = {}
    if s == True:
        file_contents = get_file_contents(repo_path,f_name)
    else:
        directory = get_subdir(repo_path,f_name) 
        
    repo =os.path.join(request.matchdict['repo'],f_name)
    
   # file_contents = os.listdir(r.repo_path)
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repo':repo,
            #'repository_name': r.repo_name,
            'f_name':f_name,
            'directory':directory,
            'file_contents': file_contents}
            '''
    f_name = request.matchdict['f_name'] 
    repo_path = os.path.join('/home/bint-e-shafiq',request.matchdict['repo'])
    s = os.path.isdir(os.path.join(repo_path, f_name))
    #if not item.startswith('.'):
    directory = {}
    file_contents = {}
    if s == True:
        file_contents = get_file_contents(repo_path,f_name)
    else:
        directory = get_subdir(repo_path,f_name) 
        
    repo =os.path.join(request.matchdict['repo'],f_name)
    
   # file_contents = os.listdir(r.repo_path)
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repo':repo,
            #'repository_name': r.repo_name,
            'f_name':f_name,
            'directory':directory,
            'file_contents': file_contents}
            
@view_config(route_name=APP_NAME+'.dir', renderer='%s:templates/dir.mako' % APP_BASE)
def tag_detail(request):
 
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()

    repo_path = r.repo_path
    browse_dir = get_dir(repo_path)
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            #'repository_name': repository_name,
            'browse_dir': browse_dir}
            
@view_config(route_name=APP_NAME+'.branches', renderer='%s:templates/branch_names.mako' % APP_BASE)
def branch(request):
    
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    branches_names = get_branch_name(r.repo_path)
    
    #d = []
    #a = range(len(branches_names))
    #for i in a:
     #   m = branches_names[i]['branch_name']
       # b_name = m
        #d.append(m)
    comit_record = get_commit_record(r.repo_path,branches_names)
    
    #comit_record = sorted(commit_record, key=lambda k: k['datetime']) 
    #comit_record = sorted(commit_record, key=operator.itemgetter('datetime'))
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            'branches_names': branches_names,
         #   'd':d,
          #  'b_name':b_name,
            'comit_record':comit_record
            }
            
@view_config(route_name=APP_NAME+'.browse', renderer='%s:templates/browse.mako' % APP_BASE)
def brwse_dir(request):
  
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()

    repo_path = r.repo_path
    f_name = request.matchdict['f_name']
    repo_path = os.path.join(repo_path ,f_name)
    contents = dir_detail(repo_path)
    return {'APP_BASE': APP_BASE,
           # 'repo_path': repo_path,
            'contents': contents}
            
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
            

              
        
            

            



