def removeEmptyAuthor(comments):
    for comment in comments:
        if not comment["author"]:
            comments.remove(comment)

def removeEmptyBody(comments):
    for comment in comments:
        if comment["body"] =="":
            comments.remove(comment) 
                      
