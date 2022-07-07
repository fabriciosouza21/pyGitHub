from urllib import response

from numpy import number
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
    pasta = './database/issues'
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
    comments_autores_toxicos_arquivos = {}
    issues_toxicos_arquivos_analizados = []

    autores_toxicos_dict = readJson("autores_toxico", f"database/autores")
    autores_toxicos = list(autores_toxicos_dict["autores_toxico"])
    comments_qtd = 0
    pasta = './database/issues'
    arquivos_local = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            nome_arquivo, extensao = os.path.splitext(arquivo)
            arquivos_local.append(nome_arquivo)
    
    arquivos_local = sorted(arquivos_local)
    for arquivo in arquivos_local:
        projeto = arquivo.split("-")[:-1]
        projeto = "-".join(projeto)
        
        issue = readJson(arquivo, f"database/issues/{projeto}")
        
        comments = issue["comments"]
        repo_name = issue["repository"]
        for comment in comments:
            if(comment["user"] in autores_toxicos):
                number_comment = 1
                text =  comment["comment"]
                user = comment["user"]
                comments_qtd+=1
                issues_toxicos_arquivos.append(arquivo)
                try:
                    number_comment = save_result(text, repo_name, user, number_comment)
                
                except Exception as e:
                    print(e)
                    print(f"{arquivo} - {comment['user']}")
                    


def save_result(text, repo_name, user, number_comment):
    if(len(text) > 50):
        if not os.path.isdir(f"resultWatson/comments-toxico/{repo_name}"):
            os.mkdir(f"resultWatson/comments-toxico/{repo_name}")
        if not os.path.isdir(f"resultWatson/comments-toxico/{repo_name}/{user}"):
            os.mkdir(f"resultWatson/comments-toxico/{repo_name}/{user}")
        response = request_ibm_watson_natural_language_understanding(repo=repo_name, text= text)
        if(os.path.isfile(f"resultWatson/comments-toxico/{repo_name}/{user}/{user}_{repo_name}_{number_comment}.json")):
            number_comment += 1
        writeDictToJson(response,f"{user}_{repo_name}_{number_comment}",f"resultWatson/comments-toxico/{repo_name}/{user}/")
        return number_comment

if __name__ == '__main__':
    analyse_natural_language_comments()