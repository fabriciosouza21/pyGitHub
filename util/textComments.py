from util.readJson import readJson

def processText(result):
    text = ""
    for comment in result:
        text = f'{text}{comment["body"]}'
    return text

def textComments(arquivo="issue",path="database/"):    
    result =readJson(f"{path}{arquivo}.json")["comments"]
    return processText(result=result)    
    
