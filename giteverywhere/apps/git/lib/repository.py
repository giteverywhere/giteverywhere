"""
Module containing functions/classes to work with repositories
"""
import re
import subprocess
import os
import operator
#from operator import itemgetter

def get_commit_log(repo_path,b_name = None):
    """
    Given path to a repository on local system, returns a list of commit messages along with
    commit hash
    """
    
    if b_name == None:
      commits = []
      s = subprocess.check_output("cd %s; git log -1" % repo_path, shell=True)
      r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I)
      
      matches = r.findall(s)
      for m in matches:
          commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip()))

      return commits
      
    else:
     
	commits = []
        s = subprocess.check_output("cd %s; git checkout %s; git log " % (repo_path,b_name), shell=True)
     
        #r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n\n", re.M+re.S+re.U+re.I)
        r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I)
        matches = r.findall(s)
        for m in matches:
            commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip()))
          
        return commits
      
def get_comit_log(repo_path):
    """
    Given path to a repository on local system, returns a list of commit messages along with
    commit hash
    """
  
    commits = []
    #s = subprocess.check_output("cd %s; git checkout %s; git log" % (repo_path,b_name), shell=True)
    s = subprocess.check_output("cd %s; git log " % repo_path, shell=True)
    r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I)
    matches = r.findall(s)
    for m in matches:
        commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip()))

    return commits

def get_branch_view(repo_path):
  
    branches = []
   #s = subprocess.check_output("cd %s; git branch " % repository_path, shell=True)
    #r = re.compile("(\w.(.*))\n")
    s = subprocess.check_output("cd %s; git branch " % repo_path, shell=True)
    r = re.compile("((.*))\n")
    matches = r.findall(s)
    for m in matches:
        branches.append(dict(branch_name=m[0].strip()))


    return branches
 
def get_current_branch(repository_path):
  
    branches = []
    s = subprocess.check_output("cd %s; git branch " % repository_path, shell=True)
    r = re.compile("(\*.(.*))\n")
    matches = r.findall(s)
    for m in matches:
        branches.append(dict(branch_name=m[0].strip()))


    return branches
    
def get_tag_list(repo_path):
  
    tags = []
   #s = subprocess.check_output("cd %s; git branch " % repository_path, shell=True)
    #r = re.compile("(\w.(.*))\n")
    s = subprocess.check_output("cd %s; git tag " % repo_path, shell=True)
    r = re.compile("((.*))\n")
    matches = r.findall(s)
    for m in matches:
        tags.append(dict(tag_title=m[0].strip()))


    return tags
    
def get_tag_detail(repo_path):
  
    tags = []
   #s = subprocess.check_output("cd %s; git branch " % repository_path, shell=True)
    #r = re.compile("(\w.(.*))\n")
    s = subprocess.check_output("cd %s; git log -p -2" % repo_path, shell=True)
    #s = subprocess.check_output("cd %s; git show " % repo_path, shell=True)
<<<<<<< HEAD
    #r = re.compile("((.*))\n")
    #r = re.compile("(([?+-])(.*))\n")
 
    r = re.compile("((^[+-])(.*?))\n", re.M+re.S+re.U)
   
=======
    
    #r = re.compile("((^[+-])(.*))\n^", re.M)
    r = re.compile("((^[+-]) (.*?))\n", re.M+re.S)
    #r = re.compile("(([+-])(.*))\n")
   # r = re.compile("((.*))")
>>>>>>> 78bd82924af54c76a6ac5cc5a31f6b803b3a6013
    matches = r.findall(s)
    
    for m in matches:
        tags.append(dict(tag_title=m[0].strip()))
   
    return tags
    
def get_comit_difference(repo_path,c_hash):
  
    cdiff = []
   #s = subprocess.check_output("cd %s; git branch " % repository_path, shell=True)
    #r = re.compile("(\w.(.*))\n")
    s = subprocess.check_output("cd %s; git log --stat -2 %s " % (repo_path,c_hash), shell=True)
   
     
    #s = subprocess.check_output("cd %s; git log -p -2" % repo_path, shell=True)
    #r = re.compile("((.*))\n")
    #r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n\n(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I+re.I+re.I)
    r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n\n(.*?)\n(.*?)\n", re.M+re.S+re.U+re.I)
    matches = r.findall(s)
    for m in matches:
        cdiff.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip(), file_name=m[4].strip(), changes=m[5].strip()))
        #diff.append(dict(commit_diff=m[0].strip()))


    return cdiff
    
