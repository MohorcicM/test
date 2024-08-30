# Get git version
import subprocess
import os

# get git tag
def get_git_version():
    try:
        git_version = subprocess.check_output(["git", "describe", "--tags", "--always"], stderr=subprocess.STDOUT).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        git_version = "unknown"
    return git_version
    
print("Git version: %s" % get_git_version())

# Create a file
with open("version.txt", "w") as f:
    f.write(get_git_version())