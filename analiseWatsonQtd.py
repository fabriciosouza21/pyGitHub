# essa função calcular a quantidades issues restantes para finalizar as analise do ibm natural language
import math
import os
from filters.Process_text import Process_text
from filters.Remove_single_crase import Remove_single_crase
from filters.Remove_three_crase import Remove_three_crase
from filters.Remove_url import Remove_url
from util.readJson import readJson


def qtd_finalize_issues():
    DATABASE_PATH = './database/issues' 
    autores_toxicos = get_autores_toxicos()
    comments_qtd = 0
    issue_qtd = 0
    maior_comentario = 0
    total_caracteres = 0
    qtd_caracteres = set()
    arquivos_analisar = []
    #arquivos_analisar = get_arquivos_local_nao_analisados(DATABASE_PATH)
    arquivos_analisar = get_arquivos_local_analisados(DATABASE_PATH)
    for arquivo in arquivos_analisar:
        comments = get_comments(arquivo)
        issue_qtd += 1
        for comment in comments:
            if (comment["user"] in autores_toxicos and comment["comment"]):
                text = remover_junk(comment)
                if (len(text) > 50):
                    qtd_caracteres.add(len(text))
                    comments_qtd += 1
                    total_caracteres+=len(text)
                    maior_comentario = get_max(maior_comentario, len(text))
                        

    frequencia = calcula_frequencia(total_caracteres,maior_comentario, 50,qtd_caracteres)
    return {'quantidade_issues': issue_qtd,
            'comentarios':
                {
                    'quantidade_comentarios': comments_qtd,
                    'total_caracteres': total_caracteres,
                    'tamanho_maximo': maior_comentario,
                    'tamanho_medio_comentario': total_caracteres/comments_qtd,
                    'frequencia': frequencia
                }
            }

def get_arquivos_local_analisados(path):
    DATABASE_RESULT_PATH = 'resultWatson/control/'
    arquivos_local = []
    get_arquivos_local(path, arquivos_local)
    arquivos_analisados_dict = readJson(
        "issues_toxicos_arquivos", DATABASE_RESULT_PATH)
    arquivos_analisados = list(
        arquivos_analisados_dict["issues_toxicos_arquivos"])
    return  arquivos_analisados


def get_max(maior_comentario, len_text):
    if(maior_comentario<len_text):
        return len_text
    return maior_comentario

def get_comments(arquivo):
    projeto = arquivo.split("-")[:-1]
    projeto = "-".join(projeto)
    issue = readJson(arquivo, f"database/issues/{projeto}")        
    comments = issue["comments"]
    return comments


def remover_junk(comment):
    text = comment["comment"].replace("\r\n", ".")
    process = Process_text()
    remove_three_crase = Remove_three_crase()
    remove_url = Remove_url()
    remove_single_quote = Remove_single_crase()
    process.add_cleaner(remove_single_quote)
    process.add_cleaner(remove_three_crase)
    process.add_cleaner(remove_url)
    return process.run_cleaner(text)

def get_arquivos_local_nao_analisados(path):
    DATABASE_RESULT_PATH = 'resultWatson/control/'
    arquivos_local = []
    get_arquivos_local(path, arquivos_local)
    arquivos_analisados_dict = readJson(
        "issues_toxicos_arquivos", DATABASE_RESULT_PATH)
    arquivos_analisados = list(
        arquivos_analisados_dict["issues_toxicos_arquivos"])
    return  sorted(list(set(arquivos_local).difference(set(arquivos_analisados))))

def get_arquivos_local(pasta, arquivos_local):
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            nome_arquivo, extensao = os.path.splitext(arquivo)
            arquivos_local.append(nome_arquivo)
   

def get_autores_toxicos():
    autores_toxicos_dict = readJson("autores_toxico", f"database/autores")
    return list(autores_toxicos_dict["autores_toxico"])

def calcula_frequencia(total_caracteres,maior_comentario, menor_comentario,qtd_caracteres):
    frequencia = {}
    numeros_classes = int(1 + math.log2(total_caracteres))
    amplitude_classes = math.ceil(maior_comentario - menor_comentario)
    amplatude_classe = math.ceil(amplitude_classes/numeros_classes)
    initial_interval = menor_comentario
    final_interval = menor_comentario + amplatude_classe
    for _ in range(numeros_classes):
        frequencia[f"{initial_interval} a {final_interval}"] = obter_intervalo(initial_interval, final_interval, qtd_caracteres)
        initial_interval = final_interval
        final_interval = final_interval + amplatude_classe
    return frequencia

def obter_intervalo(initial_interval, final_interval , qtd_caracteres)->int:
    qtd = 0
    for caracter in qtd_caracteres:
        if(caracter>=initial_interval and caracter<final_interval):
            qtd+=1
    return qtd


if __name__ == '__main__':
    print(qtd_finalize_issues())
