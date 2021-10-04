import json

def readJson(arq_json):
    with open(arq_json, 'r',encoding="utf-16") as f:
        return json.load(f)