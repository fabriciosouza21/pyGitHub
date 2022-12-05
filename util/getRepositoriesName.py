import os
import sys


def get_repositories_name(path):
    repositories = []
    for diretorio, subpastas, arquivos in os.walk(path):
        for subpasta in subpastas:
            repositories.append(subpasta)           
   
    return repositories