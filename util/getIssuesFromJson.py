import json
import os

""" this function return a list with comments from json file"""

def get_issues_from_json ( json_file, path ): 
    issues = read_json(json_file, path)
    return issues["comments"]


def read_json(file_name,path="database"):
    arquivo = os.path.exists(f'{path}/{file_name}')
    if arquivo:
        with open(f'{path}/{file_name}', 'r',encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}