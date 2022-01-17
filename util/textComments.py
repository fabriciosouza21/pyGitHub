from util.Process_text import Process_text
from util.readJson import readJson

def processText(result):
    text = ""
    for comment in result:
        text = f'{text}{comment["body"]}'
    return text

def textComments(filter:Process_text,arquivo="issue",path="database/")->str:    
    result =readJson(f"{path}{arquivo}.json")["comments"]
    text = processText(result=result)
    return filter.run_cleaner(text=text)
    
