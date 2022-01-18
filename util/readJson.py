import json

def readJson(fileName,path="database"):
    with open(f'{path}/{fileName}.json', 'r',encoding="utf-16") as f:
        return json.load(f)