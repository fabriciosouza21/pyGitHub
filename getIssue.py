

from email import header
from math import ceil
from entities.Comment import Comment
from util.resquest.GitApiHearderResponse import GitApiHearderResponse
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


def get_issue():
    token = os.environ["TOKEN"]
    g = Github(token)
    commentsTotal = []
    repo = g.get_repo("spring-projects/spring-boot")
    issues = repo.get_issue(10907)
    comments = InstantiateComments(issues)
    writeCommentsJson(comments, "spring-boot-10907")


def instantiate_comments_dict(issue):
    result = {}
    result["number"] = issue["number"]
    result["user"] = issue["user"]["login"]
    result["created_at"] = issue["created_at"]
    result["body"] = issue["body"]
    result["comments"] = []

    comments = issue["comments_list"]
    for comment in comments:
        custom_comment = {}
        custom_comment["user"] = comment["user"]["login"]
        custom_comment["created_at"] = comment["created_at"]
        custom_comment["body"] = comment["body"]
        result["comments"].append(custom_comment)

    return result


def get_pages() -> None:
    token = os.environ["TOKEN"]
    page = 0
    commentsTotal = []

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
        response_issue = r.json()
        header = r.headers.get()
        response_header = GitApiHearderResponse(header)

        for issue in response_issue:
            issue["comments_list"] = []
            if issue["comments"] > 0:
                r_comments = requests.get(
                    issue["comments_url"], headers=headers)
                response_comments = r_comments.json()
                issue["comments_list"] = response_comments
            comments = instantiate_comments_dict(issue)
            commentsTotal.append(comments)




if __name__ == '__main__':
    get_pages()
