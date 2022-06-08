from github import Github, UnknownObjectException,GithubException
import sys
import os
import requests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.readJson import readJson
from util.instantiate_comments_dict import instantiate_comments_dict
from util.writeDictToJson import writeDictToJson

token = os.environ["TOKEN"]
g = Github(token)
links = readJson("links", "issues-privadas/issues/")
listLinks = list(links["links"])
link_gitHub_api = []
for link in listLinks:
    link_whitout_gitHub = (link).removeprefix("https://github.com/")
    split_link = link_whitout_gitHub.split("/")
    owner = split_link[0]
    repo_name = split_link[1]
    issue_number = split_link[3]
    issue_dict = {}
    issue_dict["repository"] = repo_name
    try:
        repo = g.get_repo(f"{owner}/{repo_name}")

        issue = repo.get_issue(int(issue_number))
        comments_issue = [] 
        comments_issue.append(issue.body)
        comments = issue.get_comments()
        for comment in comments:
            comments_issue.append(comment.body)
        issue_dict["comments"] = comments_issue
        writeDictToJson(issue_dict,f"{repo_name}","database-natural-language/")
    except (UnknownObjectException, GithubException):
        print(f"Erro ao buscar issue {link}")
        continue