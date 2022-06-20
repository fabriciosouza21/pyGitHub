import os
from util.readJson import readJson
from github import Github, UnknownObjectException,GithubException
from util.writeDictToJson import writeDictToJson
token = os.environ["TOKEN"]
  
g = Github(token)
autores_analisados = set()
limit_exceeded = False
autores_toxico_dict = readJson("autores_toxico", "database/autores/")
control_issues = readJson("control_issues", "database/issues/")
if(control_issues !={}):
    autores_toxico = control_issues["autores_toxico"]
else:
    autores_toxico = autores_toxico_dict["autores_toxico"]
control_issue_number = control_issues.get("issue_corrente")

for author in autores_toxico:
    current_author = author
    totalCount = 1000 #total de issues pela api default
    page = 0
    if(limit_exceeded):
        break
    while totalCount ==1000 and not limit_exceeded:
        page += 1
        issues = g.search_issues(query=f"commenter:{author}",page=page)
        
        totalCount = issues.totalCount
        print(f"Total de issues: {issues.totalCount}")
        issue_dict = {}

        for issue in issues:
            if(control_issue_number and control_issue_number != issue.number and not issue_target):
                continue
            else:
                issue_target = True
            rate = g.get_rate_limit()
            rate_limit = rate.core.remaining
            if(rate_limit < 100):
                limit_exceeded = True 
                print(f"Rate limit: {rate_limit}")
                difference = set(autores_toxico).difference(autores_analisados)
                control_issues["autores_toxico"] = sorted(list(difference))
                control_issues["issue_corrente"] = issue.number
                writeDictToJson(control_issues,"control_issues", "database/issues/")
                break
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
            issue_dict["repository"] = issue.repository.name
            issue_dict["user"] = issue.user.login
            if not os.path.isdir(f"database/issues/{issue.repository.name}"):
                os.mkdir(f"database/issues/{issue.repository.name}")
            writeDictToJson(issue_dict, f"{issue.repository.name}-{issue.number}", f"database/issues/{issue.repository.name}/")

    autores_analisados.add(current_author)
