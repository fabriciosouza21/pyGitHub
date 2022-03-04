

from email import header
from math import ceil
from entities.Comment import Comment
from util.resquest.GitApiHearderResponse import GitApiHearderResponse
from util.writeCommentsJsonSomente import writeCommentsJson
from util.readJson import readJson
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
        try:
            custom_comment["user"] = comment["user"]["login"]
            custom_comment["created_at"] = comment["created_at"]
            custom_comment["body"] = comment["body"]
            result["comments"].append(custom_comment)
        except:
            print(f"Erro ao instanciar o comentario {comment}")

    return result


def get_pages() -> None:
    token = os.environ["TOKEN"]
    comments_total = []
    limite_requisicoes = False
    owner = "spring-projects"
    repo = "spring-boot"
    query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {
        "state": "all",
        "per_page": 100,
    }
    response_header = GitApiHearderResponse()
    headers = {'Authorization': f'token {token}'}

    issues_repo_armazenada = readJson(f"{repo}-issues")

    page_armazenada = issues_repo_armazenada.get("page",None)
    issues_armazenadas = issues_repo_armazenada.get("issues",None)

    if not issues_armazenadas:
        issues_repo_armazenada["issues"] = []
    if page_armazenada:
        query_url = page_armazenada

    print(f"Iniciando busca das issues {repo}...")
    
    while query_url:
        print(query_url)
        issues_repo_armazenada["page"] = query_url
        r = requests.get(query_url, headers=headers, params=params)
        response_issue = r.json()
        header = r.headers
        header["current_page"] = query_url
        response_header.set_header(header)
        if(response_header.limit_estante >100):
            for issue in response_issue:
                issue["comments_list"] = []
                if issue["comments"] > 0:
                    r_comments = requests.get(
                        issue["comments_url"], headers=headers)
                    response_comments = r_comments.json()
                    issue["comments_list"] = response_comments
                comments = instantiate_comments_dict(issue)
                comments_total.append(comments)
        else:
            print("Limite de requisições atingido")
            issues_repo_armazenada["issues"].extend(comments_total)
            issues_repo_armazenada["page"] = query_url
            query_url = None
            limite_requisicoes = True            
            break
        query_url = response_header.proxima_pagina
    if limite_requisicoes == False:  
        issues_repo_armazenada["issues"].extend(comments_total)
        
    print(f"Iniciando write das issues {repo}...")
    writeCommentsJson(issues_repo_armazenada, f"{repo}-issues")



if __name__ == '__main__':
    get_pages()