def get_commit_difference(repo_path):
  
    diff = []
   #s = subprocess.check_output("cd %s; git branch " % repository_path, shell=True)
    #r = re.compile("(\w.(.*))\n")
    s = subprocess.check_output("cd %s; git log --stat " % repo_path, shell=True)
    #s = subprocess.check_output("cd %s; git log -p -2" % repo_path, shell=True)
    #r = re.compile("((.*))\n")
    #r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n\n(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I+re.I+re.I)
    r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n\n(.*?)\n(.*?)\n", re.M+re.S+re.U+re.I)
    matches = r.findall(s)
    for m in matches:
        diff.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip(), file_name=m[4].strip(), changes=m[5].strip()))
        #diff.append(dict(commit_diff=m[0].strip()))


    return diff
  
  
def get_file_name(repo_path):
  
    files = []
   #s = subprocess.check_output("cd %s; git branch " % repository_path, shell=True)
    #r = re.compile("(\w.(.*))\n")
    s = subprocess.check_output("cd %s; ls " % repo_path, shell=True)
    r = re.compile("((.*))\n")
    matches = r.findall(s)
    for m in matches:
        files.append(dict(file_name=m[0].strip()))


    return files  
    

def get_file_contents(repo_path,f_name):
  
    
    dirs = []

    
    #s = os.path.isdir(os.path.join(repo_path, f_name))
    #if not item.startswith('.'):
    #if s == True:
            #print s
        
    repo_path = os.path.join(repo_path, f_name)
    s = subprocess.check_output("cd %s; ls " % repo_path, shell=True)
    r = re.compile("((.*))\n")
    matches = r.findall(s)
    #        for item in os.listdir(os.path.join(path, item)):
	#      print item
    for m in matches:
        dirs.append(dict(file_content=m[0].strip()))
    return dirs
             
    #else:
def get_subdir(repo_path,f_name):
    contents = []
    s = subprocess.check_output("cd %s; more %s" % (repo_path,f_name), shell=True)
    
    r = re.compile("((.*))\n")
  
    
    matches = r.findall(s)
    for m in matches:
        contents.append(dict(file_content=m[0].strip()))


    return contents
    
def get_branch_name(repo_path):
  
    branches = []
  
    s = subprocess.check_output("cd %s; git branch " % repo_path, shell=True)
    r = re.compile("((.*))\n")
    matches = r.findall(s)
    for m in matches:
        branches.append(dict(branch_name=m[0].strip()))
       
    return branches
    
def get_commit_record(repo_path,branches_names):
    
    commits = []
    comit_record = []
    comit = []
    
    #a = range(len(branches_names))
    for i in range(len(branches_names)):
      
        b = branches_names[i]['branch_name']
        s = subprocess.check_output("cd %s; git checkout %s; git log  " % (repo_path,b), shell=True)
        r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n", re.M+re.S+re.U+re.I)
        matches = r.findall(s)
        for m in matches:
            #commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip(), branches = b.strip()))
            commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip()))
        if not comit_record:
            comit_record = commits + comit_record  #concatenate bcz comit_record is em
             
        else:
	    for t in range(len(commits)):
	        for j in range(len(comit_record)):
		    if (commits[t]['commit_hash'] != comit_record[j]['commit_hash']):
		        if (j == len(comit_record)-1):
			    comit_record.append(commits[t])
			    #comit_record = commits + comit_record
	            else:
		        break
    #comit = sorted(comit_record, key=lambda k: k['message'])    
    
    commit_record = sorted(comit_record, key=operator.itemgetter('datetime'))
    return commit_record

def get_dir(repo_path):
  
    dirs = []
    for item in os.listdir(repo_path):
        if not item.startswith('.'):
      
            dirs.append(dict(browse_dir=item.strip()))
        
    return dirs   

     
def dir_detail(repo_path):
   
    dirs = []
   
    for item in os.listdir(repo_path):
      
        if not item.startswith('.'):
            s = os.path.isdir(item)
            
            if s == True:
	        for item in os.listdir(repo_path):
                    dirs.append(dict(brwse_dir=item.strip()))
                return dirs
            #print s  
	    else:
	        f = open(os.path.join(repo_path, item), "r")
	        s = f.read()
	        
	        return s
  
