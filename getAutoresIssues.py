from numbers import Number
import os
import time

from numpy import number
from util.readJson import readJson
from github import Github, UnknownObjectException,GithubException,RateLimitExceededException
from util.writeDictToJson import writeDictToJson
import datetime
from dateutil.relativedelta import relativedelta
erro_limit_5000 = False
arquivo_finalizado = False
def main():
    global erro_limit_5000 
    global arquivo_finalizado
    erro = False
    erro_limit_5000 = False
    token = os.environ["TOKEN"]
    date = datetime.datetime.now() - relativedelta(years=2)
    date = date.date()
    g = Github(token)
    autores_analisados = set()
    limit_exceeded = False
    autores_toxico_dict = readJson("autores_toxico", "database/autores/")
    control_issues = readJson("control_issues", "database/issues/")
    if(control_issues.get("autores_toxico") and control_issues["autores_toxico"] != []):
        autores_toxico = control_issues["autores_toxico"]
    else:
        autores_toxico = autores_toxico_dict["autores_toxico"]  
    control_issue_number = control_issues.get("issue_corrente")
    control_issue_project = control_issues.get("projeto_corrente")
    issue_target = False
    for author in autores_toxico:
        current_author = author
        totalCount = 1000 #total de issues pela api default
        page = 0
        if(limit_exceeded):
            break
        while totalCount ==1000 and not limit_exceeded :
            try: 
                page += 1
                # issues = g.search_issues(query=f"commenter:{author}",sort="created",order="desc",page=page)
                issues = g.search_issues(query=f"author:{author}",page=page)
            
                totalCount = issues.totalCount
                print(f"Total de issues: {issues.totalCount}")
                print(f"Página: {page}")
                issue_dict = {}
                for issue in issues:
                    rate = g.get_rate_limit()
                    rate_limit = rate.core.remaining
                    print(f"{author} {issue.number}")

                    if(rate_limit < 100):
                        erro = True
                        erro_limit_5000 = True
                        limit_exceeded = True 
                        print(f"Rate limit: {rate_limit}")
                        difference = set(autores_toxico).difference(autores_analisados)
                        print(sorted(list(difference)))
                        control_issues["autores_toxico"] = sorted(list(difference))
                        control_issues["issue_corrente"] = issue.number
                        control_issues["projeto_corrente"] = issue.repository.name
                        writeDictToJson(control_issues,"control_issues", "database/issues/")
                        break
                    if((control_issue_number and control_issue_number == issue.number and control_issue_project and control_issue_project == issue.repository.name) and not issue_target or not control_issue_number):
                        print("----------------> target encontrado")
                        issue_target = True
                    if(not issue_target):
                        print("target não encontrado")
                        continue
                        
                        
                    comments_issue = [] 
                    comment_dict = {}
                    comment_dict["user"] = issue.user.login
                    comment_dict["comment"] = issue.body
                    comments_issue.append(comment_dict)
                    if(issue.comments>0):
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
            except RateLimitExceededException as e:
                erro = True
                limit_exceeded = True 
                rate = g.get_rate_limit()
                rate_limit = rate.core.remaining
                print(f"Rate limit: {rate_limit}")
                print(e)
                difference = set(autores_toxico).difference(autores_analisados)
                control_issues["autores_toxico"] = sorted(list(difference))
                control_issues["issue_corrente"] = None
                control_issues["projeto_corrente"] = issue.repository.name
                writeDictToJson(control_issues,"control_issues", "database/issues/")
                break
            except Exception as e:
                erro = True
                print("Erro ao buscar issues")
                print("autor: " + author)
                print("page: " + str(page))
                print("date: " + str(date))
                print(e)
                difference = set(autores_toxico).difference(autores_analisados)
                control_issues["autores_toxico"] = sorted(list(difference))
                control_issues["issue_corrente"] = issue.number
                writeDictToJson(control_issues,"control_issues", "database/issues/")
                break
            
        autores_analisados.add(current_author)
        issue_target = True

    if(not erro):
        print("sem erros")
        difference = set(autores_toxico).difference(autores_analisados)
        control_issues["autores_toxico"] = sorted(list(difference))
        writeDictToJson(control_issues,"control_issues", "database/issues/")
        arquivo_finalizado = True
    print("finished total issues")

if __name__ == '__main__':
    
    while not arquivo_finalizado:
        main()
        if(erro_limit_5000):
            print("timeout 1 hora")
            time.sleep(40*60)
        else:
            print("timeout 3 minutos")
            time.sleep(3*60)
        
