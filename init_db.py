import os
from util.readJson import readJson
from util.write_json_db import write_comments_json_db
pasta = './database'
arquivos_local = []
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        nome_arquivo, extensao = os.path.splitext(arquivo)
        arquivos_local.append(nome_arquivo)

comentarios_total = []    

for arquivo in arquivos_local:
    issues = readJson(arquivo)
    isFinish = issues.get("finished",False)
    if isFinish:
        issuesRepo = readJson(arquivo).get("issues",[])
        comentarios_total.extend(issuesRepo)
write_comments_json_db(comentarios_total,"init")