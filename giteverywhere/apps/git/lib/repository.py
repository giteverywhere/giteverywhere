"""
Module containing functions/classes to work with repositories
"""
import re
import subprocess


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

    

#def get_branch_view(repository_path):
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
    r = re.compile("((.*))\n")
    matches = r.findall(s)
    for m in matches:
        tags.append(dict(tag_title=m[0].strip()))


    return tags
    
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
  
    contents = []
   #s = subprocess.check_output("cd %s; git branch " % repository_path, shell=True)
    #r = re.compile("(\w.(.*))\n")
    s = subprocess.check_output("cd %s; more %s" % (repo_path,f_name), shell=True)
    r = re.compile("((.*))")
   # r = re.compile("(.*?)\n")
 #   s = subprocess.check_output("cd %s; git checkout %s; git log" % (repo_path,b_name), shell=True)
    #s = subprocess.check_output("cd %s; more " % repo_path, shell=True)
    #r = re.compile("((.*))\n")
    
    matches = r.findall(s)
    for m in matches:
        contents.append(dict(file_content=m[0].strip()))


    return contents
