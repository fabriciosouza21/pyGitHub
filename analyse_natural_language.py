import time
from urllib import response
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
    pasta = './database-natural-language/issues'
    arquivos_local = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            nome_arquivo, extensao = os.path.splitext(arquivo)
            arquivos_local.append(nome_arquivo)
    for arquivo in arquivos_local:
        issue = readJson(
            f"{arquivo}.json", f"database-natural-language/issues/{arquivo}")
        comments = issue["comments"]
        for comment in comments:
                process = Process_text()
                remove_three_crase = Remove_three_crase()
                remove_url = Remove_url()
                remove_single_quote = Remove_single_crase()
                process.add_cleaner(remove_three_crase)
                process.add_cleaner(remove_url)
                process.add_cleaner(remove_single_quote)
                text = process.run_cleaner(comment["comment"])
                text = text.replace("\r\n", ".")
                text = text.replace("\n", ".")
                text = text.replace("\r", ".")
                text = text.replace("\n\r", ".")

                if(len(text) > 50 and comment.get('raw_data')):
                    if not os.path.isdir(f"resultWatson/comments-toxico-private/{comment['user']}"):
                       os.mkdir(f"resultWatson/comments-toxico-private/{comment['user']}")

                    print(arquivo)
                    print(text)
                    result=request_ibm_watson_natural_language_understanding(
						repo=issue["repository"], text=text
				)

                    time.sleep(1*2)
                    result["raw_data"] = comment["raw_data"]
                    url_infos = obter_proprietario_github(comment["raw_data"]["html_url"])
                    result["repository"] = url_infos["repositorio"]
                    result["owner"] = url_infos["proprietario"]
                    print(url_infos["repositorio"])
                    writeDictToJson(result, f"{comment['raw_data']['id']}", f"resultWatson/comments-toxico-private/{comment['user']}/")


def obter_proprietario_github(url):
    # Extrair o nome do proprietário e do repositório da URL
    partes_url = url.split('/')
    infos_url = {}
    infos_url["proprietario"] = partes_url[3]
    infos_url["repositorio"] = partes_url[4]
    return infos_url


def analyse_natural_language_comments():
    comments_autores_toxicos_arquivos = {}
    issues_toxicos_arquivos_analizados = []
    retry_erros = False

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

    arquivos_analisados_erro_dict = readJson(
        "issues_toxicos_erro", "resultWatson/control/")

    arquivos_analisados_erro_retry_dict = readJson(
        "issues_toxicos_erro_retry", "resultWatson/control/")

    arquivos_analisados = []

    if(retry_erros):
        arquivos_analisados_total = list(
            arquivos_analisados_dict["issues_toxicos_arquivos"])
        arquivos_analisados_erro = list(
            arquivos_analisados_erro_dict["issues_toxicos_arquivos_erro"])
        arquivos_analisados_erro_retry = arquivos_analisados_erro_retry_dict.get("issues_toxicos_arquivos_erro",[])

        arquivos_analisados_erro = set(arquivos_analisados_erro).difference(arquivos_analisados_erro_retry)
        arquivos_analisados = list(set(arquivos_analisados_total).difference(set(arquivos_analisados_erro)))
    else:
         arquivos_analisados = arquivos_analisados_dict["issues_toxicos_arquivos"]

    arquivos_local = set(arquivos_local).difference(set(arquivos_analisados))

    arquivos_local = list(arquivos_local)
    arquivos_local = sorted(arquivos_local)
    for arquivo in arquivos_local:
        print(arquivo)
        projeto = arquivo.split("-")[:-1]
        projeto = "-".join(projeto)

        issue = readJson(arquivo, f"database/issues/{projeto}")

        comments = issue["comments"]
        repo_name = issue["repository"]
        issues_toxicos_arquivos_analizados.append(arquivo)
        number_comment = 0
        for comment in comments:
            if (comment["user"] in autores_toxicos):

                if (comment["comment"]):
                    text = comment["comment"].replace("\r\n", ".")
                    user = comment["user"]

                    try:
                        number_comment = save_result(
                            text, repo_name, user, number_comment,arquivo)


                    except Exception as e:

                        print(f"{arquivo} - {comment['user']}")
                        if(retry_erros):
                            erros = readJson("issues_toxicos_erro_retry",
                              "resultWatson/control/")
                            erros_arquivos = erros.get(
                                "issues_toxicos_arquivos_erro", [])
                            erros_arquivos.append(arquivo)
                            erros["issues_toxicos_arquivos_erro"] = erros_arquivos
                            writeDictToJson(
                                erros, "issues_toxicos_erro_retry", "resultWatson/control/")

                            print("erro comentario retry ..............................................")
                            time.sleep(1*20)
                            continue
                        else:

                            erros = readJson("issues_toxicos_erro",
                                            "resultWatson/control/")
                            erros_arquivos = erros.get(
                                "issues_toxicos_arquivos_erro", [])
                            erros_arquivos.append(arquivo)
                            erros["issues_toxicos_arquivos_erro"] = erros_arquivos
                            writeDictToJson(
                                erros, "issues_toxicos_erro", "resultWatson/control/")

                            arquivos_analisados.append(arquivo)
                            comments_autores_toxicos_arquivos["issues_toxicos_arquivos"] = arquivos_analisados
                            writeDictToJson(comments_autores_toxicos_arquivos,
                                        "issues_toxicos_arquivos", f"resultWatson/control/")
                            print(e)
                            print("erro comentario ..............................................")
                            time.sleep(1*20)
                            continue

        arquivos_analisados.append(arquivo)
        comments_autores_toxicos_arquivos["issues_toxicos_arquivos"] = arquivos_analisados
        writeDictToJson(comments_autores_toxicos_arquivos,
                                        "issues_toxicos_arquivos", f"resultWatson/control/")
        if(retry_erros):
            erros = readJson("issues_toxicos_erro_retry",
                              "resultWatson/control/")
            erros_arquivos = erros.get(
                "issues_toxicos_arquivos_erro", [])
            erros_arquivos.append(arquivo)
            erros["issues_toxicos_arquivos_erro"] = erros_arquivos
            writeDictToJson(
                erros, "issues_toxicos_erro_retry", "resultWatson/control/")





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
        writeDictToJson(response,f"{user}_{repo_name}_{arquivo}_{number_comment}",f"resultWatson/comments-toxico/{repo_name}/{user}/")
        number_comment = number_comment + 1
    return number_comment

if __name__ == '__main__':
    analyse_natural_language()



