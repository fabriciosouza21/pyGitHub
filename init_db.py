import os
from util.readJson import readJson
pasta = './database'
arquivos_local = []
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        nome_arquivo, extensao = os.path.splitext(arquivo)
        arquivos_local.append(nome_arquivo)
    

for arquivo in arquivos_local:
    issues = readJson(arquivo)
    isFinish = issues.get("finished",False)
    if isFinish:
        print(f"Arquivo {arquivo} foi finalizado")