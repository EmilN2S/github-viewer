from sys import argv

from github_viewer.api import GithubViewer

if len(argv) != 2:
    print("usage: request_status.py <username>")
else:
    print(GithubViewer(username=argv[1]).profile())