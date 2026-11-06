from sys import argv

from github_viewer.api import profile

print(profile(argv[1]))