from util.getIssuesFromJson import read_json

def importacao_sql(repository, user, arquivo, path):
    issues = read_json(arquivo, path)
    issue_projeto_number = arquivo.split("_")[-2]
    issue_number = issue_projeto_number.split("-")[-1]
    info = {
        "user" : user,
        "repository" : repository,
        "issue" : int(issue_number)
    }
    issues["info"] = info
    return issues




    