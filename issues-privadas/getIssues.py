from github import Github, UnknownObjectException,GithubException
import sys
import os
import requests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.readJson import readJson
from util.instantiate_comments_dict import instantiate_comments_dict


token = os.environ["TOKEN"]
g = Github(token)
links = readJson("links", "issues-privadas/issues/")
listLinks = list(links["links"])
link_gitHub_api = []
for link in listLinks:
    link_whitout_gitHub = (link).removeprefix("https://github.com/")
    split_link = link_whitout_gitHub.split("/")
    owner = split_link[0]
    repo = split_link[1]
    issue_number = split_link[3]
    try:
        repo = g.get_repo(f"{owner}/{repo}")

        issue = repo.get_issue(int(issue_number))
        print(issue.body)
        comments = issue.get_comments()
        for comment in comments:
            print(comment.body)
    except (UnknownObjectException, GithubException):
        print(f"Erro ao buscar issue {link}")
        continue