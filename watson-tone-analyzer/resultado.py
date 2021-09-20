import json
from ToString import toString

def ler_json(arq_json):
    with open(arq_json, 'r',encoding="utf-16") as f:
        return json.load(f)

def escrever_linha(sentece):
    with open('issue.csv', "a", encoding='utf8') as f:
        f.write(toString(sentece))


with open('issue.csv', "w", encoding='utf8'):
    pass
data = ler_json("issue.json")
sentences_tones = data["sentences_tone"]
for sentence in sentences_tones:
    escrever_linha(sentence)


     