from pyramid.view import view_config
import os
import re
import zipfile
import sys
import json
from pyramid.httpexceptions import HTTPFound

from ..models import (
    DBSession,
    Repository,
    #include your models here
)


from ..lib.repository import get_commit_log
from ..lib.repository import get_branch_view
from ..lib.repository import get_current_branch
from ..lib.repository import get_clog
from ..lib.repository import get_tag_list
from ..lib.repository import get_tag_detail
from ..lib.repository import get_neg_detail
from ..lib.repository import get_unc_contents
from ..lib.repository import get_commit_difference
from ..lib.repository import get_comit_difference
from ..lib.repository import get_file_name
from ..lib.repository import get_file_contents
from ..lib.repository import get_subdir
from ..lib.repository import get_commit_record
from ..lib.repository import get_comit_record
from ..lib.repository import del_common_cmt
from ..lib.repository import get_comit_log
from ..lib.repository import get_sorted
from ..lib.repository import get_zip
from ..lib.repository import get_tar_gz

#Note: Instead of so many import lines this would have been better
#import ..lib.repository
#OR
#from ..lib.repository import *

from .. import APP_NAME, PROJECT_NAME, APP_BASE


@view_config(route_name=APP_NAME+'.home', renderer='%s:templates/list.mako' % APP_BASE)
def my_view(request):
    return {'APP_BASE': APP_BASE}


@view_config(route_name=APP_NAME+'.view_repo_names', renderer='%s:templates/view_repo_names.mako'%APP_BASE)
def view_rnames(request):

    only_content = request.GET.get('only_content', 0)
    view = DBSession.query(Repository).all()
    return {'view': view, 'only_content': only_content}


@view_config(route_name=APP_NAME+'.json_repo_names', renderer='json')
def json_rnames(request):

    repositories = DBSession.query(Repository).all()
    return repositories


@view_config(route_name=APP_NAME+'.log', renderer='%s:templates/log.mako' % APP_BASE)
def log_view(request):
    #Note: View the log of a particular branch of repository

    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    
    b_name = request.matchdict['b_name']
    commit_log = get_commit_log(r.repo_path,b_name)  
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            'b_name' : b_name,
            'commit_log': commit_log}  
    
@view_config(route_name=APP_NAME+'.clog', renderer='%s:templates/clog.mako' %APP_BASE)
def log(request):
    #Note: view the log of active branch of repository
 
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    output = request.matchdict['output']
    log = get_clog(r.repo_path)
    data = json.dumps(log)
    
    return {'APP_BASE': APP_BASE,   
            'repo_path': r.repo_path,
            'repo': r.repo_name,
            'comit_log': log,
            'output':output,
            'data':data
            }        


def get_branches(repo_name):
    r = DBSession.query(Repository).filter_by(repo_name=repo_name).first()
    branches = get_branch_view(r.repo_path)
    return branches


@view_config(route_name=APP_NAME+'.branch', renderer='%s:templates/branch.mako' % APP_BASE)
def branch_log(request):
    #Note: View branches of repository
    branches = get_branches(request.matchdict['repo'])
    only_content = request.GET.get('only_content', 0)

    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            'branches': branches,
            'only_content': only_content}


@view_config(route_name=APP_NAME+'.json_branch', renderer="json")
def json_branch_log(request):
    branches = get_branches(request.matchdict['repo'])
    return branches


@view_config(route_name=APP_NAME+'.cbranch', renderer="json")
def current_branch(request):
    #Note: View active branche of repository
  
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
   
    branch_view = get_current_branch(r.repo_path)  
    output = request.matchdict['output']
    
    data = json.dumps(branch_view)
    if output == 'html': 
        return {'APP_BASE': APP_BASE,
                'repository_path': r.repo_path,
                'repository_name': r.repo_name,
                'branch_view': branch_view
                }
    else:
        return data

@view_config(route_name=APP_NAME+'.tag', renderer='%s:templates/tag.mako' % APP_BASE)
def tag_title(request):
    #Note: View tags of repository
   
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    
    tag_list = get_tag_list(r.repo_path)
    
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            'tag_list': tag_list}
            

#@view_config(route_name=APP_NAME+'.showtag', renderer='%s:templates/tag.mako' % APP_BASE)
@view_config(route_name=APP_NAME+'.showtag', renderer='%s:templates/new1.mako' % APP_BASE)
def tag_info(request):
   
    #Note: Need to be modified
    
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    
    #tags = get_tag_detail(r.repo_path)
    #negs = get_neg_detail(r.repo_path)
    unc = get_unc_contents(r.repo_path)
    
    #negs = get_neg_detail(r.repo_path)
    
    
      
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            #'tags': tags,
            #'negs': negs,
            'unc':unc
            }
            
