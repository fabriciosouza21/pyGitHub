from util.readJson import readJson

def processText(result):
    text = ""
    for comment in result:
        text = f'{text}{comment["body"]}'
    return text

def textCommensts(database="database/issue"):    
    result =readJson(f"{database}.json")["comments"]
    return processText(result=result)    
    
