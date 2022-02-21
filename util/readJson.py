import json
import os

def readJson(fileName,path="database"):
    arquivo = os.path.exists(f'{path}/{fileName}.json')
    if arquivo:
        with open(f'{path}/{fileName}.json', 'r',encoding="utf-16") as f:
            return json.load(f)
    else:
        return {}
