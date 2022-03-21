import json


def writeCommentsJson(comments, nameFile="file"):

    commentsjson = {}

    commentsjson["comments"] = comments

    with open(f'database/{nameFile}.json', 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=True,

                  sort_keys=True, indent=2, separators=(',', ':'))
