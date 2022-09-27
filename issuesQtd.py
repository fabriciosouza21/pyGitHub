import os
from util.readJson import readJson
from util.write_json_db import write_comments_json_db
pasta = './resultWatson/comments-toxico'
arquivos_local = []
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        nome_arquivo, extensao = os.path.splitext(arquivo)
        arquivos_local.append(nome_arquivo)

print(len(arquivos_local))