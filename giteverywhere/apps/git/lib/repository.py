"""
Module containing functions/classes to work with repositories
"""
import re
import subprocess
import os
import operator
import datetime


def get_commit_log(repo_path,b_name = None):
    """
    Given branch and path of a repository on local system, returns a list of commit messages along with
    commit hash for the specified repository branch
    """ 
    
    commits = []
    s = subprocess.check_output("cd %s; git checkout %s; git log " % (repo_path,b_name), shell=True)
        
    r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I)
    matches = r.findall(s)
    for m in matches:
        commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip()))
          
    return commits

def get_log(repo_path):
    """
    Given branch and path of a repository on local system, returns a list of commit messages along with
    commit hash 
    """ 
    
    commits = []
    s = subprocess.check_output("cd %s; git log " % (repo_path), shell=True)
        
    r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I)
    matches = r.findall(s)
    for m in matches:
        commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip()))
          
    return commits
      
def get_comit_log(repo_path):
    """
    Given path to a repository on local system, returns most recent commit message along with
    commit hash
    """
  
    commits = []
    s = subprocess.check_output("cd %s; git log -1 " % repo_path, shell=True)
    r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I)
    matches = r.findall(s)
    for m in matches:
        commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip()))

    return commits

def get_branch_view(repo_path):
  
  # Given path to a repository on local system, returns a list of branches
  
  
    branches = []

    s = subprocess.check_output("cd %s; git branch " % repo_path, shell=True)
    r = re.compile("((.*))\n")
    matches = r.findall(s)
    for m in matches:
        branches.append(dict(branch_name=m[0].strip()))


    return branches
 
def get_current_branch(repository_path):
  
  # Given path to a repository on local system, returns active branch of the repository
  
  
    branches = []
    s = subprocess.check_output("cd %s; git branch " % repository_path, shell=True)
    r = re.compile("(\*.(.*))\n")
    matches = r.findall(s)
    for m in matches:
        branches.append(dict(branch_name=m[0].strip()))


    return branches
    
def get_tag_list(repo_path):
 
  # Given path to a repository on local system, returns a list of tags
   
    tags = []
   
    s = subprocess.check_output("cd %s; git tag " % repo_path, shell=True)
    r = re.compile("((.*))\n")
    matches = r.findall(s)
    for m in matches:
        tags.append(dict(tag_title=m[0].strip()))

    return tags
    
def get_tag_detail(repo_path):
  
    """
    Given path to a repository on local system, returns difference of last two commits, showing added lines of code in green color and deleted lines of code in red color (Not working)
    """
    tags = []
  
    s = subprocess.check_output("cd %s; git log -p -2" % repo_path, shell=True) 
    #r = re.compile("((^[+-]) (.*?))\n", re.M+re.S) # just show channges in file contents
    r = re.compile("((^[+-])(.*?))\n", re.M+re.S+re.U) # show detailed insertions and deletions in contents of file
    
    matches = r.findall(s)
    
    for m in matches:
        tags.append(dict(tag_title=m[0].strip()))
   
    return tags
    
def get_comit_difference(repo_path,c_hash):
    """
    Given path to a repository on local system, returns a list differences of last two commits without showing code, just show number of insertions and deletions made along the file names
    """
  
    cdiff = []
    s = subprocess.check_output("cd %s; git log --stat -2 %s " % (repo_path,c_hash), shell=True)
   
    r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n\n(.*?)\n(.*?)\n", re.M+re.S+re.U+re.I)
    matches = r.findall(s)
    for m in matches:
        cdiff.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip(), file_name=m[4].strip(), changes=m[5].strip()))
   


    return cdiff
    
def get_commit_difference(repo_path):
  
    """
    Given path to a repository on local system, returns a list of differences of commits without showing code, just show number of insertions and deletions made along the file names
    """
  
    diff = []
    s = subprocess.check_output("cd %s; git log --stat " % repo_path, shell=True)
    r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n\n(.*?)\n(.*?)\n", re.M+re.S+re.U+re.I)
    matches = r.findall(s)
    for m in matches:
        diff.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip(), file_name=m[4].strip(), changes=m[5].strip()))
        #diff.append(dict(commit_diff=m[0].strip()))


    return diff
  
  
def get_file_name(repo_path):
  
    """
    Given path to a repository on local system, returns names of files and directorie
    """
  
    files = []
   
    s = subprocess.check_output("cd %s; ls " % repo_path, shell=True)
    r = re.compile("((.*))\n")
    matches = r.findall(s)
    for m in matches:
        files.append(dict(file_name=m[0].strip()))


    return files  
    

def get_file_contents(repo_path,f_name):
  
    """
    Given path to a repository on local system along directory or file name in the repository, return list of subfolders and files if directory name given and return contents of file if file name given
    """
  
    
    dirs = []

    repo_path = os.path.join(repo_path, f_name)
    s = subprocess.check_output("cd %s; ls " % repo_path, shell=True)
    r = re.compile("((.*))\n")
    matches = r.findall(s)
  
    for m in matches:
        dirs.append(dict(file_content=m[0].strip()))
    return dirs
             
    
def get_subdir(repo_path,f_name):
  
    """
    Given path to a repository on local system with file name, read and return contents of file
    """
    contents = []
    s = subprocess.check_output("cd %s; more %s" % (repo_path,f_name), shell=True)
    
    r = re.compile("((.*))\n")
  
    
    matches = r.findall(s)
    for m in matches:
        contents.append(dict(file_content=m[0].strip()))


    return contents
        
def get_commit_record(repo_path,branches_names):
    """
    Given path to a repository on local system along list of branches of repository, returns commit log of all branches sorted by date and time, without repeating same commit log
    """
    
    commits = []
    comit_record = []
    comit = []
    s = [] 
    time = []
 
    for i in range(len(branches_names)):
        b = branches_names[i]['branch_name']
        
        if b.startswith('*'):
            b = b[2:] 
     
        s = subprocess.check_output("cd %s; git checkout %s; git log  " % (repo_path,b), shell=True)
        r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I)
        matches = r.findall(s)
        for m in matches:
	    s = m[2][3:len(m[2])-6]    #  m[2] contains date and time of commit log
	    time = datetime.datetime.strptime(s, '%a %b %d %H:%M:%S %Y')
            commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=time, message=m[3].strip(), branches = b.strip()))
     
        if not comit_record:
            comit_record = commits + comit_record  #concatenate bcz comit_record is empty
             
        else:
	    for t in range(len(commits)):
	        for j in range(len(comit_record)):
		    if (commits[t]['commit_hash'] != comit_record[j]['commit_hash']):
		        if (j == len(comit_record)-1):
			    comit_record.append(commits[t])
			 
	            else:
		        break
   
    comit_record = sorted(comit_record, key=operator.itemgetter('datetime'), reverse = True)
    return comit_record
     

