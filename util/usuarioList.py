
""" this function return a list with users from json file"""

def usuario_list ( comments: list ): 
    users = set()
    for comment in comments:
        users.add(comment["user"])
    return users
