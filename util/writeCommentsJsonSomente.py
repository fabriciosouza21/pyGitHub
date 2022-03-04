import json
def writeCommentsJson(comments,nameFile="file"):

    commentsjson = {}
    commentslist = []
    for comment in comments:
        commentslist.append(comment.to_dict())
    commentsjson["comments"] = commentslist

    with open(f'database/{nameFile}.json', 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False,

                  sort_keys=True, indent=2, separators=(',', ':'))