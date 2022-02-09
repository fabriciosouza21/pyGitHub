

from math import ceil
from entities.Comment import Comment
#from util.writeCommentsJson import writeCommentsJson
from util.writeCommentsJsonSomente import writeCommentsJson
from github import Github
import os
import requests


def InstantiateComments(issue):
    all_comments = []
    comment = Comment(issue.number, issue.user.name,
                      issue.created_at, issue.body)
    all_comments.append(comment)
    comments = issue.get_comments()
    for comment in comments:
        custom_comment = Comment(
            issue.number, comment.user.name, comment.created_at, comment.body)
        all_comments.append(custom_comment)
    return all_comments


def getIssue():
    token = os.environ["TOKEN"]
    g = Github(token)
    commentsTotal = []
    repo = g.get_repo("spring-projects/spring-boot")
    issues = repo.get_issue(10907)
    comments = InstantiateComments(issues)
    writeCommentsJson(comments, "spring-boot-10907")


def InstantiateCommentsDict(issue):
    result = {}
    result["number"] = issue.number
    result["user"] = issue.user.name
    result["created_at"] = issue.created_at.strftime("%d %B, %Y")
    result["body"] = issue.body
    result["comments"] = []
    comments = issue.get_comments()
    global comentraios 
    for comment in comments:
        custom_comment = {}
        custom_comment["user"] = comment.user.name
        custom_comment["created_at"] = comment.created_at.strftime("%d %B, %Y")
        custom_comment["body"] = comment.body
        result["comments"].append(custom_comment)

    return result


def getPages():
    global comentraios
    token = os.environ["TOKEN"]
    g = Github(token)
    page = 0
    commentsTotal = []
    issuesPages = []
    try:
        owner = "spring-projects"
        repo = "spring-boot"
        query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        params = {
           "state": "all",
           "per_page": 100,
           "page": page
        }
        headers = {'Authorization': f'token {token}'}
        r = requests.get(query_url, headers=headers, params=params)
        link = r.headers.get('link')
        query_url = proximaPagina(link)
        limite = r.headers.get('X-RateLimit-Limit')
        restante = r.headers.get('X-RateLimit-Remaining')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    getPages()
