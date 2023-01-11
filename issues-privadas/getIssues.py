from github import Github, UnknownObjectException,GithubException
import sys
import os
from util.IssueRepositoryUtills import IssueRepositoryUtils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.readJson import readJson
from util.instantiate_comments_dict import instantiate_comments_dict
from util.writeDictToJson import writeDictToJson


def get_issues():
    links = readJson("links", "issues-privadas/issues/")
    list_links = list(links["links"])
    for link in list_links:
        issue_uttil = IssueRepositoryUtils(link)        
        try:
            issue_dict = issue_instanciate(issue_uttil)
            save_issue(issue_dict, issue_uttil.repo_name)
        except (UnknownObjectException , GithubException):
            print(f"Erro ao buscar issue {link}")
            continue

def issue_instanciate(issue_uttil:IssueRepositoryUtils)->dict:
    token = os.environ["TOKEN"]
    g = Github(token)
    issue_dict = {}
    repo = g.get_repo(f"{issue_uttil.get_owner()}/{issue_uttil.repo_name}")
    issue = repo.get_issue(int(issue_uttil.get_issue_number()))
    comments_issue = [] 
    comment_dict = {}
    comment_dict["user"] = issue.user.login
    comment_dict["comment"] = issue.body
    comments_issue.append(comment_dict)
    comments = issue.get_comments()
    for comment in comments:
        comment_dict = {}
        comment_dict["user"] = comment.user.login
        comment_dict["comment"] = comment.body
        comments_issue.append(comment_dict)
    issue_dict["comments"] = comments_issue
    issue_dict["repository"] = issue_uttil.repo_name
    issue_dict["user"] = issue.user.login
    return issue_dict

def create_dir(repo_name):
    if not os.path.isdir(f"database-natural-language/issues/{repo_name}"):
        os.mkdir(f"database-natural-language/issues/{repo_name}")

def save_issue(issue, repo_name):
     create_dir(repo_name)
     writeDictToJson(issue,f"{repo_name}",f"database-natural-language/issues/{repo_name}/")

if __name__ == "__main__":
    get_issues()