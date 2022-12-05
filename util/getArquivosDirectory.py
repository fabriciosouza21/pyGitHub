import os
import sys

def get_arquivo_directory(project):
    issues = []
    for diretorio, subpastas, arquivos in os.walk(project):
        for arquivo in arquivos:
            issues.append(arquivo)           
   
    return issues