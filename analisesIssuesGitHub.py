from util.getRepositoriesName import get_repositories_name
from util.getArquivosDirectory import get_arquivo_directory
from util.projetStatics import projetc_statics
from util.writeDictToJson import writeDictToJson

def analises_issues_github(path: str) -> dict:
    repositories = get_repositories_name(path)
    projects = []
    for repo in repositories:
        repository = {"name": repo}
        issues = get_arquivo_directory(f"{path}/{repo}")
        statics = projetc_statics(issues, f"{path}/{repo}")
        repository["statics"] = statics
        projects.append(repository)

    q_issues = qtde_issues(projects)
    q_users = qtde_users(projects)
    q_comments = qtde_comments(projects)
    t_users = top_users(projects)
    m_comments = media_comments(projects)
    m_users = media_users(projects)
    m_comments_users = media_comments_users(projects)
    
    for project in projects:
        project["statics"].pop("comments")

    return {"projects": projects,
            "total_issues": q_issues,
            "total_users": q_users,
            "total_comments": q_comments,
            "top_users": t_users,
            "media_comments": m_comments,
            "media_users": m_users,
            "total_projects": len(repositories),
            "media_comments_users": m_comments_users}


def qtde_issues(projects):
    qtde_issues = 0
    for project in projects:
        qtde_issues += project["statics"]["qtd_issues"]
    return qtde_issues

def qtde_users(projects):
    users = set()
    for project in projects:
        for comment in project["statics"]["comments"]:
            users.add(comment["user"])
    return len(users)

def qtde_comments(projects):
    comments = 0
    for project in projects:
        comments += project["statics"]["qtde_commentaries"]
    return comments

def top_users(projects, rank=3):
    users = set()
    for project in projects:
        for comment in project["statics"]["comments"]:
            users.add(comment["user"])
    users_list = []
    for user in users:
        user_dict = {}
        user_dict["user"] = user
        user_dict["qtde_commentaries"] = 0
        for project in projects:
            for comment in project["statics"]["comments"]:
                if user == comment["user"]:
                    user_dict["qtde_commentaries"] += 1
        users_list.append(user_dict)
    return sorted(users_list, key=lambda k: k['qtde_commentaries'], reverse=True)[:rank]

def top_projects(projects, rank=3):
    projects_list = []
    for project in projects:
        project_dict = {}
        project_dict["name"] = project["name"]
        project_dict["qtde_commentaries"] = project["statics"]["qtde_commentaries"]
        projects_list.append(project_dict)
    return sorted(projects_list, key=lambda k: k['qtde_commentaries'], reverse=True)[:rank]

def top_projects_issues(projects, rank=3):
    projects_list = []
    for project in projects:
        project_dict = {}
        project_dict["name"] = project["name"]
        project_dict["qtde_issues"] = project["statics"]["qtd_issues"]
        projects_list.append(project_dict)
    return sorted(projects_list, key=lambda k: k['qtde_issues'], reverse=True)[:rank]

def media_comments(projects):
    return qtde_comments(projects) / qtde_issues(projects)

def media_users(projects):
    return  qtde_users(projects)/ qtde_issues(projects) 

def media_comments_users(projects):
    return qtde_comments(projects) / qtde_users(projects)


if __name__ == '__main__':
    result = analises_issues_github("database/issues")
    writeDictToJson(result,"analises_issues_github", "database/")
