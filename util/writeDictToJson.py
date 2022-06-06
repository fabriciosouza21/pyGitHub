import json

def writeDictToJson(dados,fileName="issue",path="resultWatson/"):
    with open(f'{path}{fileName}.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ':'))