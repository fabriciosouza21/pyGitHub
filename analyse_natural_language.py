from util.readJson import readJson
import os
from util.readJson import readJson
from util.write_json_db import write_comments_json_db
from util.natural_language_understanding import request_ibm_watson_natural_language_understanding



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


if __name__ == '__main__':
    analyse_natural_language()