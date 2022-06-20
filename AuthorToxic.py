import os
from util.readJson import readJson
from github import Github, UnknownObjectException,GithubException
from util.writeDictToJson import writeDictToJson



pasta = './resultWatson/comments/'
autores_toxico = set()
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        nome_arquivo, extensao = os.path.splitext(arquivo)
        arquivo_split = nome_arquivo.split("_")
        author = arquivo_split[0]
        project = arquivo_split[1]

        if author not in "None":
            watsonResult = readJson(nome_arquivo, f"resultWatson/comments/{project}/{author}")
            emotion = watsonResult.get("emotion", {}).get("document", {}).get("emotion", {})
           
            if len(emotion.keys()) > 0:
                if emotion["joy"] > emotion["sadness"] and emotion["joy"] > emotion["anger"] and emotion["joy"] > emotion["fear"]:
                    continue
                else:
                    
                    autores_toxico.add(author)

authors = {}
list_authors = list(autores_toxico)
authors["autores_toxico"] = sorted(list_authors)
print(authors)
writeDictToJson(authors, "autores_toxico","database/autores/")



            

