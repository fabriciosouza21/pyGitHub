from urllib import response
from util.readJson import readJson
import os
from util.readJson import readJson
from util.write_json_db import write_comments_json_db
from util.natural_language_understanding import request_ibm_watson_natural_language_understanding
from util.writeDictToJson import writeDictToJson



def get_comments(comment):
    return comment["comment"]

comentarios_total = []    
def analyse_natural_language():
    pasta = './database-natural-language'
    arquivos_local = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            nome_arquivo, extensao = os.path.splitext(arquivo)
            arquivos_local.append(nome_arquivo)
    for arquivo in arquivos_local:
        issue = readJson(arquivo, f"database-natural-language/issues/{arquivo}")
        comments = map(get_comments, list(issue["comments"]))
        text = " .".join(comments)
        request_ibm_watson_natural_language_understanding(repo=issue["repository"], text= text)

def analyse_natural_language_comments():
    pasta = './database-natural-language'
    arquivos_local = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            nome_arquivo, extensao = os.path.splitext(arquivo)
            arquivos_local.append(nome_arquivo)
    for arquivo in arquivos_local:
        issue = readJson(arquivo, f"database-natural-language/issues/{arquivo}")
        comments = issue["comments"]
        repo_name = issue["repository"]
        for comment in comments:
            text =  comment["comment"]
            user = comment["user"]
            print(text)
            if(len(text) > 50):
                if not os.path.isdir(f"resultWatson/comments/{repo_name}"):
                    os.mkdir(f"resultWatson/comments/{repo_name}")
                if not os.path.isdir(f"resultWatson/comments/{repo_name}/{user}"):
                    os.mkdir(f"resultWatson/comments/{repo_name}/{user}")
                response = request_ibm_watson_natural_language_understanding(repo=repo_name, text= text)
                writeDictToJson(response,f"{user}_{repo_name}",f"resultWatson/comments/{repo_name}/{user}/")
            

if __name__ == '__main__':
    analyse_natural_language_comments()