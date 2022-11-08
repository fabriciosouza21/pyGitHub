import time
from urllib import response

from numpy import number
from filters.Process_text import Process_text
from filters.Remove_three_crase import Remove_three_crase
from filters.Remove_url import Remove_url
from filters.Remove_single_crase import Remove_single_crase
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
        issue = readJson(
            arquivo, f"database-natural-language/issues/{arquivo}")
        comments = map(get_comments, list(issue["comments"]))
        text = " .".join(comments)
        request_ibm_watson_natural_language_understanding(
            repo=issue["repository"], text=text)


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

    arquivos_analisados_dict = readJson(
        "issues_toxicos_arquivos", "resultWatson/control/")
    
    arquivos_analisados = list(
        arquivos_analisados_dict["issues_toxicos_arquivos"])
    arquivos_local = set(arquivos_local).difference(set(arquivos_analisados))
    list(arquivos_local)
    arquivos_local = sorted(arquivos_local)
    for arquivo in arquivos_local:
        print(arquivo)
        projeto = arquivo.split("-")[:-1]
        projeto = "-".join(projeto)

        issue = readJson(arquivo, f"database/issues/{projeto}")

        comments = issue["comments"]
        repo_name = issue["repository"]
        issues_toxicos_arquivos_analizados.append(arquivo)
        for comment in comments:
            if (comment["user"] in autores_toxicos):
                number_comment = 1
                if (comment["comment"]):
                    text = comment["comment"].replace("\r\n", ".")
                    user = comment["user"]
                    comments_qtd += 1

                    try:
                        number_comment = save_result(
                            text, repo_name, user, number_comment,arquivo)
                        
                        
                                                
                    except Exception as e:
                        print(e)
                        print(f"{arquivo} - {comment['user']}")
                        erros = readJson("issues_toxicos_erro",
                                         "resultWatson/control/")
                        erros_arquivos = erros.get(
                            "issues_toxicos_arquivos_erro", [])
                        erros_arquivos.append(arquivo)
                        erros["issues_toxicos_arquivos_erro"] = erros_arquivos
                        writeDictToJson(
                            erros, "issues_toxicos_erro", "resultWatson/control/")

                        print("erro comentario ..............................................")
                        time.sleep(1*20)
                        continue
        
        arquivos_analisados.append(arquivo)
        comments_autores_toxicos_arquivos["issues_toxicos_arquivos"] = arquivos_analisados
        writeDictToJson(comments_autores_toxicos_arquivos,
                                        "issues_toxicos_arquivos", f"resultWatson/control/")
    
    


def save_result(text, repo_name, user, number_comment,arquivo):
    process = Process_text()
    remove_three_crase = Remove_three_crase()
    remove_url = Remove_url()
    remove_single_quote = Remove_single_crase()
    process.add_cleaner(remove_three_crase)
    process.add_cleaner(remove_url)
    process.add_cleaner(remove_single_quote)
    text = process.run_cleaner(text)
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
    while True:
        print("Analisando comentários......................................")
        analyse_natural_language_comments()
        

        
        