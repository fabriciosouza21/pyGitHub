def instantiate_comments_dict(issue, repositorio=None):
    result = {}
    result["number"] = issue["number"]
    result["user"] = issue["user"]["login"]
    result["created_at"] = issue["created_at"]
    result["body"] = issue["body"]
    result["repository"] = repositorio
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