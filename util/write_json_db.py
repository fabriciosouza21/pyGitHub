import json


def write_comments_json_db(comments, name_file="file"):
    with open(f'docker/mongo-seed/{name_file}.json', 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False,

                  sort_keys=True, indent=2, separators=(',', ':'))