@view_config(route_name=APP_NAME+'.diff', renderer='%s:templates/diff.mako' % APP_BASE)
def commit_diff(request):
    #Note: View file name with changes in form of number of insertions and deletions
    
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()

    view_diff = get_commit_difference(r.repo_path)
    
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            'view_diff': view_diff
            }
            
            
@view_config(route_name=APP_NAME+'.cdiff', renderer='%s:templates/cdiff.mako' % APP_BASE)
def com_diff(request):
    #Note: View difference of a commit with its previous commit 'Not working properly yet'
    
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
    #Note: View name of files and subdirectories

    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()

    f_name = get_file_name(r.repo_path)
      
    return {'APP_BASE': APP_BASE,
            'repo_name':r.repo_name,
            'repo_path': r.repo_path,
            'f_name': f_name
            }
            
@view_config(route_name=APP_NAME+'.contents', renderer='%s:templates/file_contents.mako' % APP_BASE)
def file_content(request):
    #Note: View contents of file

    f_name = request.matchdict['f_name'] 
    #repo_path = os.path.join('/home/bint-e-shafiq',request.matchdict['repo'])
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    s = os.path.isdir(os.path.join(r.repo_path, f_name))
    directory = {}
    file_contents = {}
    if s == True:
        file_contents = get_file_contents(r.repo_path,f_name)
    else:
        directory = get_subdir(r.repo_path,f_name) 
        
    repo =os.path.join(request.matchdict['repo'],f_name)
    
    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repo':repo,
            'f_name':f_name,
            'directory':directory,
            'file_contents': file_contents}
            
#@view_config(route_name=APP_NAME+'.branches', renderer='%s:templates/branches.mako' % APP_BASE)
#@view_config(route_name=APP_NAME+'.branches', renderer='%s:templates/branch_names.mako' % APP_BASE) #show sorted record in form of table
@view_config(route_name=APP_NAME+'.branches', renderer='%s:templates/branch_diagram.mako' % APP_BASE) #show branch diagram
def branch(request):
    #Note: View branch diagram or commit log of all branches of repository

    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()

    branches_names = get_branch_view(r.repo_path)    
    #comit_record = get_commit_record(r.repo_path,branches_names)    
    comit_record = get_comit_record(r.repo_path,branches_names) 
    
    branch_commits = del_common_cmt(r.repo_path,branches_names,comit_record)
    
    sorted_record = get_sorted(branch_commits)

    return {'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name': r.repo_name,
            'branches_names': branches_names,
            'sorted_record':sorted_record,
            'branch_commits':branch_commits,
            'comit_record': comit_record
            }


@view_config(route_name=APP_NAME+'.manage', renderer='%s:templates/manage.mako' % APP_BASE)
def manage_branch(request):
    #Note: View repository summary including branches, commits, difference, tags, branch diagram, directories , file contents
 
    repo = request.matchdict['repo']
    R = DBSession.query(Repository).filter_by(repo_name=repo).first()
    repo_path = R.repo_path 

    branch_view = get_branch_view(repo_path)
    comit_log = get_comit_log(repo_path)

       
    return {'APP_BASE': APP_BASE,
            'repo_path': repo_path,
            'repo': repo,
            'branch_view': branch_view,
            'comit_log':comit_log           
     }

    
@view_config(route_name=APP_NAME+'.zip',renderer='%s:templates/archive.mako' % APP_BASE)
def archive(request):
  

    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
  
    zip_name = r.repo_name + '.zip'
    #zipped = get_zip(r.repo_path,r.repo_name,branches)
    zipped = get_zip(zip_name,r.repo_path)  #directory at given path is zipped  and saved at /home/bint-e-shafiq/giteverywhere
    path = os.path.join('git:static/',zip_name)
    
    return HTTPFound (location = request.static_url(path))
 
    '''return{
           'repo_path': r.repo_path,
           'repository_name':r.repo_name,
           'zipped':zipped
            
     }
    '''
    
@view_config(route_name=APP_NAME+'.tar',renderer='%s:templates/archive.mako' % APP_BASE)
def tar_gz(request):
  
    r = DBSession.query(Repository).filter_by(repo_name=request.matchdict['repo']).first()
    tar_name = r.repo_name + '.tgz'
    tar = get_tar_gz(r.repo_path,r.repo_name)
    
    path = os.path.join('git:static/',tar_name)
    
    return HTTPFound (location = request.static_url(path))
    ''' 
    return{'APP_BASE': APP_BASE,
            'repo_path': r.repo_path,
            'repository_name':r.repo_name,
            'tar':tar           
          }     
    '''
        
            

       


