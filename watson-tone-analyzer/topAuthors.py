def topAuthors(comments):
    author = {}
    authors = []
    for comment in comments:
        if author.get(comment["author"]):
            author[comment["author"]]=author[comment["author"]] + 1
        else:
            author[comment["author"]] = 1
    top = sorted(author.items(), key=lambda x: x[1], reverse=True)
    authors.append(top[0][0])    
    return authors