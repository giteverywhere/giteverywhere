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
        if m == matches[0]:                 # conditional statements to identify first and last commit of each branch
	    f_commit = 'TRUE'
	    l_commit = 'FALSE'
	elif m == matches[-1]:
	    f_commit = 'FALSE'
	    l_commit = 'TRUE'
	else:
	    f_commit = 'FALSE'
	    l_commit = 'FALSE'
        commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip(), is_first = f_commit.strip(), is_last = l_commit.strip()))
          
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
        b = m[0]
        if b.startswith('*'): 
	   b = b[2:]             # return active branch name without *
        branches.append(b.strip())
        
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
    '''
    s = subprocess.check_output("cd %s; git log -p -2" % repo_path, shell=True) 
    #r = re.compile("((^[+-]) (.*?))\n", re.M+re.S) # just show channges in file contents
    r = re.compile("((^[+-])(.*?))\n", re.M+re.S+re.U) # show detailed insertions and deletions in contents of file
    '''
    tags = []
    
    s = subprocess.check_output("cd %s; git log -p -2" % repo_path, shell=True)
    r = re.compile("((^[+])(.*?))\n", re.M+re.S)
   
    matches = r.findall(s)
    for m in matches:
        tags.append(dict(tag_title=m[0].strip()))
                  
    return tags
    
def get_neg_detail(repo_path):  

    negs = []
    
    s = subprocess.check_output("cd %s; git log -p -2" % repo_path, shell=True)
    n = re.compile("((^[-])(.*?))\n", re.M+re.S+re.I)

    matches = n.findall(s)
    for m in matches:
        negs.append(dict(neg_title=m[0].strip()))
    
    return negs
    
def get_unc_contents(repo_path):
  
    unc = []
    
    s = subprocess.check_output("cd %s; git log -p -2" % repo_path, shell=True)
    #u = re.compile("(^(?![commitAuthorDate\s])(.*?))\n", re.M+re.S+re.U)   #doesn't remove 'No new line at end of file'
    u = re.compile("((^(?![commitAuthorDate\s\\\]))(.*?))\n", re.M+re.S+re.U)
    #u = re.compile("((.*))\n")
    matches = u.findall(s)
    for m in matches:
        unc.append(dict(unc_title=m[0].strip()))
    
    return unc
            
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

def get_comit_record(repo_path,branches_names):
    """
    Given path to a repository on local system along list of branches of repository, returns commit log of all branches sorted by date and time, without repeating same commit log
    """    
    log = []
    
    if 'master' in branches_names:
        del branches_names[branches_names.index('master')]
        branches_names.insert(0,'master') 
        
    for b in branches_names:      
        log.append([])
        s = subprocess.check_output("cd %s; git checkout %s; git log  " % (repo_path,b), shell=True)
        r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I)
        matches = r.findall(s)
        for m in matches[::-1]:
	        
	    l = m[2][3:len(m[2])-6]    #  m[2] contains date and time of commit log
	    
	    time = datetime.datetime.strptime(l, '%a %b %d %H:%M:%S %Y')  #  parses datetime string ('l' here) according to format
	    log[branches_names.index(b)].append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=time, message=m[3].strip(),branches = b.strip()))

    return log
    
def get_commit_record(repo_path,branches_names):
    """
    Given path to a repository on local system along list of branches of repository, returns commit log of all branches sorted by date and time, without repeating same commit log
    """    
    commits = []
    commit_record = []  
    
    if 'master' in branches_names:
        del branches_names[branches_names.index('master')]
        branches_names.insert(0,'master') 
        
    for b in branches_names:      
        
        s = subprocess.check_output("cd %s; git checkout %s; git log  " % (repo_path,b), shell=True)
        r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I)
        matches = r.findall(s)
        for m in matches:
	        
	    l = m[2][3:len(m[2])-6]    #  m[2] contains date and time of commit log
	    
	    time = datetime.datetime.strptime(l, '%a %b %d %H:%M:%S %Y')  #  parses datetime string ('l' here) according to format
	    
	    commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=time, message=m[3].strip(),branches = b.strip()))
     
        if not commit_record:
            commit_record = commits + commit_record  #concatenate bcz comit_record is empty
             
        else:                   
	    for t in commits:         # comapare commit hash to avoid repitition of same commit log
	        for j in commit_record:
		    if (t ['commit_hash'] != j['commit_hash']):
		        if j == commit_record[-1]:    
			    commit_record.append(t)
	            else:
		        break
        commit_record = sorted(commit_record, key=operator.itemgetter('datetime'), reverse = True)    # sort commit record according to date and time	
    
        #for cr in commit_record:
	    
	    #if (b != cr ['branches']):    # append parent branch (branch which is missed due to same commit hash)
	        #if cr == commit_record[-1]:
		    #commit_record.append(dict(commit_hash='', author='', datetime='' , message='',is_first = '',is_last = '', branches = b))     
	    #else:
	        #break    
    return commit_record
     