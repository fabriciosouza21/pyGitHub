import json
def writeCommentsJson(comments,nameFile="file"):
    with open(f'database/{nameFile}.json', 'w', encoding='utf16') as f:
        json.dump(comments, f, ensure_ascii=False,
                  sort_keys=True, indent=2, separators=(',', ':'))