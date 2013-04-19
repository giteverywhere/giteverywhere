"""
Module containing functions/classes to work with repositories
"""
import re
import subprocess


def get_commit_log(repository_path):
    """
    Given path to a repository on local system, returns a list of commit messages along with
    commit hash
    """

    commits = []
    s = subprocess.check_output("cd %s; git log" % repository_path, shell=True)
    r = re.compile("commit (.*?)\n.*?Author: (.*?)\n.*?Date:(.*?)\n\n(.*?)\n\n", re.M+re.S+re.U+re.I)
    matches = r.findall(s)
    for m in matches:
        commits.append(dict(commit_hash=m[0].strip(), author=m[1].strip(), datetime=m[2].strip(), message=m[3].strip()))

    return commits
