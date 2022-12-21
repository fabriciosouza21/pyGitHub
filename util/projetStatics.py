import os
import sys
from util.getIssuesFromJson import get_issues_from_json
from util.usuarioList import usuario_list

def projetc_statics(files:list, path)-> dict:
    comments_total = []
    users = set() 
    for file in files:
        comments = get_issues_from_json(file, path)
        comments_total.extend(comments)
        users = users.union(usuario_list(comments))
    


    return {
        "qtde_commentaries": len(comments_total),
        "qtde_users": len(users),
        "top_users": top_users(comments_total, users,len(users) )        
    }

def top_users(comments, users, rank=3) -> list: 
    users_list = []   
    for user in users:
        user_dict = {}
        user_dict["user"] = user
        user_dict["qtde_commentaries"] = 0
        for comment in comments:
            if user == comment["user"]:
                user_dict["qtde_commentaries"] += 1
        users_list.append(user_dict)
    return sorted(users_list, key=lambda k: k['qtde_commentaries'], reverse=True)[:rank]
        
